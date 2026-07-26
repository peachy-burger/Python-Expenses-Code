# Import csv
import csv

expenses = []

def updated_income():
# Input monthly income
    monthly_income = float(input("\nYour monthly income is: R"))
    while monthly_income < 0:
        monthly_income = float(input("Income can't be negative. Re-enter: R"))
    return monthly_income

# Input expenses, thresholds and costs

def add_expense():
    name = input("\nEnter the name of your expense: ")

    threshold = float(input(f"Enter threshold for {name}: R"))
    while threshold < 0:
        threshold = float(input("Threshold can't be negative. Re-enter: R"))

    cost = float(input(f"Enter cost of {name}: R"))
    while cost < 0:
        cost = float(input("Cost can't be negative. Re-enter: R"))

    if cost > threshold:
        print(f"Your {name} expense exceeds the threshold")

    expenses.append({
        "name": name,
        "threshold": threshold,
        "cost": cost
    })

# Calculations

def calculate_balance(income):
    total_expenses = sum(expense["cost"] for expense in expenses)
    balance = income - total_expenses
    return total_expenses, balance

# Check threshold

def check_thresholds():
    print("\nThreshold Check:")
    for expense in expenses:
        status = "meets threshold" if expense["cost"] <= expense["threshold"] else "over threshold"
        threshold_total = sum(expense["threshold"] for expense in expenses)
        print(f"\n{expense['name']}: Cost = R{expense['cost']}, Threshold = R{expense['threshold']} = {status}")
        print("\nTotal threshold amount set for all expenses is: R", threshold_total)

# Search for expenses

def search_expenses_by_expense_name():
    search_name = input("\nEnter expense name to search for: ")
    found = False
    for expense in expenses:
        if expense["name"].lower() == search_name.lower():
            print(f"{expense['name']} - Cost: R{expense['cost']}, Threshold: R{expense['threshold']}")
            found = True
    if not found:
        print("Expense not found.")

# Generate CSV

def generate_csv_report(income):
    total_expenses, balance = calculate_balance(income)
    filename = "budget_report.csv"
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount", "Threshold"])
        for expense in expenses:
            writer.writerow([expense["name"], f"R{expense['cost']}", f"R{expense['threshold']}"])
        writer.writerow([])
        writer.writerow(["Total Expenses", f"R{total_expenses}", ""])
        writer.writerow(["Remaining Balance", f"R{balance}", ""])
    print(f"\nReport saved to {filename}")

# Main menu options

def main():
    income = updated_income()

    while True:
        print("\nMENU")
        print("1. Add Expense")
        print("2. Update Monthly Income")
        print("3. View Balance")
        print("4. Check Thresholds")
        print("5. Search Expenses by Expense Name")
        print("6. Generate CSV Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            print(float(input("\nEnter your updated monthly income: R")))
        elif choice == "3":
            total_expenses, balance = calculate_balance(income)
            print(f"\nTotal Expenses: R{total_expenses}")
            print(f"Remaining Balance: R{balance}")
        elif choice == "4":
            check_thresholds()
        elif choice == "5":
            search_expenses_by_expense_name()
        elif choice == "6":
            generate_csv_report(income)
        elif choice == "7":
            print("You're welcome for the service.")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()