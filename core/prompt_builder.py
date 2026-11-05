class PromptBuilder:
    """Constructor especializado de prompts industriales."""

    @staticmethod
    def build_acr_prompt(title: str, area: str, equipment: str, description: str) -> str:
        return f"""
Actúa como un equipo multidisciplinario experto compuesto por: Especialista RCA, Especialista ACR, Especialista AFA, Ingeniero Mecánico Senior, Ingeniero Eléctrico Senior, Ingeniero de Automatización y Reliability Engineer.
Analiza el siguiente evento industrial y genera un Análisis de Causa Raíz (ACR) riguroso bajo metodologías Lean Manufacturing, Six Sigma y gestión de confiabilidad industrial.

INFORMACIÓN DEL EVENTO:
- Título: {title}
- Área: {area}
- Equipo: {equipment}
- Descripción del Evento: {description}

REGLAS ESTRICTAS PARA LOS 5 PORQUÉS:
1. No repetir información entre niveles.
2. No terminar el análisis en "error humano" o "falta de capacitación" (buscar la causa sistémica o de diseño organizacional/técnico).
3. Llegar obligatoriamente a una causa raíz sistémica y a una causa física controlable.
4. Identificar claramente la Causa Física, la Causa Contribuyente y la Causa Raíz.

DEBES RESPONDER EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO CON LA SIGUIENTE ESTRUCTURA EXACTA:
{{
    "problema": "Definición clara y técnica del problema enfocado (5W+2H)",
    "porque1": "Respuesta al primer porqué (nivel físico directo)",
    "porque2": "Respuesta al segundo porqué",
    "porque3": "Respuesta al tercer porqué",
    "porque4": "Respuesta al cuarto porqué",
    "porque5": "Respuesta al quinto porqué (causa raíz sistémica)",
    "causa_fisica": "Descripción detallada de la causa física de la falla",
    "causa_contribuyente": "Descripción de los factores contribuyentes o ambientales",
    "causa_raiz": "Causa raíz fundamental identificada",
    "acciones": [
        {{
            "accion": "Descripción clara de la acción de contención o correctiva",
            "objetivo": "Objetivo de la acción",
            "responsable": "Cargo o departamento",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Inmediata"
        }},
        {{
            "accion": "Acción correctiva sobre el componente afectado",
            "objetivo": "Restaurar condición original",
            "responsable": "Mantenimiento Mecánico",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Correctiva"
        }},
        {{
            "accion": "Acción preventiva basada en RCM",
            "objetivo": "Prevenir recurrencia",
            "responsable": "Planeamiento",
            "prioridad": "Media",
            "fecha": "2027-01-15",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }},
        {{
            "accion": "Modificación en procedimientos o diseño para eliminar causa raíz",
            "objetivo": "Eliminación sistémica",
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
Analiza la siguiente falla industrial y genera un reporte FMEA/AFA completo.

INFORMACIÓN:
- Título: {title}
- Área: {area}
- Equipo: {equipment}
- Descripción: {description}

RESPONDE EXCLUSIVAMENTE EN FORMATO JSON VÁLIDO:
{{
    "modo_falla": "Descripción técnica del modo de falla",
    "efecto": "Efecto local y en el sistema",
    "consecuencia": "Consecuencia operativa o económica",
    "porque1": "Primer porqué",
    "porque2": "Segundo porqué",
    "porque3": "Tercer porqué",
    "porque4": "Cuarto porqué",
    "porque5": "Quinto porqué (Causa Raíz)",
    "causa_raiz": "Causa raíz identificada",
    "acciones": [
        {{
            "accion": "Acción de mitigación",
            "objetivo": "Reducir RPN",
            "responsable": "Ingeniería",
            "prioridad": "Alta",
            "fecha": "2026-12-31",
            "estado": "Pendiente",
            "tipo": "Preventiva"
        }}
    ]
}}
"""

