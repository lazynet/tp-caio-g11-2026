# AGENTS.md — tp-caio-2026

`AGENTS.md` is the portable contract for coding agents. Keep repository rules
here; do not add a `CLAUDE.md`. Verify with `lh repo instructions .`.

## What this repo owns

The final integrative assignment (Trabajo Integrador Final) of the UTN BA
*Diplomatura Chief AI Officer (CAIO)*: a **12-month CAIO Master Plan** for
**Flexibility** (flexibility SRL, Argentine software provider to fintech and
banking clients), defended before a board.

The plan must integrate:

- Integral strategy: architecture, governance, security, people plan, finance.
- Technical, financial and cultural roadmap, with milestones and success criteria.
- Financial storytelling for a skeptical CFO.
- Risk-adjusted roadmap: scenarios, contingencies, reversible vs irreversible decisions.
- Defense prep: storyline, anticipated objections, evidence.

**Format rule:** max 10 slides. What the board must *decide* goes in the
slides; everything that *supports* it goes in annexes.

**Team:** Grupo 11, 5 members. Teammate onboarding lives in `README.md`; keep
it in sync when the workflow changes.

**Everything is generated.** `plan/slides.md` (Marp-compatible markdown, one
slide per `---`) is the only deck source; `scripts/build-deck.sh` renders it
to `out/` (gitignored) with Marp and pandoc so formats can be compared. Never
edit a rendered deck; fix the markdown and rebuild.

## Key dates

| Milestone | Date |
|---|---|
| Team formed + scope chosen | 2026-10-13 (suggested) |
| Version for peer review | 2026-10-27 |
| Final delivery | 2026-10-28 → 2026-11-04 |
| Top-3 voting | 2026-11-05 → 2026-11-08 |
| Board defense (tentative) | 2026-11-10 18:30 |

## Layout

| Path | Holds |
|---|---|
| `context/` | Facts about Flexibility the plan rests on, each with its source |
| `material/` | Index of course material: which unit/framework backs which section |
| `plan/slides.md` | The 10 slides — source of truth for the deck |
| `plan/annexes/` | One file per annex, referenced from the slides |
| `defense/` | Storyline, objection bank, evidence map |
| `reviews/` | Output of board reviews and peer review, dated |
| `scripts/build-deck.sh` | Renders the deck: `all` (default), `marp` or `pandoc` |

## Sources

- Course material (PDFs, frameworks): Google Drive
  `~/Library/CloudStorage/GoogleDrive-martin@example.invalid/Mi unidad/Personales/Diplomatura Chief AI Officer (CAIO)/`.
  Read from there; never copy the PDFs into the repo.
- Consolidated notebook: https://notebook.google.com/notebook/57ec4d6d-41a0-4030-9273-9bfc94cfb4ae
  (not reachable by agents; Martin pastes excerpts into `material/`).
- Class notes: LazyMind `2-Areas/Trabajo/Reuniones/* - Diplomatura Chief AI Officer (CAIO)*`
  (QMD collection `lazy-lazymind-areas`).

## Rules

- **Audience is the whole cohort.** Peers, another team and the teaching staff
  read everything in `plan/`, `defense/` and `reviews/`. Flexibility internal
  data (client names, contract figures, rates, P&L, headcount by person) never
  lands there verbatim: use ranges, ratios or anonymized clients, and record the
  real source only in `context/` with `confidential: true` in frontmatter.
  Agents with access to `flex-*` QMD collections must apply this before writing.
- **Every number has a source.** A figure in a slide traces to an annex, and the
  annex states the assumption or the source. Assumptions are labeled as such.
- **One owner per section.** Each slide/annex declares its owner agent in
  frontmatter (`owner: finance`); others propose, the owner writes.
- **Board review before peer review.** Run `/board-review` on any slide set
  before it goes to the team or the peer-review team.
- Deliverable content is in Spanish (rioplatense, executive register). File
  names, frontmatter keys and this contract stay in English.
- Commits: `type: short description`, no trailers.

## Agents

Synthetic copilots per role in `.claude/agents/`. Each owns a lens, not a file
tree; `caio` integrates.

| Agent | Owns | Slide/annex focus |
|---|---|---|
| `caio` | Storyline, integration, risk-adjusted roadmap | Exec summary, roadmap, decisions asked |
| `architect` | Target architecture, platform, data, technical roadmap | Architecture + tech milestones |
| `governance` | AI governance, security, compliance, responsible AI | Operating model, policies, controls |
| `people` | People plan, org design, change and cultural roadmap | Talent, adoption, culture milestones |
| `finance` | Business case, budget, ROI, CFO narrative | Financial storytelling, scenarios |
| `board` | Adversarial review as board / skeptical CFO / grader | Objections, gaps vs assignment |
