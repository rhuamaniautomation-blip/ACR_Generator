class PromptBuilder:
    """Constructor especializado de prompts industriales bajo estándar MAN-F-054 e ingeniería de confiabilidad."""

    @staticmethod
    def build_acr_prompt(title: str, area: str, equipment: str, description: str, attachments_text: str = "") -> str:
        attachment_section = f"\nEVIDENCIAS Y DOCUMENTOS ADJUNTOS ANALIZADOS:\n{attachments_text}\n" if attachments_text else ""
        return f"""
Actúa como un equipo multidisciplinario senior compuesto por: Especialista RCA, Especialista ACR, Especialista AFA, Ingeniero Mecánico Senior, Ingeniero Eléctrico, Ingeniero de Automatización y Reliability Engineer.
Analiza el siguiente evento industrial y genera un Análisis de Causa Raíz (ACR) exhaustivo, técnico y de nivel de ingeniería bajo el estándar MAN-F-054.

INFORMACIÓN DEL EVENTO:
- Título: {title}
- Área: {area}
- Equipo/Tag: {equipment}
- Descripción del Evento: {description}
{attachment_section}

REGLAS OBLIGATORIAS PARA EL ANÁLISIS DE INGENIERÍA Y LOS 5 PORQUÉS:
1. Debes completar OBLIGATORIAMENTE los 5 niveles del árbol de los 5 Porqués (porque1, porque2, porque3, porque4, porque5).
2. Cada porqué debe ser un análisis técnico profundo. No repetir información ni omitir ningún nivel.
3. Prohibido concluir en "error humano", "descuido" o "falta de capacitación". Se debe profundizar hasta la causa raíz sistémica, organizacional, de diseño o de estrategia de mantenimiento (RCM).
4. El desglose 5W+2H debe completar técnicamente:
   - ¿Qué ocurrió?
   - ¿Cómo ocurrió?
   - ¿Quién detectó el problema?
   - ¿Cuánto (frecuencia, pérdida económica o de OEE)?
   - ¿Cuál (materiales, repuestos o componentes afectados)?
   - ¿Dónde nació la falla exactamente?
   - ¿Cuándo inició?

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "problema": "Definición técnica enfocado bajo 5W+2H",
    "que_paso": "Descripción detallada de qué se observó o falló",
    "como_ocurrio": "Análisis del mecanismo de falla y propagación",
    "quien_detecto": "Rol o sistema que detectó el evento",
    "cuanto_perdida": "Estimación técnica de la pérdida (horas de parada, costo o impacto en OEE)",
    "cual_material": "Especificación de componentes, modelos o materiales afectados",
    "donde_nacimiento": "Ubicación técnica exacta donde se originó la falla",
    "cuando_inicio": "Línea temporal de inicio y evolución",
    "porque1": "Por qué 1: Causa física o inmediata directa",
    "porque2": "Por qué 2: Mecanismo técnico o condición operacional que la originó",
    "porque3": "Por qué 3: Deficiencia en el estándar, ajuste o inspección previa",
    "porque4": "Por qué 4: Brecha en las políticas de mantenimiento o control de calidad",
    "porque5": "Por qué 5: Causa raíz sistémica, organizacional o de ingeniería de confiabilidad",
    "causa_fisica": "Descripción del modo físico de degradación o rotura",
    "causa_contribuyente": "Factores ambientales, operacionales o de contexto",
    "causa_raiz": "Causa raíz sistémica fundamental",
    "acciones": [
        {{
            "accion": "Acción inmediata de contención o corrección",
            "objetivo": "Asegurar la contención del problema",
            "responsable": "Mantenimiento / Operaciones",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva sobre componentes dañados",
            "objetivo": "Restaurar condición nominal",
            "responsable": "Mantenimiento Mecánico",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva basada en RCM / LUP",
            "objetivo": "Prevenir recurrencia periódica",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Media",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Acción sobre la Causa Raíz (Rediseño, LUP o Estándar)",
            "objetivo": "Eliminar la causa sistémica",
            "responsable": "Jefatura de Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2027-01-30",
            "estado": "Pendiente",
            "tipo": "Causa Raíz"
        }}
    ]
}}
"""

    @staticmethod
    def build_afa_prompt(title: str, area: str, equipment: str, description: str, attachments_text: str = "") -> str:
        attachment_section = f"\nEVIDENCIAS Y DOCUMENTOS ADJUNTOS ANALIZADOS:\n{attachments_text}\n" if attachments_text else ""
        return f"""
Actúa como un Especialista Senior en FMEA/AFA y Reliability Engineer.
Analiza la siguiente falla industrial y genera un Análisis de Falla (AFA / FMEA) exhaustivo de carácter de ingeniería bajo el estándar MAN-F-054.

INFORMACIÓN DE LA FALLA:
- Título: {title}
- Área: {area}
- Equipo/Componente: {equipment}
- Descripción del Modo de Falla y Síntomas: {description}
{attachment_section}

REGLAS OBLIGATORIAS PARA EL AFA Y LOS 5 PORQUÉS:
1. DEBES COMPLETAR OBLIGATORIAMENTE LOS 5 PORQUÉS SIN EXCEPCIÓN (porque1, porque2, porque3, porque4, porque5).
2. Cada nivel debe contener un análisis de ingeniería riguroso y diferenciado. Prohibido dejar campos vacíos o duplicar texto.
3. Profundizar hasta encontrar la causa raíz sistémica y de diseño/gestión de activos.
4. Definir con precisión el Modo de Falla, el Efecto local/sistémico y la Consecuencia operativa/económica.

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "modo_falla": "Descripción técnica detallada del modo de falla",
    "efecto": "Efecto detallado en el equipo, subsistema y proceso",
    "consecuencia": "Consecuencia en seguridad, impacto ambiental, OEE y costos",
    "porque1": "Por qué 1: Causa directa o manifestación física del modo de falla",
    "porque2": "Por qué 2: Mecanismo intermedio de falla o esfuerzo no controlado",
    "porque3": "Por qué 3: Condición latente o degradación del estándar",
    "porque4": "Por qué 4: Deficiencia en las pautas de inspección o mantenimiento predictivo",
    "porque5": "Por qué 5 (Causa Raíz): Deficiencia sistémica de gestión de activos, diseño o estrategia de confiabilidad",
    "causa_raiz": "Causa raíz fundamental identificada",
    "acciones": [
        {{
            "accion": "Acción inmediata de contención",
            "objetivo": "Mitigar impacto operativo",
            "responsable": "Operaciones",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva técnica sobre el activo",
            "objetivo": "Restaurar la confiabilidad del componente",
            "responsable": "Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva (Creación de LUP / Actualización de Plan RCM)",
            "objetivo": "Evitar la recurrencia del modo de falla",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Causa Raíz"
        }}
    ]
}}
"""
