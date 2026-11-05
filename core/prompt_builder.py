class PromptBuilder:
    """Constructor especializado de prompts industriales de nivel de ingeniería bajo estándar MAN-F-054."""

    @staticmethod
    def build_acr_prompt(title: str, area: str, equipment: str, description: str, leader: str = "", participants: str = "", attachments_text: str = "") -> str:
        attachment_section = f"\nEVIDENCIAS Y DOCUMENTOS ADJUNTOS ANALIZADOS:\n{attachments_text}\n" if attachments_text else ""
        return f"""
Actúa como un especialista senior en:
- Análisis de Causa Raíz (RCA)
- Metodología ACR
- Metodología AFA
- Mantenimiento Mecánico
- Mantenimiento Eléctrico
- Automatización Industrial
- Confiabilidad y Disponibilidad de Equipos
- Ingeniería de Manufactura
- Análisis de Fallas
- Lean Manufacturing
- Six Sigma
- Industria de Explosivos

Tu objetivo es analizar el evento reportado y completar rigurosamente el formulario oficial ACR/AFA bajo el estándar MAN-F-054 con un enfoque técnico e institucional de nivel gerencial.
PROHIBIDO copiar textualmente los errores ortográficos o la redacción informal del usuario; debes transformar, sintetizar y redactar con vocabulario corporativo apto para auditorías.

INFORMACIÓN GENERAL DEL EVENTO:
- Título del Evento: {title}
- Área / Sistema: {area}
- Equipo / Tag: {equipment}
- Líder del Análisis: {leader or 'Ingeniero de Confiabilidad'}
- Participantes: {participants or 'Equipo Multidisciplinario de Confiabilidad y Operaciones'}
- Descripción Bruta del Evento / Problema: {description}
{attachment_section}

REGLAS TÉCNICAS OBLIGATORIAS:
1. Identificar el problema principal y generar el Problema Enfocado.
2. Analizar el evento diferenciando claramente: Síntoma, Falla observable, Causa física, Causa contribuyente y Causa raíz sistémica.
3. Construir el análisis de los 5 Porqués con lógica causal estricta, sin repetir información, conduciendo a causas administrables, evitando concluir en errores humanos simples y llegando a causas sistémicas de diseño, automatización o gestión.
4. Si el problema involucra componentes mecánicos, considera: desgaste, deformación, desalineamiento, holguras, interferencia, tolerancias, lubricación y fatiga.
5. Si el problema es eléctrico o de automatización, considera: alimentación, cableado, sensores, lógica PLC, HMI, comunicaciones, secuencia, interlocks y sincronización.
6. Completar de forma exhaustiva el desglose 5W + 2H (Qué, Quién, Dónde, Cuándo, Cuánto, Cómo, Por qué).
7. Emitir un resultado estructurado con hallazgos detallados, defendibles para auditorías gerenciales.

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "participantes": "Líder y lista de participantes técnicos",
    "problema_enfocado": "Redacción ejecutiva formal del problema enfocado bajo estándar MAN-F-054",
    "que_paso": "Descripción técnica detallada del qué sucedió y secuencia lógica",
    "como_ocurrio": "Descripción analítica de la propagación del fallo, secuencia de estaciones o modo de falla",
    "quien_detecto": "Detalle formal de quién detectó y contexto operativo",
    "cuanto_perdida": "Evaluación del impacto, tiempo de parada, riesgo de seguridad o pérdida de OEE",
    "cual_material": "Identificación técnica de componentes, lotes, marcas o materiales involucrados",
    "where_located": "Estación o ubicación técnica precisa del evento",
    "when_started": "Momento temporal y modo de operación del sistema",
    "accion_inmediata": "Acción inmediata de contención y seguridad ejecutada",
    "porque1": "Por qué 1: Análisis técnico de la manifestación física inicial o síntoma",
    "porque2": "Por qué 2: Análisis de la condición o anomalía en el flujo, secuencia o componentes",
    "porque3": "Por qué 3: Deficiencia en la validación de interlocks, sensores o pautas",
    "porque4": "Por qué 4: Brecha en la lógica de control, diseño o estándar operativo",
    "porque5": "Por qué 5 (Causa Raíz Sistémica): Deficiencia estructural en la ingeniería del proceso, automatización o gestión de activos",
    "causa_fisica": "Descripción formal de la causa física directa del evento",
    "causa_contribuyente": "Factores operacionales, ambientales o de entorno contribuyentes",
    "causa_raiz": "Causa raíz sistémica fundamental validada",
    "acciones": [
        {{
            "accion": "Acción inmediata de verificación y contención técnica",
            "objetivo": "Mitigar riesgo operativo inmediato",
            "responsable": "Supervisión de Operaciones / Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva sobre componentes, sensores o lógica de secuencia",
            "objetivo": "Restaurar fiabilidad operativa",
            "responsable": "Mantenimiento / Automatización",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva basada en RCM (Actualización de pautas y validación de interlocks)",
            "objetivo": "Prevenir recurrencia de fallas operativas o de secuencia",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Acción sobre la Causa Raíz (Rediseño, mejora de lógica PLC o gestión de activos)",
            "objetivo": "Eliminar sistémicamente la vulnerabilidad",
            "responsable": "Gerencia de Ingeniería / Operaciones",
            "prioridad": "Alta",
            "fecha": "2027-01-30",
            "estado": "Pendiente",
            "tipo": "Causa Raíz"
        }}
    ]
}}
"""

    @staticmethod
    def build_afa_prompt(title: str, area: str, equipment: str, description: str, leader: str = "", participants: str = "", attachments_text: str = "") -> str:
        attachment_section = f"\nEVIDENCIAS Y DOCUMENTOS ADJUNTOS ANALIZADOS:\n{attachments_text}\n" if attachments_text else ""
        return f"""
Actúa como un especialista senior en Análisis de Fallas (AFA), metodología FMEA, Mantenimiento Mecánico/Eléctrico, Automatización Industrial y Confiabilidad de Equipos.
A partir de la descripción bruta proporcionada, DEBES ANALIZAR, TRANSFORMAR y REDACTAR formalmente un Análisis de Falla (AFA) estructurado y riguroso bajo el estándar MAN-F-054, orientado a la industria de procesos y explosivos, con vocabulario técnico institucional para la gerencia.

INFORMACIÓN GENERAL DE LA FALLA:
- Título del AFA: {title}
- Área / Sistema: {area}
- Equipo / Componente / Tag: {equipment}
- Líder del AFA: {leader or 'Especialista en Confiabilidad'}
- Participantes: {participants or 'Equipo Multidisciplinario de Mantenimiento'}
- Descripción Bruta del Modo de Falla y Síntomas: {description}
{attachment_section}

REGLAS TÉCNICAS OBLIGATORIAS:
1. Identificar con precisión el Modo de Falla, el Efecto local/sistémico y la Consecuencia operativa y de seguridad.
2. Considerar factores de desgaste, fatiga, desalineamiento, holguras, tolerancias, lubricación, fallas de sensores o secuencias lógicas de PLC según aplique.
3. Desarrollar el árbol de los 5 Porqués con rigor analítico de ingeniería.
4. Generar planes de acción estructurados con acciones inmediatas, correctivas, preventivas y sobre la causa raíz.

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "participantes": "Líder y participantes del AFA",
    "problema_enfocado": "Descripción formal del modo de falla enfocado bajo estándar MAN-F-054",
    "que_paso": "Análisis formal del qué sucedió y desviación técnica respecto a la condición nominal",
    "como_ocurrio": "Análisis del cómo se propagó el modo de falla en el equipo o sistema",
    "quien_detecto": "Contexto de detección del fallo y condiciones operativas",
    "cuanto_perdida": "Impacto y consecuencia en la disponibilidad, OEE y costos",
    "cual_material": "Componentes, partes y materiales críticos afectados",
    "where_located": "Ubicación técnica precisa del componente en falla",
    "when_started": "Momento de inicio de la degradación o anomalía",
    "accion_inmediata": "Acción inmediata de contención ejecutada",
    "modo_falla": "Descripción técnica formal del Modo de Falla",
    "effect": "Efecto local y sistémico de la falla",
    "consequence": "Consecuencia en seguridad, medio ambiente y costos",
    "porque1": "Por qué 1: Causa física directa del modo de falla",
    "porque2": "Por qué 2: Mecanismo de esfuerzo, desgaste o condición anómala",
    "porque3": "Por qué 3: Condición latente o factor contribuyente en el sistema",
    "porque4": "Por qué 4: Brecha en la estrategia predictiva, preventiva o lógica de control",
    "porque5": "Por qué 5 (Causa Raíz Sistémica): Deficiencia estructural en la gestión de activos, diseño o automatización",
    "causa_fisica": "Descripción formal de la causa física de la falla",
    "causa_contribuyente": "Factores operacionales y de entorno contribuyentes",
    "causa_raiz": "Causa raíz fundamental identificada",
    "actions": [
        {{
            "accion": "Acción inmediata de contención del riesgo",
            "objetivo": "Mitigar impacto operativo",
            "responsable": "Operaciones / Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva sobre el componente o sistema",
            "objetivo": "Restaurar integridad técnica",
            "responsable": "Mantenimiento Mecánico / Eléctrico",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva (Actualización RCM / Pautas / Sensores)",
            "objetivo": "Prevenir recurrencia del modo de falla",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Acción sobre la Causa Raíz (Modificación de diseño, lógica o rediseño sistémico)",
            "objetivo": "Eliminar la causa raíz definitivamente",
            "responsable": "Jefatura de Mantenimiento / Ingeniería",
            "prioridad": "Alta",
            "fecha": "2027-01-30",
            "estado": "Pendiente",
            "tipo": "Causa Raíz"
        }}
    ]
}}
"""
