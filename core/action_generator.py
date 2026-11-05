from db.sqlite_manager import SQLiteManager

class ActionManager:
    """Gestor de planes de acción."""

    def __init__(self, db_manager: SQLiteManager):
        self.db = db_manager

    def update_action_status(self, action_id: int, status: str, username: str) -> None:
        query = "UPDATE actions SET status = ? WHERE id = ?"
        self.db.execute_non_query(query, (status, action_id))
        self.db.log_audit(username, "ACTUALIZAR_ACCION", f"Se actualizó estado de acción ID {action_id} a '{status}'")

