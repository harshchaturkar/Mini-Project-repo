expenses = []
# Set Monthly Budget
budget = float(input("Enter Monthly Budget: Rs. "))

# Add Expense
def add_expense():
    description = input("Enter Expense Description: ")
    category = input("Enter Category: ")
    
    try:
        amount = float(input("Enter Amount: Rs. "))
        
        if amount <= 0:
            print("Amount must be greater than 0!")
            return
            
    except ValueError:
        print("Invalid Amount!")
        return

    date = input("Enter Date (DD-MM-YYYY): ")

    expense = {
        "description": description,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    print("Expense Added Successfully!")

# View All Expenses
def view_expenses():
    if not expenses:
        print("No Expenses Found!")
        return

    print("\n===== ALL EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(i, expense["description"],
              expense["category"],
              expense["amount"],
              expense["date"])

# Category Summary
def category_summary():
    if not expenses:
        print("No Expenses Found!")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n===== CATEGORY SUMMARY =====")

    for category, total in summary.items():
        print(category, ": Rs.", total)

# Find Highest Spending Category
def get_top_category():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    top_category = ""
    max_amount = 0

    for category, total in summary.items():
        if total > max_amount:
            max_amount = total
            top_category = category

    return top_category, max_amount

# Budget Report
def budget_report():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    remaining = budget - total
    percentage = (total / budget) * 100

    print("\n===== BUDGET REPORT =====")
    print("Total Spent : Rs.", total)
    print("Budget Limit: Rs.", budget)
    print("Remaining   : Rs.", remaining)
    print("Used        :", round(percentage, 2), "%")

    if percentage >= 100:
        print("WARNING: Budget Exceeded!")
    elif percentage >= 80:
        print("WARNING: You have used 80% of your budget!")

    category, amount = get_top_category()

    if category:
        print("Top Category:", category, "(Rs.", amount, ")")

# Main Menu
while True:

    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        budget_report()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")