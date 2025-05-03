import sqlite3

def init_db():
    conn = sqlite3.connect('rolls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rolls (
        roll_id TEXT PRIMARY KEY,
        roll_value INTEGER,
        roll_timestamp TEXT
    )''')
    conn.commit()
    conn.close()

def save_roll(roll):
    conn = sqlite3.connect('rolls.db')
    c = conn.cursor()
    c.execute("INSERT INTO rolls VALUES (?, ?, ?)",
              (roll['roll_id'], roll['roll_value'], roll['roll_timestamp'].isoformat()))
    conn.commit()
    conn.close()