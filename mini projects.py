'''students = {}
# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "B+"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

# Function to add student
def add_student():
    try:
        roll_no = int(input("Enter Roll Number: "))

        if roll_no in students:
            print(" Roll Number already exists!")
            return

        name = input("Enter Student Name: ")

        marks = []
        total = 0

        print("Enter Marks for 5 Subjects:")
        for i in range(1, 6):
            mark = float(input(f"Subject {i}: "))
            marks.append(mark)
            total += mark

        percentage = total / 5
        grade = calculate_grade(percentage)

        students[roll_no] = {
            "name": name,
            "marks": marks,
            "percentage": percentage,
            "grade": grade
        }

        print("\n Student Added Successfully!")

    except ValueError:
        print(" Invalid Input!")

# Function to display all students
def view_all():
    if not students:
        print("No Records Found!")
        return

    print("\n" + "=" * 80)
    print(f"{'Roll No':<10}{'Name':<20}{'Percentage':<15}{'Grade':<10}")
    print("=" * 80)

    for roll, data in students.items():
        print(
            f"{roll:<10}{data['name']:<20}{data['percentage']:<15.2f}{data['grade']:<10}"
        )

    print("=" * 80)

# Function to search student
def search_student():
    roll_no = int(input("Enter Roll Number to Search: "))

    if roll_no in students:
        data = students[roll_no]

        print("\nStudent Found")
        print("-" * 30)
        print("Roll No    :", roll_no)
        print("Name       :", data["name"])
        print("Marks      :", data["marks"])
        print("Percentage :", round(data["percentage"], 2))
        print("Grade      :", data["grade"])

    else:
        print(" Student Not Found!")

# Function to update student
def update_student():
    roll_no = int(input("Enter Roll Number to Update: "))

    if roll_no not in students:
        print(" Student Not Found!")
        return

    print("\n1. Update Name")
    print("2. Update Marks")

    choice = input("Enter Choice: ")

    if choice == "1":
        new_name = input("Enter New Name: ")
        students[roll_no]["name"] = new_name
        print(" Name Updated Successfully!")

    elif choice == "2":
        marks = []
        total = 0

        print("Enter New Marks for 5 Subjects:")

        for i in range(1, 6):
            mark = float(input(f"Subject {i}: "))
            marks.append(mark)
            total += mark

        percentage = total / 5
        grade = calculate_grade(percentage)

        students[roll_no]["marks"] = marks
        students[roll_no]["percentage"] = percentage
        students[roll_no]["grade"] = grade

        print(" Marks Updated Successfully!")

    else:
        print(" Invalid Choice!")

# Function to delete student
def delete_student():
    roll_no = int(input("Enter Roll Number to Delete: "))

    if roll_no in students:
        confirm = input("Are you sure? (y/n): ")

        if confirm.lower() == "y":
            del students[roll_no]
            print(" Student Deleted Successfully!")
    else:
        print(" Student Not Found!")

# Function to display menu
def show_menu():
    print("\n" + "=" * 40)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 40)

# Main Program
while True:
    show_menu()

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_all()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("Thank You! Exiting Program...")
            break

        else:
            print(" Please Enter a Valid Choice (1-6)!")

    except ValueError:
        print(" Invalid Input! Enter Numbers Only.")'''
















'''library = {}
# Add Book
def add_book():
    isbn = input("Enter ISBN: ")

    if isbn in library:
        print("ISBN already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower": None
    }

    print("Book Added Successfully!")

# Issue Book
def issue_book():
    isbn = input("Enter ISBN: ")

    if isbn not in library:
        print("Book Not Found!")
        return

    if not library[isbn]["available"]:
        print("Book Already Issued!")
        return

    borrower = input("Enter Borrower Name: ")

    library[isbn]["available"] = False
    library[isbn]["borrower"] = borrower

    print("Book Issued Successfully!")

# Return Book
def return_book():
    isbn = input("Enter ISBN: ")

    if isbn not in library:
        print("Book Not Found!")
        return

    if library[isbn]["available"]:
        print("Book is already available!")
        return

    library[isbn]["available"] = True
    library[isbn]["borrower"] = None

    print("Book Returned Successfully!")

# Search Book
def search_book():
    keyword = input("Enter Title or Author: ").lower()

    found = False

    for isbn, book in library.items():
        if keyword in book["title"].lower() or keyword in book["author"].lower():

            status = "Available"
            if not book["available"]:
                status = "Issued"

            print("\nISBN :", isbn)
            print("Title :", book["title"])
            print("Author :", book["author"])
            print("Status :", status)

            found = True

    if not found:
        print("Book Not Found!")

# View All Books
def view_catalog():
    if not library:
        print("No Books Available!")
        return

    print("\n" + "=" * 70)
    print("ISBN\t\tTitle\t\tAuthor\t\tStatus")
    print("=" * 70)

    for isbn, book in library.items():

        status = "Available"
        if not book["available"]:
            status = "Issued"

        print(isbn, "\t", book["title"], "\t",
              book["author"], "\t", status)

# Menu
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View Catalog")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        issue_book()

    elif choice == "3":
        return_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        view_catalog()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")'''











'''expenses = []
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
        print("Invalid Choice!")'''












'''# Question Bank (Tuple)
questions = (
    ("Which data type is immutable in Python?",
     "List", "Dictionary", "Tuple", "Set", "C"),

    ("Which keyword is used to define a function?",
     "func", "define", "def", "function", "C"),

    ("Which operator is used for exponentiation?",
     "*", "^", "**", "//", "C"),

    ("What is the output of len('Python')?",
     "5", "6", "7", "8", "B"),

    ("Which loop is used when number of iterations is known?",
     "while", "for", "do while", "none", "B"),

    ("Which symbol is used for comments?",
     "//", "#", "/*", "%", "B"),

    ("Which function takes user input?",
     "print()", "scan()", "input()", "read()", "C"),

    ("Python is a ______ language.",
     "Compiled", "Interpreted", "Assembly", "Machine", "B"),

    ("Which collection stores key-value pairs?",
     "Tuple", "List", "Dictionary", "Set", "C"),

    ("Which function displays output?",
     "input()", "show()", "print()", "display()", "C")
)

# Grade Function
def calculate_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "B+"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    else:
        return "F"

# Main Quiz Function
def start_quiz():

    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    score = 0
    wrong_answers = []

    print("\n===== PYTHON QUIZ SYSTEM =====")
    print("Student:", name, "| Roll:", roll)

    q_no = 1

    for q in questions:

        print("\nQ" + str(q_no) + ".", q[0])

        print("A.", q[1])
        print("B.", q[2])
        print("C.", q[3])
        print("D.", q[4])

        answer = input("Your Answer (A/B/C/D): ").upper()

        if answer == q[5]:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Wrong!")
            print("Correct Answer:", q[5])

            wrong_answers.append(
                {
                    "question": q[0],
                    "correct": q[5]
                }
            )

        q_no += 1

    total = len(questions)
    percent = (score / total) * 100
    grade = calculate_grade(percent)

    print("\n===== RESULT REPORT =====")
    print("Name    :", name)
    print("Roll No :", roll)
    print("Score   :", score, "/", total)
    print("Percent :", round(percent, 2), "%")
    print("Grade   :", grade)

    if percent >= 50:
        print("Result  : PASS")
    else:
        print("Result  : FAIL")

    if wrong_answers:
        print("\n===== WRONG ANSWERS =====")

        for item in wrong_answers:
            print("Question :", item["question"])
            print("Correct Answer :", item["correct"])
            print()

# Run Quiz
start_quiz()'''












inventory = {}
transactions = []
# Load Inventory
def load_inventory():
    try:
        file = open("inventory.txt", "r")

        for line in file:
            data = line.strip().split(",")

            inventory[data[0]] = {
                "name": data[1],
                "category": data[2],
                "price": float(data[3]),
                "quantity": int(data[4]),
                "reorder": int(data[5])
            }

        file.close()

    except FileNotFoundError:
        pass

# Save Inventory
def save_inventory():
    file = open("inventory.txt", "w")
    for pid, product in inventory.items():
        file.write(
            f"{pid},{product['name']},{product['category']},"
            f"{product['price']},{product['quantity']},"
            f"{product['reorder']}\n"
        )
    file.close()

# Add Product
def add_product():
    pid = input("Enter Product ID: ")

    if pid in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    reorder = int(input("Enter Reorder Level: "))

    inventory[pid] = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "reorder": reorder
    }
    print("Product Added Successfully!")

# Stock In
def stock_in():
    pid = input("Enter Product ID: ")

    if pid not in inventory:
        print("Product Not Found!")
        return

    qty = int(input("Enter Quantity to Add: "))

    inventory[pid]["quantity"] += qty

    transactions.append(f"IN - {pid} - {qty}")

    print("Stock Updated!")

# Stock Out
def stock_out():
    pid = input("Enter Product ID: ")

    if pid not in inventory:
        print("Product Not Found!")
        return

    qty = int(input("Enter Quantity to Remove: "))

    if qty > inventory[pid]["quantity"]:
        print("Insufficient Stock!")
        return

    inventory[pid]["quantity"] -= qty

    transactions.append(f"OUT - {pid} - {qty}")

    print("Stock Removed Successfully!")

# View Inventory
def view_inventory():

    if not inventory:
        print("No Products Available!")
        return

    print("\n===== INVENTORY =====")

    for pid, product in inventory.items():

        value = product["price"] * product["quantity"]

        print("\nID :", pid)
        print("Name :", product["name"])
        print("Category :", product["category"])
        print("Price :", product["price"])
        print("Quantity :", product["quantity"])
        print("Value :", value)

# Low Stock Alert
def low_stock_alert():

    print("\n===== LOW STOCK ITEMS =====")

    found = False

    for pid, product in inventory.items():

        if product["quantity"] <= product["reorder"]:

            found = True

            print(pid, "-", product["name"],
                  "(Qty:", product["quantity"], ")")

    if not found:
        print("No Low Stock Products!")

# Report
def generate_report():

    total_value = 0
    categories = set()

    for product in inventory.values():

        total_value += product["price"] * product["quantity"]

        categories.add(product["category"])

    print("\n===== INVENTORY REPORT =====")
    print("Total Products :", len(inventory))
    print("Total Stock Value : Rs.", total_value)
    print("Categories :", ", ".join(categories))

# Main Program
load_inventory()

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Save & Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()
        
    elif choice == "2":
        stock_in()

    elif choice == "3":
        stock_out()

    elif choice == "4":
        view_inventory()

    elif choice == "5":
        low_stock_alert()

    elif choice == "6":
        generate_report()

    elif choice == "7":
        save_inventory()
        print("Inventory Saved Successfully!")
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")