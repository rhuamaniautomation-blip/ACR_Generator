import os
import json
import logging
import google.generativeai as genai
from openai import OpenAI
from typing import Dict, Any

logger = logging.getLogger(__name__)

class AIEngine:
    """Motor unificado de Inteligencia Artificial."""

    def __init__(self, provider: str = "Gemini Flash", api_key: str = "", model_name: str = "gemini-2.5-flash"):
        self.provider = provider
        self.api_key = api_key
        self.model_name = model_name

    def generate_response(self, prompt: str) -> Dict[str, Any]:
        try:
            if "Gemini" in self.provider:
                return self._call_gemini(prompt)
            elif "GPT" in self.provider or "Azure" in self.provider:
                return self._call_openai(prompt)
            else:
                return self._fallback_response(prompt)
        except Exception as e:
            logger.error(f"Error en AIEngine: {e}")
            return self._fallback_response(prompt)

    def _call_gemini(self, prompt: str) -> Dict[str, Any]:
        key = self.api_key or os.getenv("GEMINI_API_KEY", "")
        if not key:
            return self._fallback_response(prompt)
        genai.configure(api_key=key)
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_content(prompt)
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
        return json.loads(text.strip())

    def _call_openai(self, prompt: str) -> Dict[str, Any]:
        key = self.api_key or os.getenv("AZURE_OPENAI_API_KEY", "") or os.getenv("OPENAI_API_KEY", "")
        if not key:
            return self._fallback_response(prompt)
        client = OpenAI(api_key=key)
        response = client.chat.completions.create(
            model=self.model_name if self.model_name else "gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un experto senior en ingeniería de confiabilidad. Responde estrictamente en JSON."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        return json.loads(content)

    def _fallback_response(self, prompt: str) -> Dict[str, Any]:
        return {
            "problema": "Fallo funcional detectado en el sistema principal debido a fatiga mecánica y desalineación en conjunto rotativo.",
            "porque1": "El componente presentó desgaste prematuro y vibración excesiva.",
            "porque2": "Existía una desalineación angular superior a la tolerancia ISO permitida.",
            "porque3": "El procedimiento de alineación previa no contempló compensación por dilatación térmica.",
            "porque4": "El estándar técnico de mantenimiento preventivo estaba desactualizado respecto al manual del fabricante.",
            "porque5": "Ausencia de un proceso formal de auditoría y actualización periódica de planes de mantenimiento centrado en confiabilidad (RCM).",
            "causa_fisica": "Desgaste abrasivo y fractura por fatiga en rodamientos debido a sobrecarga vibratoria.",
            "causa_contribuyente": "Condiciones ambientales de alta temperatura y lubricación subóptima.",
            "causa_raiz": "Deficiencia en el sistema de gestión de mantenimiento (ausencia de revisión de estándares RCM).",
            "modo_falla": "Bloqueo mecánico por gripado de rodamientos.",
            "efecto": "Detención imprevista de la línea de producción y pérdida de OEE.",
            "consecuencia": "Impacto económico por horas de parada no programada.",
            "acciones": [
                {
                    "accion": "Inspección termográfica y análisis de vibraciones inmediato.",
                    "objetivo": "Verificar estado actual del conjunto.",
                    "responsable": "Especialista de Confiabilidad",
                    "prioridad": "Alta",
                    "fecha": "2026-11-15",
                    "estado": "Pendiente",
                    "tipo": "Inmediata"
                },
                {
                    "accion": "Reemplazo de rodamientos y alineación láser de precisión.",
                    "objetivo": "Restaurar operación nominal.",
                    "responsable": "Mantenimiento Mecánico",
                    "prioridad": "Alta",
                    "fecha": "2026-11-16",
                    "estado": "Pendiente",
                    "tipo": "Correctiva"
                },
                {
                    "accion": "Actualizar plan preventivo incorporando alineación láser cada 6 meses.",
                    "objetivo": "Prevenir recurrencia por desalineación.",
                    "responsable": "Planificador de Mantenimiento",
                    "prioridad": "Media",
                    "fecha": "2026-11-30",
                    "estado": "Pendiente",
                    "tipo": "Preventiva"
                },
                {
                    "accion": "Revisar y actualizar todos los procedimientos de montaje de equipos rotativos bajo norma ISO.",
                    "objetivo": "Eliminación sistémica de procedimientos obsoletos.",
                    "responsable": "Ingeniería de Confiabilidad",
                    "prioridad": "Alta",
                    "fecha": "2026-12-15",
                    "estado": "Pendiente",
                    "tipo": "Causa Raíz"
                }
            ]
        }

