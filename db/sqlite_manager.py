import sqlite3
import os
import logging
from typing import List, Dict, Any, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "database.db")
SCHEMA_PATH = os.path.join(BASE_DIR, "database", "schema.sql")

class SQLiteManager:
    """Gestor robusto de base de datos SQLite con migración en caliente para Streamlit Cloud."""
    
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        db_dir = os.path.dirname(self.db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)
        self.init_db()

    def get_connection(self) -> sqlite3.Connection:
        # Timeout de 30 segundos para evitar bloqueos concurrentes en Streamlit Cloud
        conn = sqlite3.connect(self.db_path, timeout=30.0)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def init_db(self) -> None:
        try:
            db_dir = os.path.dirname(self.db_path)
            if db_dir and not os.path.exists(db_dir):
                os.makedirs(db_dir, exist_ok=True)

            conn = self.get_connection()
            cursor = conn.cursor()

            # 1. Crear tablas base si no existen
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    full_name TEXT NOT NULL,
                    role TEXT CHECK(role IN ('Administrador', 'Investigador', 'Supervisor', 'Consulta')) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    event_date TEXT NOT NULL,
                    area TEXT NOT NULL,
                    linea TEXT NOT NULL,
                    equipment TEXT NOT NULL,
                    criticality TEXT CHECK(criticality IN ('Alta', 'Media', 'Baja')) NOT NULL,
                    description TEXT NOT NULL,
                    status TEXT DEFAULT 'Abierto',
                    created_by TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS acr (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
                    participants TEXT,
                    leader TEXT,
                    team_area TEXT,
                    problem_definition TEXT,
                    technical_description TEXT,
                    what_happened TEXT,
                    how_happened TEXT,
                    who_detected TEXT,
                    how_much_loss TEXT,
                    which_materials TEXT,
                    where_located TEXT,
                    when_started TEXT,
                    immediate_action TEXT,
                    why_1 TEXT,
                    why_2 TEXT,
                    why_3 TEXT,
                    why_4 TEXT,
                    why_5 TEXT,
                    physical_cause TEXT,
                    contributor_cause TEXT,
                    root_cause TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS afa (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
                    participants TEXT,
                    leader TEXT,
                    team_area TEXT,
                    problem_definition TEXT,
                    technical_description TEXT,
                    what_happened TEXT,
                    how_happened TEXT,
                    who_detected TEXT,
                    how_much_loss TEXT,
                    which_materials TEXT,
                    where_located TEXT,
                    when_started TEXT,
                    immediate_action TEXT,
                    failure_mode TEXT,
                    effect TEXT,
                    consequence TEXT,
                    why_1 TEXT,
                    why_2 TEXT,
                    why_3 TEXT,
                    why_4 TEXT,
                    why_5 TEXT,
                    physical_cause TEXT,
                    contributor_cause TEXT,
                    root_cause TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS actions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
                    action_text TEXT NOT NULL,
                    objective TEXT NOT NULL,
                    responsible TEXT NOT NULL,
                    priority TEXT CHECK(priority IN ('Alta', 'Media', 'Baja')) NOT NULL,
                    due_date TEXT NOT NULL,
                    status TEXT CHECK(status IN ('Pendiente', 'En Progreso', 'Completada', 'Vencida')) DEFAULT 'Pendiente',
                    action_type TEXT CHECK(action_type IN ('Inmediata', 'Correctiva', 'Preventiva', 'Causa Raíz')) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    action TEXT NOT NULL,
                    details TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            # 2. Insertar usuario administrador por defecto si no existe
            cursor.execute("""
                INSERT OR IGNORE INTO users (id, username, password_hash, full_name, role) 
                VALUES (1, 'admin', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW', 'Administrador General', 'Administrador');
            """)

            conn.commit()
            conn.close()
            logger.info("Base de datos inicializada y verificada correctamente.")

        except Exception as e:
            logger.error(f"Error crítico al inicializar la base de datos: {e}")
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
