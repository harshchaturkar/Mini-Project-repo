# Question Bank (Tuple)
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
start_quiz()
