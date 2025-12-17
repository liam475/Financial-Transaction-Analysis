from db import get_conn

def summary_by_category():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT category, ROUND(SUM(amount), 2)
        FROM transactions
        GROUP BY category
        ORDER BY 2 ASC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows

def monthly_cashflow():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT SUBSTR(tx_date, 1, 7),
               ROUND(SUM(CASE WHEN amount > 0 THEN amount ELSE 0 END), 2),
               ROUND(ABS(SUM(CASE WHEN amount < 0 THEN amount ELSE 0 END)), 2),
               ROUND(SUM(amount), 2)
        FROM transactions
        GROUP BY 1
        ORDER BY 1
    """)
    rows = cur.fetchall()
    conn.close()
    return rows