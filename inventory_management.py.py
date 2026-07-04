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