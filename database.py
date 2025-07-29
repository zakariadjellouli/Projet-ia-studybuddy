import sqlite3

def init_db():
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rappels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texte TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_rappel(texte, date):
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rappels (texte, date) VALUES (?, ?)", (texte, date))
    conn.commit()
    conn.close()

def get_rappels():
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("SELECT texte, date FROM rappels")
    rappels = cursor.fetchall()
    conn.close()
    return rappels

def init_events():
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evenements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            date TEXT NOT NULL,
            heure TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_event(titre, date, heure):
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO evenements (titre, date, heure) VALUES (?, ?, ?)", (titre, date, heure))
    conn.commit()
    conn.close()

def get_events():
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("SELECT titre, date, heure FROM evenements ORDER BY date, heure")
    events = cursor.fetchall()
    conn.close()
    return events
