import sqlite3, os
from datetime import datetime

DB_PATH = "data/chat_history.db"
os.makedirs("data", exist_ok=True)

def save_message(platform, user_msg, ai_msg):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT, user_msg TEXT, ai_msg TEXT, ts TEXT)""")
    c.execute("INSERT INTO messages (platform, user_msg, ai_msg, ts) VALUES (?,?,?,?)",
              (platform, user_msg, ai_msg, datetime.now()))
    conn.commit()
    conn.close()

def get_messages(limit=30):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT platform, user_msg, ai_msg, ts FROM messages ORDER BY id DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    return rows
