library = {}
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
        print("Invalid Choice!")

