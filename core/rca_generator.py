from core.ai_engine import AIEngine
from core.prompt_builder import PromptBuilder
from db.sqlite_manager import SQLiteManager

class RCAGenerator:
    """Generador y gestor de Análisis de Causa Raíz (ACR)."""

    def __init__(self, db_manager: SQLiteManager, ai_engine: AIEngine):
        self.db = db_manager
        self.ai = ai_engine

    def process_acr(self, title: str, event_date: str, area: str, linea: str, equipment: str, criticality: str, description: str, leader: str, participants: str, username: str, attachments_text: str = "") -> int:
        event_query = """
            INSERT INTO events (title, event_date, area, linea, equipment, criticality, description, status, created_by)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'Abierto', ?)
        """
        event_id = self.db.execute_non_query(event_query, (title, event_date, area, linea, equipment, criticality, description, username))

        prompt = PromptBuilder.build_acr_prompt(title, area, equipment, description, leader, participants, attachments_text)
        ai_data = self.ai.generate_response(prompt)

        acr_query = """
            INSERT INTO acr (event_id, participants, leader, team_area, problem_definition, technical_description, what_happened, how_happened, who_detected, how_much_loss, which_materials, where_located, when_started, immediate_action, why_1, why_2, why_3, why_4, why_5, physical_cause, contributor_cause, root_cause)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.db.execute_non_query(acr_query, (
            event_id,
            ai_data.get("participantes", participants),
            leader,
            area,
            ai_data.get("problema_enfocado", description),
            description,
            ai_data.get("que_paso", description),
            ai_data.get("como_ocurrio", ""),
            ai_data.get("quien_detecto", ""),
            ai_data.get("cuanto_perdida", ""),
            ai_data.get("cual_material", ""),
            ai_data.get("donde_nacimiento", ""),
            ai_data.get("cuando_inicio", ""),
            ai_data.get("accion_inmediata", ""),
            ai_data.get("porque1", ""),
            ai_data.get("porque2", ""),
            ai_data.get("porque3", ""),
            ai_data.get("porque4", ""),
            ai_data.get("porque5", ""),
            ai_data.get("causa_fisica", ""),
            ai_data.get("causa_contribuyente", ""),
            ai_data.get("causa_raiz", "")
        ))

        acciones = ai_data.get("acciones", [])
        for act in acciones:
            action_query = """
                INSERT INTO actions (event_id, action_text, objective, responsible, priority, due_date, status, action_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            self.db.execute_non_query(action_query, (
                event_id,
                act.get("accion", ""),
                act.get("objetivo", ""),
                act.get("responsable", ""),
                act.get("prioridad", "Alta"),
                act.get("fecha", "2026-12-31"),
                act.get("estado", "Pendiente"),
                act.get("tipo", "Correctiva")
            ))

        self.db.log_audit(username, "CREAR_ACR", f"Se creó el ACR para el evento ID {event_id}: {title}")
        return event_id
