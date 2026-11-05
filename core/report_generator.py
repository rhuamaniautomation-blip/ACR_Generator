from db.sqlite_manager import SQLiteManager

class ReportGenerator:
    """Generador central de reportes."""

    def __init__(self, db_manager: SQLiteManager):
        self.db = db_manager

    def get_event_data(self, event_id: int):
        event = self.db.execute_query("SELECT * FROM events WHERE id = ?", (event_id,))
        acr = self.db.execute_query("SELECT * FROM acr WHERE event_id = ?", (event_id,))
        afa = self.db.execute_query("SELECT * FROM afa WHERE event_id = ?", (event_id,))
        actions = self.db.execute_query("SELECT * FROM actions WHERE event_id = ?", (event_id,))
        return {
            "event": dict(event[0]) if event else {},
            "acr": dict(acr[0]) if acr else {},
            "afa": dict(afa[0]) if afa else {},
            "actions": [dict(a) for a in actions]
        }

