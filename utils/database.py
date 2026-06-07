import sqlite3

def init_db():
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_name TEXT,
        score REAL,
        ats INTEGER,
        recommendation TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_result(name, score, ats, rec):
    conn = sqlite3.connect("resumes.db")
    c = conn.cursor()

    c.execute("""
    INSERT INTO results (resume_name, score, ats, recommendation)
    VALUES (?, ?, ?, ?)
    """, (name, score, ats, rec))

    conn.commit()
    conn.close()