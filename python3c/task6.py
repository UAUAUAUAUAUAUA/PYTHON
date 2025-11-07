# Ask for the student's name
student_name = input("Student name: ")

# Initialize lists for subjects and grades
subjects = []
grades = []

# Loop to collect 5 subjects and grades
for i in range(1, 6):
    subject = input(f"Enter subject {i}: ")
    grade = float(input(f"Enter grade {i}: "))
    subjects.append(subject)
    grades.append(grade)

# Calculate average grade
average = sum(grades) / len(grades)

# Determine letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the report card
print("\nREPORT CARD")
print("Student:", student_name)
print()

for i in range(5):
    print(subjects[i], "grade is", grades[i])

print("\nAverage grade:", round(average, 2))
print("Letter grade:", letter_grade)
