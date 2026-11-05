class PromptBuilder:
    """Constructor especializado de prompts industriales bajo formato MAN-F-054 y análisis riguroso de 5 Porqués."""

    @staticmethod
    def build_acr_prompt(title: str, area: str, equipment: str, description: str) -> str:
        return f"""
Actúa como un equipo multidisciplinario experto compuesto por: Especialista RCA, Especialista ACR, Especialista AFA, Ingeniero Mecánico Senior, Ingeniero Eléctrico Senior, Ingeniero de Automatización y Reliability Engineer.
Analiza el siguiente evento industrial y genera un Análisis de Causa Raíz (ACR) riguroso bajo el estándar MAN-F-054 y metodologías Lean Manufacturing, Six Sigma y gestión de confiabilidad industrial.

INFORMACIÓN DEL EVENTO:
- Título: {title}
- Área: {area}
- Equipo: {equipment}
- Descripción del Evento: {description}

REGLAS ESTRICTAS PARA LOS 5 PORQUÉS Y CAUSAS:
1. No repetir información entre niveles.
2. No terminar el análisis en "error humano" o "falta de capacitación" (buscar la causa sistémica o de diseño organizacional/técnico).
3. Llegar obligatoriamente a una causa raíz sistémica profunda y a una causa física controlable.
4. Definir claramente el problema enfocado bajo 5W+2H (Qué, Cómo, Quién, Cuánto, Cuál, Dónde, Cuándo).

DEBES RESPONDER EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "problema": "Definición técnica y detallada del problema (5W+2H: Qué pasó, Cómo ocurrió, Dónde, Cuándo, etc.)",
    "porque1": "Porque 1: Causa directa física o inmediata del problema",
    "porque2": "Porque 2: Mecanismo o condición que permitió el Porque 1",
    "porque3": "Porque 3: Deficiencia técnica o fallo en el estándar operativo",
    "porque4": "Porque 4: Ausencia de control o brecha en el sistema de gestión",
    "porque5": "Porque 5 (Causa Raíz Sistémica): Deficiencia organizacional, de diseño o en las políticas de mantenimiento RCM",
    "causa_fisica": "Descripción detallada de la causa física de la falla",
    "causa_contribuyente": "Descripción de los factores contribuyentes o ambientales",
    "causa_raiz": "Causa raíz fundamental identificada",
    "acciones": [
        {{
            "accion": "Acción inmediata de contención o corrección",
            "objetivo": "Restaurar operación segura inmediata",
            "responsable": "Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva sobre el componente afectado",
            "objetivo": "Reparar o reemplazar componente dañado",
            "responsable": "Mantenimiento Mecánico",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva basada en RCM",
            "objetivo": "Prevenir recurrencia futura",
            "responsable": "Planeamiento",
            "prioridad": "Media",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Acción sobre la Causa Raíz (actualización de procedimientos, LUP o diseño)",
            "objetivo": "Eliminación sistémica del problema",
            "responsable": "Ingeniería de Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-30",
            "estado": "Pendiente",
            "tipo": "Causa Raíz"
        }}
    ]
}}
"""

    @staticmethod
    def build_afa_prompt(title: str, area: str, equipment: str, description: str) -> str:
        return f"""
Actúa como un Especialista en FMEA/AFA y Reliability Engineer.
Analiza la siguiente falla industrial y genera un reporte FMEA/AFA completo y riguroso bajo el estándar MAN-F-054.

INFORMACIÓN:
- Título: {title}
- Área: {area}
- Equipo: {equipment}
- Descripción: {description}

REGLAS ESTRICTAS PARA LOS 5 PORQUÉS DEL AFA:
1. No repetir información entre niveles.
2. Llegar a la causa raíz sistémica y modo de falla detallado.

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "modo_falla": "Descripción técnica del modo de falla",
    "efecto": "Efecto local y sistémico del modo de falla",
    "consecuencia": "Consecuencia operativa, de seguridad y económica",
    "porque1": "Porque 1: Causa directa del modo de falla",
    "porque2": "Porque 2: Mecanismo intermedio",
    "porque3": "Porque 3: Condición latente",
    "porque4": "Porque 4: Brecha en estándares",
    "porque5": "Porque 5 (Causa Raíz): Deficiencia sistémica de gestión o diseño",
    "causa_raiz": "Causa raíz fundamental identificada",
    "acciones": [
        {{
            "accion": "Acción inmediata de contención",
            "objetivo": "Mitigar efecto inmediato",
            "responsable": "Operaciones",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva sobre componentes",
            "objetivo": "Restaurar integridad",
            "responsable": "Mantenimiento",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva y sobre Causa Raíz (LUP / RCM)",
            "objetivo": "Evitar recurrencia sistémica",
            "responsable": "Confiabilidad",
            "prioridad": "Alta",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Causa Raíz"
        }}
    ]
}}
"""
