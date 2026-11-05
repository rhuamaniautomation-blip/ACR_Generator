import sqlite3
import os
import logging
from typing import List, Dict, Any, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "database.db")
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database", "schema.sql")

class SQLiteManager:
    """Gestor robusto de base de datos SQLite para la plataforma ACR & AFA."""
    
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        db_dir = os.path.dirname(self.db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)
        self.init_db()

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def init_db(self) -> None:
        try:
            recreate = False
            # Verificamos si el archivo de base de datos ya existe para chequear su estructura
            if os.path.exists(self.db_path):
                conn = self.get_connection()
                cursor = conn.cursor()
                try:
                    cursor.execute("PRAGMA table_info(acr);")
                    columns = [col[1] for col in cursor.fetchall()]
                    # Si la tabla existe pero le falta la columna 'leader', forzamos recreación
                    if not columns or "leader" not in columns:
                        recreate = True
                except Exception:
                    recreate = True
                finally:
                
                    conn.close()

            if recreate and os.path.exists(self.db_path):
                os.remove(self.db_path)
                logger.warning("Base de datos obsoleta eliminada. Se recreará con el nuevo esquema.")

            # Ejecutar el esquema oficial
            if os.path.exists(SCHEMA_PATH):
                with open(SCHEMA_PATH, "r", encoding="utf-8") as sf:
                    schema_script = sf.read()
                conn = self.get_connection()
                conn.executescript(schema_script)
                conn.commit()
                conn.close()
                logger.info("Base de datos inicializada correctamente.")
        except Exception as e:
            logger.error(f"Error al inicializar la base de datos: {e}")
            raise

    def execute_query(self, query: str, params: tuple = ()) -> List[sqlite3.Row]:
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            conn.close()
            return rows
        except Exception as e:
            logger.error(f"Error en execute_query: {e}")
            return []

    def execute_non_query(self, query: str, params: tuple = ()) -> int:
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            last_id = cursor.lastrowid
            conn.close()
            return last_id
        except Exception as e:
            logger.error(f"Error en execute_non_query: {e}")
            raise

    def log_audit(self, username: str, action: str, details: str) -> None:
        query = "INSERT INTO audit_logs (username, action, details) VALUES (?, ?, ?)"
        try:
            self.execute_non_query(query, (username, action, details))
        except Exception as e:
            logger.error(f"Error al registrar auditoría: {e}")
