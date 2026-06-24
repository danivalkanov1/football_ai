import sqlite3
from config import DB_PATH

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def execute(sql: str, params: tuple = ()):
    conn = get_connection()
    try:
        cur = conn.execute(sql, params)
        conn.commit()
        return cur.lastrowid, cur.rowcount
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def fetch_all(sql: str, params: tuple = ()):
    conn = get_connection()
    try:
        rows = conn.execute(sql, params).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()

def fetch_one(sql: str, params: tuple = ()):
    conn = get_connection()
    try:
        row = conn.execute(sql, params).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()
