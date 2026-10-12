---
type: Concepto
title: AIMM, uso en un diagnóstico
description: Reglas para aplicar la escala AIMM en un diagnóstico, sus limitaciones y los marcos que la complementan.
tags: [diagnostico, madurez]
status: draft
sources:
  - id: aimm
    resource: AIMM (Gartner) 2026.pdf
    title: AIMM (Gartner), documento de referencia de la cursada, pp. 2-3
generated: { by: claude-code/claude-sonnet-5-5, at: 2026-10-11T23:00:00Z }
---

Parte del [AIMM](/frameworks/aimm-gartner.md); niveles en [AIMM, los 5 niveles](/frameworks/aimm-niveles.md). Todo lo que sigue es criterio del documento de la cursada, no de Gartner.[^aimm]

# Cómo usarlo

1. **No asignar un único nivel a toda la organización.** La madurez es despareja: un área puede estar en 3 y el resto en 1. Evaluar por dimensión y por unidad; quedarse con el perfil, no con el promedio.
2. **Evaluar por separado** datos, talento, gobernanza, infraestructura y adopción. El nivel global lo determina la dimensión más débil, no la más fuerte.
3. **Buscar evidencia, no percepción:** ¿hay un sistema en producción?, ¿quién lo monitorea?, ¿qué pasó la última vez que falló?
4. **No saltear niveles.** Pasar de 1 a 4 comprando tecnología es el patrón clásico de proyecto fallido: la capacidad organizacional no se adquiere.
5. **Definir el nivel objetivo** con horizonte temporal y criterio de verificación.

# Limitaciones

* Es descriptivo, no prescriptivo: nombra estados, no dice cómo llegar.
* Es anterior a la ola de IA generativa: un uso masivo de herramientas de terceros puede convivir con capacidad propia casi nula.
* No incorpora una dimensión de riesgo o cumplimiento normativo.
* Por su difusión, se usa a menudo como etiqueta retórica más que como instrumento de diagnóstico.

# Marcos complementarios

| Instrumento | Aporta | Acceso |
|---|---|---|
| NIST AI Risk Management Framework 1.0 | Gestión de riesgos: Govern / Map / Measure / Manage | Gratuito |
| [Microsoft Responsible AI Maturity Model](/frameworks/microsoft-rai-maturity.md) | Madurez en IA responsable, cinco niveles | Gratuito |
| ISO/IEC 42001:2023 | Sistema de gestión de IA certificable | Norma paga |
| [Reglamento (UE) 2024/1689](/frameworks/eu-ai-act.md) | Obligaciones legales por nivel de riesgo | Gratuito (EUR-Lex) |

Otro diagnóstico por pilares: [Cisco AI Readiness Index](/frameworks/cisco-ai-readiness.md).

[^aimm]: AIMM (Gartner), documento de referencia de la cursada, pp. 2-3
