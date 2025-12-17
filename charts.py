import matplotlib.pyplot as plt
from db import get_conn

def category_bar_chart():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT category, SUM(amount) AS total
        FROM transactions
        GROUP BY category
        ORDER BY total ASC
    """)
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No data to chart.")
        return

    categories = [r[0] for r in rows]
    totals = [r[1] for r in rows]

    plt.figure()
    plt.title("Total by Category (Income positive, Expenses negative)")
    plt.bar(categories, totals)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()

def monthly_net_cashflow_chart():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT SUBSTR(tx_date, 1, 7) AS month,
               SUM(amount) AS net
        FROM transactions
        GROUP BY month
        ORDER BY month
    """)
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No data to chart.")
        return

    months = [r[0] for r in rows]
    net = [r[1] for r in rows]

    plt.figure()
    plt.title("Monthly Net Cashflow")
    plt.plot(months, net, marker="o")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()