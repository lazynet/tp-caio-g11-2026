import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


SCRIPT = Path(
    os.environ.get(
        "LEAK_CHECK_SCRIPT",
        Path(__file__).resolve().parents[1] / "scripts/leak-check.sh",
    )
)
TERM = "Synthetic" + "Customer"
MAIL = "fake.person" + "@" + "flexibility" + ".com.ar"
KEY = "-----BEGIN " + "RSA PRIVATE " + "KEY-----"
CUIT = "30-" + "12345678" + "-9"
CONFIDENTIAL = "confidential:" + " true"


class LeakCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.env = dict(os.environ, LEAK_DENYLIST="")
        for key in tuple(self.env):
            if key.startswith("GIT_"):
                del self.env[key]
        self.git("init", "-q")

    def git(self, *args):
        return subprocess.run(
            ["git", *args], cwd=self.repo, env=self.env, check=True, capture_output=True
        )

    def stage(self, path="draft.md", content="public draft\n"):
        target = self.repo / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content)
        self.git("add", "--", path)
        return target

    def scan(self, *args, shell="/bin/bash"):
        return subprocess.run(
            [shell, str(SCRIPT), *args],
            cwd=self.repo,
            env=self.env,
            capture_output=True,
            text=True,
        )

    def output(self, result):
        return result.stdout + result.stderr

    def assert_redacted(self, result, *values):
        for value in values:
            self.assertNotIn(value, self.output(result))

    def test_bash32_and_available_bash(self):
        self.stage()
        for shell in sorted({"/bin/bash", shutil.which("bash")} - {None}):
            with self.subTest(shell=shell):
                version = subprocess.run(
                    [shell, "--version"], capture_output=True, text=True, check=True
                ).stdout.splitlines()[0]
                print("Shell verificado: " + version)
                for mode in ("--all", "--staged"):
                    result = self.scan(mode, shell=shell)
                    self.assertEqual(result.returncode, 0, self.output(result))
                    self.assertIn("PARCIAL", self.output(result))
                    self.assertNotIn("unbound variable", self.output(result))

    def test_private_guard(self):
        path = "private/" + TERM + ".md"
        self.stage(path)
        for mode in ("--all", "--staged"):
            result = self.scan(mode)
            self.assertEqual(result.returncode, 1, self.output(result))
            self.assertIn("archivo privado versionado", result.stderr)
            self.assert_redacted(result, path, TERM)

    def test_fixed_patterns_and_redaction(self):
        for value, category in (
            (MAIL, "mail corporativo"),
            (KEY, "clave privada"),
            (CUIT, "CUIT"),
            (CONFIDENTIAL, "confidencialidad"),
        ):
            with self.subTest(category=category):
                path = TERM + "\n" + ".md"
                self.stage(path, "public\n" + value + "\n")
                result = self.scan("--all")
                self.assertEqual(result.returncode, 1, self.output(result))
                self.assertIn(category, result.stderr)
                self.assertIn("línea 2", result.stderr)
                self.assert_redacted(result, value, TERM, path)

    def test_index_differs_from_worktree(self):
        path = self.stage(content=MAIL + "\n")
        path.write_text("public\n")
        self.assertEqual(self.scan("--staged").returncode, 1)
        self.assertEqual(self.scan("--all").returncode, 0)
        self.git("add", "draft.md")
        path.write_text(MAIL + "\n")
        self.assertEqual(self.scan("--staged").returncode, 0)
        self.assertEqual(self.scan("--all").returncode, 1)

    def test_staged_deleted_file_is_ignored(self):
        self.stage("private/draft.md")
        self.git("rm", "--cached", "private/draft.md")
        self.assertEqual(self.scan().returncode, 0)

    def test_denylist_env_file_precedence_and_word_matching(self):
        self.stage(content="prefix" + TERM + "suffix\n")
        self.env["LEAK_DENYLIST"] = TERM
        self.assertEqual(self.scan("--strict").returncode, 0)
        self.stage(content=TERM.lower() + "\n")
        result = self.scan("--all", "--strict")
        self.assertEqual(result.returncode, 1)
        self.assertIn("denylist privada", result.stderr)
        self.assert_redacted(result, TERM, TERM.lower())
        self.env["LEAK_DENYLIST"] = ""
        (self.repo / ".leak-denylist").write_text("# ignored\n\n" + TERM + "\n")
        self.assertEqual(self.scan("--strict").returncode, 1)
        self.env["LEAK_DENYLIST"] = "Different" + "Term"
        result = self.scan("--strict")
        self.assertEqual(result.returncode, 0, self.output(result))
        self.assertIn("COMPLETA", result.stdout)

    def test_missing_empty_and_comment_denylist(self):
        self.stage()
        for denylist in ("", "\n  \n", "# ignored\n"):
            self.env["LEAK_DENYLIST"] = denylist
            result = self.scan("--all", "--strict")
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("✓", self.output(result))
            self.assertEqual(self.scan("--all").returncode, 0)

    def test_denylist_read_error_is_redacted(self):
        self.stage()
        (self.repo / ".leak-denylist").mkdir()
        result = self.scan()
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("✓", self.output(result))
        self.assertNotIn(str(self.repo), self.output(result))

    def test_invalid_arguments(self):
        for args in (
            ("--unknown",),
            ("--all", "extra"),
            ("--strict", "--strict"),
            ("--all", "--staged"),
        ):
            result = self.scan(*args)
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("✓", self.output(result))
            self.assertNotIn("extra", self.output(result))

    def test_non_repository_error(self):
        (self.repo / ".git").rename(self.repo / ".git-hidden")
        env = dict(self.env, GIT_CEILING_DIRECTORIES=str(self.repo.parent))
        result = subprocess.run(
            ["/bin/bash", str(SCRIPT)],
            cwd=self.repo,
            env=env,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("✓", self.output(result))
        self.assertNotIn(str(self.repo.parent), self.output(result))

    def fake_git(self, command, code, stdout="", stderr=""):
        real_git = shutil.which("git")
        directory = self.repo / "bin"
        directory.mkdir(exist_ok=True)
        wrapper = directory / "git"
        wrapper.write_text(
            "#!/usr/bin/env python3\nimport os, sys\n"
            + "if sys.argv[1] == "
            + repr(command)
            + ":\n"
            + "    sys.stdout.write("
            + repr(stdout)
            + ")\n"
            + "    sys.stderr.write("
            + repr(stderr)
            + ")\n"
            + "    sys.exit("
            + str(code)
            + ")\n"
            + "os.execv("
            + repr(real_git)
            + ", ["
            + repr(real_git)
            + ", *sys.argv[1:]])\n"
        )
        wrapper.chmod(0o755)
        self.env["PATH"] = str(directory) + os.pathsep + os.environ["PATH"]

    def test_git_and_scanner_errors_never_succeed_or_leak(self):
        self.stage()
        for command in ("rev-parse", "diff", "ls-files", "grep"):
            with self.subTest(command=command):
                self.fake_git(command, 128, stdout=KEY, stderr=MAIL + TERM)
                result = self.scan("--all" if command == "ls-files" else "--staged")
                self.assertEqual(result.returncode, 2)
                self.assertNotIn("✓", self.output(result))
                self.assert_redacted(result, KEY, MAIL, TERM)

    def test_malformed_scanner_output_is_redacted(self):
        self.stage()
        self.fake_git("grep", 0, stdout=MAIL + TERM, stderr=KEY)
        result = self.scan()
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("✓", self.output(result))
        self.assert_redacted(result, MAIL, TERM, KEY)


if __name__ == "__main__":
    unittest.main(verbosity=2)
