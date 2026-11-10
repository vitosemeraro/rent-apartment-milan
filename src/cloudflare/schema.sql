-- Registro eventi anonimo del sito (sostituisce i CSV in ~/ram-events su Netsons)
CREATE TABLE IF NOT EXISTS events (ts TEXT NOT NULL, e TEXT NOT NULL, p TEXT NOT NULL, l TEXT, s TEXT, v INTEGER DEFAULT 0);
CREATE INDEX IF NOT EXISTS events_ts ON events (ts);
