students = {}
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
        print(" Invalid Input! Enter Numbers Only.")
