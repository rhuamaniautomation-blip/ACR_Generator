class PromptBuilder:
    """Constructor especializado de prompts industriales de nivel de ingeniería bajo estándar MAN-F-054."""

    @staticmethod
    def build_acr_prompt(title: str, area: str, equipment: str, description: str, leader: str = "", participants: str = "", attachments_text: str = "") -> str:
        attachment_section = f"\nEVIDENCIAS Y DOCUMENTOS ADJUNTOS ANALIZADOS:\n{attachments_text}\n" if attachments_text else ""
        return f"""
Actúa como un equipo multidisciplinario senior de Ingeniería de Confiabilidad y Mantenimiento Industrial (Especialista RCA/ACR Senior, Reliability Engineer y Gerente de Confiabilidad).
A partir de la descripción bruta proporcionada por el usuario, DEBES ANALIZAR, TRANSFORMAR y REDACTAR de forma profesional, estructurada, formal y con rigor técnico de ingeniería cada uno de los campos del formato oficial MAN-F-054. 
PROHIBIDO copiar textualmente los errores ortográficos o de redacción del usuario; debes sintetizar y redactar con vocabulario corporativo e institucional de nivel gerencial.

INFORMACIÓN GENERAL DEL EVENTO:
- Título del Evento: {title}
- Área / Sistema: {area}
- Equipo / Tag: {equipment}
- Líder del Análisis: {leader or 'Ingeniero de Confiabilidad'}
- Participantes: {participants or 'Equipo de Mantenimiento y Operaciones'}
- Descripción Bruta del Evento / Problema: {description}
{attachment_section}

REGLAS OBLIGATORIAS DE INGENIERÍA PARA EL ESTÁNDAR MAN-F-054:
1. DESGLOSE 5W + 2H PROFESIONAL Y TÉCNICO:
   - Problema Enfocado: Síntesis ejecutiva y formal del problema detectado para la gerencia.
   - ¿Qué?: Qué sucedió exactamente, tarea que falló, secuencia lógica y condición nominal esperada.
   - ¿Cómo?: Mecanismo técnico detallado de cómo se originó y propagó la falla o error de secuencia.
   - ¿Quién?: Quién detectó el evento, quién operaba y a quién no le afectó.
   - ¿Cuánto?: Cuantificación del impacto, tiempo de parada, riesgo de seguridad o pérdida de OEE.
   - ¿Cuál?: Componentes, números de lote (ej. Pyro G, BF), marcas, formatos o materiales implicados.
   - ¿Dónde?: Estación o ubicación técnica exacta donde nace o se manifiesta el problema (ej. Estación ST22 / ST23).
   - ¿Cuándo?: Fecha, hora exacta y modo de operación (ej. Automático, vaciado EMPTYN, producción normal).
   - Acción Inmediata: Contención operativa ejecutada (parada de emergencia, evacuación, revisión de herramental).

2. ÁRBOL DE LOS 5 PORQUÉS RIGUROSO (MÍNIMO Y OBLIGATORIO 5 NIVELES):
   - Cada Porqué debe ser un análisis técnico avanzado de ingeniería. Prohibido usar respuestas simples o superficiales.
   - Prohibido atribuir la causa raíz a "error humano" simple; profundizar en deficiencias de lógica de control, automatización, sincronización de estaciones o gestión de activos.
   - Nivel 1: Causa física o secuencia inmediata del fallo.
   - Nivel 2: Condición técnica o operacional facilitadora en el sistema.
   - Nivel 3: Deficiencia en la pauta de control, sensor o validación de secuencia.
   - Nivel 4: Brecha en el diseño de automatización o validación de interlocks.
   - Nivel 5: Causa Raíz Sistémica Organizacional / Ingeniería de Confiabilidad y Automatización.

3. ACCIONES Y PLANES DE SEGUIMIENTO (CORRECTIVAS, PREVENTIVAS Y CAUSA RAÍZ):
   - Definir acciones específicas asignando objetivo gerencial, responsable por cargo corporativo, prioridad, fecha tentativa y tipo.

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "participantes": "Líder y lista de participantes técnicos",
    "problema_enfocado": "Redacción ejecutiva formal del problema enfocado bajo estándar MAN-F-054",
    "que_paso": "Descripción técnica del qué sucedió y secuencia de eventos",
    "como_ocurrio": "Descripción analítica del cómo ocurrió la propagación del fallo",
    "quien_detecto": "Detalle formal de quién detectó y contexto operativo",
    "cuanto_perdida": "Evaluación del impacto, tiempo de parada y criticidad del riesgo",
    "cual_material": "Identificación técnica de componentes, lotes y materiales involucrados",
    "where_located": "Estación o ubicación técnica precisa del evento",
    "when_started": "Momento temporal y modo de operación del sistema",
    "accion_inmediata": "Acción inmediata de contención y seguridad ejecutada",
    "porque1": "Por qué 1: Análisis técnico de la manifestación física inicial",
    "porque2": "Por qué 2: Análisis de la condición o anomalía en el flujo/secuencia",
    "porque3": "Por qué 3: Deficiencia en la validación de interlocks o sensores",
    "porque4": "Por qué 4: Brecha en la lógica de control o estándar operativo",
    "porque5": "Por qué 5 (Causa Raíz Sistémica): Deficiencia estructural en la ingeniería del proceso o sistema de gestión",
    "causa_fisica": "Descripción formal de la causa física directa del evento",
    "causa_contribuyente": "Factores operacionales y de entorno contribuyentes",
    "causa_raiz": "Causa raíz sistémica fundamental validada",
    "acciones": [
        {{
            "accion": "Acción inmediata de verificación y contención técnica",
            "objetivo": "Mitigar riesgo operativo inmediato",
            "responsable": "Supervisión de Operaciones",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva sobre sensores o lógica de secuencia",
            "objetivo": "Restaurar fiabilidad operativa",
            "responsable": "Mantenimiento / Automatización",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva basada en RCM (Actualización de pautas y validación de interlocks)",
            "objetivo": "Prevenir recurrencia de fallas de secuencia",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Acción sobre la Causa Raíz (Rediseño o mejora del sistema de control y verificación de herramental)",
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
Actúa como un Especialista Senior en FMEA/AFA y Reliability Engineer.
A partir de la descripción bruta proporcionada, DEBES ANALIZAR, TRANSFORMAR y REDACTAR formalmente un Análisis de Falla (AFA / FMEA) estructurado y riguroso bajo el estándar MAN-F-054, con vocabulario técnico institucional para la gerencia.

INFORMACIÓN GENERAL DE LA FALLA:
- Título del AFA: {title}
- Área / Sistema: {area}
- Equipo / Componente / Tag: {equipment}
- Líder del AFA: {leader or 'Especialista en Confiabilidad'}
- Participantes: {participants or 'Equipo Multidisciplinario de Mantenimiento'}
- Descripción Bruta del Modo de Falla y Síntomas: {description}
{attachment_section}

REGLAS OBLIGATORIAS DE INGENIERÍA PARA EL AFA (MAN-F-054):
1. DESGLOSE 5W + 2H FORMAL Y TÉCNICO:
   - Problema Enfocado / Modo de Falla: Descripción técnica formal del modo de falla principal.
   - ¿Qué?: Síntoma técnico y desviación respecto a la condición nominal.
   - ¿Cómo?: Mecanismo de propagación de la falla en el sistema.
   - ¿Quién?: Quién detectó el fallo y contexto de operación.
   - ¿Cuánto?: Impacto en disponibilidad, OEE y seguridad.
   - ¿Cuál?: Componentes, partes y materiales involucrados.
   - ¿Dónde?: Ubicación exacta del componente fallido.
   - ¿Cuándo?: Patrón temporal y condiciones de carga.
   - Acción Inmediata: Medida correctiva de contención inicial.

2. ÁRBOL DE LOS 5 PORQUÉS COMPLETO Y PROFUNDO (5 NIVELES OBLIGATORIOS).
3. DETERMINACIÓN DE MODO DE FALLA, EFECTO, CONSECUENCIA Y PLANES DE ACCIÓN.

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "participantes": "Líder y participantes del AFA",
    "problema_enfocado": "Descripción formal del modo de falla enfocado bajo estándar MAN-F-054",
    "que_paso": "Análisis formal del qué sucedió y desviación técnica",
    "como_ocurrio": "Análisis del cómo se propagó el modo de falla",
    "quien_detecto": "Contexto de detección del fallo",
    "cuanto_perdida": "Impacto y consecuencia en la producción",
    "cual_material": "Componentes y partes críticas afectadas",
    "where_located": "Ubicación técnica precisa del componente",
    "when_started": "Momento de inicio de la degradación",
    "accion_inmediata": "Acción inmediata de contención ejecutada",
    "modo_falla": "Descripción técnica formal del Modo de Falla",
    "effect": "Efecto local y sistémico en la producción",
    "consequence": "Consecuencia en seguridad y costos",
    "porque1": "Por qué 1: Causa física directa del modo de falla",
    "porque2": "Por qué 2: Mecanismo de esfuerzo o condición anómala",
    "porque3": "Por qué 3: Condición latente en el sistema",
    "porque4": "Por qué 4: Brecha en la estrategia predictiva/preventiva",
    "porque5": "Por qué 5 (Causa Raíz Sistémica): Deficiencia estructural en la gestión de activos o diseño",
    "causa_fisica": "Descripción formal de la causa física de la falla",
    "causa_contribuyente": "Factores operacionales contribuyentes",
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
            "accion": "Acción correctiva sobre el componente",
            "objetivo": "Restaurar integridad técnica",
            "responsable": "Mantenimiento Mecánico",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva (Actualización RCM / Pauta de Inspección)",
            "objetivo": "Prevenir recurrencia del modo de falla",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Acción sobre la Causa Raíz (Modificación o rediseño sistémico)",
            "objetivo": "Eliminar la causa raíz definitivamente",
            "responsable": "Jefatura de Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2027-01-30",
            "estado": "Pendiente",
            "tipo": "Causa Raíz"
        }}
    ]
}}
"""
