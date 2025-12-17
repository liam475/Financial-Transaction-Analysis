from db import init_db, add_transaction, list_transactions, import_from_csv
from analysis import summary_by_category, monthly_cashflow
from charts import category_bar_chart, monthly_net_cashflow_chart
def prompt_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Enter a valid number.")

def main():
    init_db()
    print("\nFinancial Transaction Analysis System\n")

    while True:
        print("1) Add transaction")
        print("2) List transactions")
        print("3) Summary by category")
        print("4) Monthly cashflow")
        print("5) Category bar chart")
        print("6) Monthly net cashflow chart")
        print("7) Import transactions from CSV")
        print("8) Exit")

        choice = input("Choose 1-8: ").strip()
        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            desc = input("Description: ")
            amt = prompt_float("Amount (positive income, negative expense): ")
            cat = input("Category: ")
            add_transaction(date, desc, amt, cat)
            print("Added.")

        elif choice == "2":
            for row in list_transactions():
                print(row)

        elif choice == "3":
            for cat, total in summary_by_category():
                print(cat, total)

        elif choice == "4":
            for m, inc, exp, net in monthly_cashflow():
                print(m, inc, exp, net)

        elif choice == "5":
            category_bar_chart()

        elif choice == "6":
            monthly_net_cashflow_chart()
        elif choice == "7":
            filename = input("CSV filename (example: transactions.csv): ").strip()
            import_from_csv(filename)
            print("CSV data imported.")
        elif choice == "8":
            print("Bye.")
            break

    else:
        print("Pick 1-8.")

if __name__ == "__main__":
    main()