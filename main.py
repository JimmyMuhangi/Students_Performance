# A simple project to tract Students performace
# student_performance.py

import pandas as pd

# List to store student records
students = []

# Function to add a student
def add_student():
    name = input("Enter Student Name: ")
    index_number = input("Enter Index Number: ")
    mid_term = float(input("Enter Mid-term Marks: "))
    end_term = float(input("Enter End-term Marks: "))

    total_marks = mid_term + end_term
    percentage = (total_marks / 200) * 100  # Assuming each exam is out of 100

    student = {
        "Name": name,
        "Index Number": index_number,
        "Mid-term Marks": mid_term,
        "End-term Marks": end_term,
        "Total Marks": total_marks,
        "Percentage": round(percentage, 2)
    }

    students.append(student)
    print(f"\nStudent {name} added successfully!\n")

# Function to display student records
def display_students():
    if not students:
        print("\nNo student records available!\n")
        return
    df = pd.DataFrame(students)
    print("\nStudent Performance Records:\n")
    print(df.to_string(index=False))

# Main menu
while True:
    print("\nSTUDENT PERFORMANCE TRACKER")
    print("1. Add Student")
    print("2. View Records")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
