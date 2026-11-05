PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    full_name TEXT NOT NULL,
    role TEXT CHECK(role IN ('Administrador', 'Investigador', 'Supervisor', 'Consulta')) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

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

CREATE TABLE IF NOT EXISTS acr (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
    problem_definition TEXT,
    technical_description TEXT,
    what_happened TEXT,
    how_happened TEXT,
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

CREATE TABLE IF NOT EXISTS afa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
    failure_mode TEXT,
    effect TEXT,
    consequence TEXT,
    why_1 TEXT,
    why_2 TEXT,
    why_3 TEXT,
    why_4 TEXT,
    why_5 TEXT,
    root_cause TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

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

CREATE TABLE IF NOT EXISTS audit_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    action TEXT NOT NULL,
    details TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT OR IGNORE INTO users (id, username, password_hash, full_name, role) 
VALUES (1, 'admin', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW', 'Administrador General', 'Administrador');

