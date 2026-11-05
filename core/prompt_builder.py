class PromptBuilder:
    """Constructor especializado de prompts industriales de nivel de ingeniería bajo estándar MAN-F-054."""

    @staticmethod
    def build_acr_prompt(title: str, area: str, equipment: str, description: str, leader: str = "", participants: str = "", attachments_text: str = "") -> str:
        attachment_section = f"\nEVIDENCIAS Y DOCUMENTOS ADJUNTOS ANALIZADOS:\n{attachments_text}\n" if attachments_text else ""
        return f"""
Actúa como un equipo multidisciplinario senior de Ingeniería de Confiabilidad y Mantenimiento Industrial compuesto por: Especialista RCA/ACR Senior, Ingeniero Mecánico, Ingeniero Eléctrico, Ingeniero de Automatización y Reliability Engineer.
Analiza el siguiente evento industrial y genera un Análisis de Causa Raíz (ACR) completo, técnico y profundo según el Estándar Oficial MAN-F-054.

INFORMACIÓN GENERAL DEL EVENTO:
- Título del Evento: {title}
- Área / Sistema: {area}
- Equipo / Tag: {equipment}
- Líder del Análisis: {leader or 'Ingeniero de Confiabilidad'}
- Participantes: {participants or 'Equipo de Mantenimiento y Operaciones'}
- Descripción Inicial del Problema: {description}
{attachment_section}

REGLAS OBLIGATORIAS DE INGENIERÍA PARA COMPLETA EL ESTÁNDAR MAN-F-054:
1. DESGLOSE 5W + 2H OBLIGATORIO:
   - ¿Qué?: Qué se observó, qué tarea falló y qué debió haber pasado nominalmente.
   - ¿Cómo?: Mecanismo físico de la falla, cómo ocurría el problema y cómo se ejecutó el trabajo.
   - ¿Quién?: Quién originó, quién detectó y a quién no le afectó.
   - ¿Cuánto?: Frecuencia del evento, extensión del daño y estimación de pérdidas (horas de parada, OEE o costo).
   - ¿Cuál?: Marcas, modelos, formatos, componentes y materiales intermedios/finales involucrados.
   - ¿Dónde?: Punto técnico exacto donde nace la falla.
   - ¿Cuándo?: Fecha/hora de inicio y patrón de ocurrencia.

2. ÁRBOL DE LOS 5 PORQUÉS RIGUROSO (MÍNIMO Y OBLIGATORIO 5 NIVELES):
   - Cada Porqué debe ser un análisis técnico avanzado de ingeniería. Prohibido usar respuestas simples de una frase o superficiales.
   - Prohibido atribuir la causa raíz a "error humano", "falta de atención" o "falta de capacitación". Debes profundizar hasta llegar a la falla sistémica de gestión de activos, deficiencia en estándares RCM, errores de diseño o procedimientos defectuosos.
   - Nivel 1: Causa física inmediata.
   - Nivel 2: Mecanismo técnico o condición operacional facilitadora.
   - Nivel 3: Deficiencia en el estándar operativo, inspección o mantenimiento.
   - Nivel 4: Brecha en el sistema de gestión, control de calidad o proveedores.
   - Nivel 5: Causa Raíz Sistémica Organizacional / Estrategia de Confiabilidad.

3. ACCIONES Y PLANES DE SEGUIMIENTO (CORRECTIVAS, PREVENTIVAS Y CAUSA RAÍZ):
   - Definir acción inmediata de contención.
   - Definir acciones específicas asignando objetivo, responsable por cargo, prioridad (Alta/Media/Baja), fecha tentativa y tipo.

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "participantes": "Líder y lista de participantes técnicos",
    "problema_enfocado": "Descripción enfocada del problema bajo estándar MAN-F-054",
    "que_paso": "Análisis del QUÉ: Qué se vio, tarea que falló y qué debió pasar",
    "como_ocurrio": "Análisis del CÓMO: Mecanismo de ocurrencia y ejecución del trabajo",
    "quien_detecto": "Análisis del QUIÉN: Quién detectó, quién originó y a quién no le pasó",
    "cuanto_perdida": "Análisis del CUÁNTO: Frecuencia de ocurrencia, horas de parada e impacto económico",
    "cual_material": "Análisis del CUÁL: Componentes, marcas, formatos y materiales afectados",
    "donde_nacimiento": "Análisis del DÓNDE: Punto exacto donde nace el problema",
    "cuando_inicio": "Análisis del CUÁNDO: Momento exacto de inicio y condición temporal",
    "accion_inmediata": "Acción inmediata de contención o corrección ejecutada",
    "porque1": "Por qué 1: Causa directa física o manifestación visible inmediata",
    "porque2": "Por qué 2: Mecanismo técnico y condición física/operativa subyacente",
    "porque3": "Por qué 3: Deficiencia en el estándar de mantenimiento, ajuste o inspección",
    "porque4": "Por qué 4: Ausencia de control de calidad o brecha en la política de activos",
    "porque5": "Por qué 5 (Causa Raíz Sistémica): Deficiencia organizacional, de diseño o de estrategia RCM",
    "causa_fisica": "Descripción detallada de la causa física directa de la falla",
    "causa_contribuyente": "Factores de entorno, operacionales o de contexto contribuyente",
    "causa_raiz": "Causa raíz sistémica fundamental identificada",
    "acciones": [
        {{
            "accion": "Acción de contención inmediata o corrección",
            "objetivo": "Restaurar operación nominal o contener el evento",
            "responsable": "Mantenimiento Mecánico / Operaciones",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva técnica sobre el activo",
            "objetivo": "Restaurar condición original de los componentes",
            "responsable": "Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva basada en RCM (LUP o Pauta de Inspección)",
            "objetivo": "Estandarizar inspecciones y prevenir recurrencia",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Acción sobre la Causa Raíz (Rediseño, Calibración o Modificación del Sistema)",
            "objetivo": "Eliminar sistémicamente el modo de falla",
            "responsable": "Jefatura de Mantenimiento / Ingeniería",
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
Analiza la siguiente falla industrial y genera un Análisis de Falla (AFA / FMEA) completo y riguroso de nivel de ingeniería bajo el estándar MAN-F-054.

INFORMACIÓN GENERAL DE LA FALLA:
- Título del AFA: {title}
- Área / Sistema: {area}
- Equipo / Componente / Tag: {equipment}
- Líder del AFA: {leader or 'Especialista en Confiabilidad'}
- Participantes: {participants or 'Equipo Multidisciplinario de Mantenimiento'}
- Descripción del Modo de Falla y Síntomas: {description}
{attachment_section}

REGLAS OBLIGATORIAS DE INGENIERÍA PARA COMPLETAR EL ESTÁNDAR MAN-F-054 Y EL AFA:
1. DESGLOSE COMPLETO 5W + 2H DEL MODO DE FALLA:
   - ¿Qué?: Qué se observó, modo de falla técnica y qué debió haber pasado.
   - ¿Cómo?: Mecanismo de degradación/falla y cómo se operaba/ejecutaba el trabajo.
   - ¿Quién?: Quién detectó el fallo y quién originó la condición.
   - ¿Cuánto?: Frecuencia, horas de indisponibilidad y consecuencia económica/OEE.
   - ¿Cuál?: Componente específico, repuesto, marcas, modelos y materiales afectados.
   - ¿Dónde?: Ubicación técnica exacta y punto de origen.
   - ¿Cuándo?: Cuándo inició el síntoma y patrón de falla.

2. ÁRBOL DE LOS 5 PORQUÉS COMPLETO (COMPLETAR OBLIGATORIAMENTE LOS 5 NIVELES):
   - Cada Porqué debe ser un análisis técnico detallado y profundo. Prohibido omitir niveles o colocar frases genéricas.
   - Profundizar hasta encontrar la causa raíz sistémica, fallas en la estrategia de mantenimiento predictivo/preventivo o problemas de diseño del activo.

3. DETERMINACIÓN DE MODO DE FALLA, EFECTO, CONSECUENCIA Y PLANES DE ACCIÓN.

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "participantes": "Líder y participantes del AFA",
    "problema_enfocado": "Descripción técnica del problema/modo de falla enfocado",
    "que_paso": "Análisis del QUÉ: Síntoma técnico, falla observada y condición deseada",
    "como_ocurrio": "Análisis del CÓMO: Mecanismo de propagación y operación del componente",
    "quien_detecto": "Análisis del QUIÉN: Quién detectó el modo de falla",
    "cuanto_perdida": "Análisis del CUÁNTO: Extensión del daño, tiempo de reparación e impacto OEE",
    "cual_material": "Análisis del CUÁL: Componentes específicos, piezas y materiales afectados",
    "donde_nacimiento": "Análisis del DÓNDE: Punto de origen físico de la falla",
    "cuando_inicio": "Análisis del CUÁNDO: Inicio de la degradación y condición temporal",
    "accion_inmediata": "Acción inmediata de contención ejecutada",
    "modo_falla": "Descripción técnica formal del Modo de Falla",
    "efecto": "Efecto local y en el sistema de producción",
    "consecuencia": "Consecuencia en seguridad, medio ambiente y costos",
    "porque1": "Por qué 1: Causa directa o manifestación física visible del modo de falla",
    "porque2": "Por qué 2: Mecanismo de degradación técnico o esfuerzo mecánico/eléctrico anómalo",
    "porque3": "Por qué 3: Condición latente o deficiencia en la pauta de inspección/mantenimiento",
    "porque4": "Por qué 4: Brecha en el plan preventivo/predictivo RCM o proveedores de piezas",
    "porque5": "Por qué 5 (Causa Raíz Sistémica): Deficiencia en la gestión de activos, diseño o ingeniería de planta",
    "causa_fisica": "Descripción del modo físico de falla de los materiales",
    "causa_contribuyente": "Factores de contexto y parámetros operacionales",
    "causa_raiz": "Causa raíz fundamental identificada",
    "acciones": [
        {{
            "accion": "Acción inmediata de contención del impacto",
            "objetivo": "Mitigar el riesgo operativo inmediato",
            "responsable": "Operaciones / Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva sobre componentes dañados",
            "objetivo": "Restaurar integridad técnica del activo",
            "responsable": "Mantenimiento Mecánico/Eléctrico",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva (LUP / Actualización de Plan RCM)",
            "objetivo": "Prevenir la recurrencia del modo de falla",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Acción sobre la Causa Raíz (Rediseño, Calibración o Modificación del Sistema)",
            "objetivo": "Eliminar sistémicamente la causa raíz",
            "responsable": "Jefatura de Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2027-01-30",
            "estado": "Pendiente",
            "tipo": "Causa Raíz"
        }}
    ]
}}
"""
