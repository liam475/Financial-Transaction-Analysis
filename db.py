import sqlite3

DB_NAME = "transactions.db"

def get_conn():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tx_date TEXT NOT NULL,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def add_transaction(tx_date, description, amount, category):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO transactions (tx_date, description, amount, category)
        VALUES (?, ?, ?, ?)
    """, (tx_date, description, amount, category))
    conn.commit()
    conn.close()

def list_transactions(limit=20):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, tx_date, description, amount, category
        FROM transactions
        ORDER BY tx_date DESC, id DESC
        LIMIT ?
    """, (limit,))
    rows = cur.fetchall()
    conn.close()
    return rows
import csv

def import_from_csv(filename):
    conn = get_conn()
    cur = conn.cursor()

    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [
            (
                row["date"],
                row["description"],
                float(row["amount"]),
                row["category"]
            )
            for row in reader
        ]

    cur.executemany("""
        INSERT INTO transactions (tx_date, description, amount, category)
        VALUES (?, ?, ?, ?)
    """, rows)

    conn.commit()
    conn.close()