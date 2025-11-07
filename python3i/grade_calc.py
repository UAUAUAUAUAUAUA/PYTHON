# Ben B, Jamelle, Yarosalv
def display_menu():
    """Display the main menu options."""
    print("\n--- GRADE CALCULATOR MENU ---")
    print("1. Add a grade")
    print("2. View grade report")
    print("3. Quit")
def add_grade(grades):
    """
    Prompt for a new grade, validate it, and add it to the list.
    Parameters:
        grades (list): The current list of grades.
    Returns:
        list: The updated list of grades.
    """
    while True:
        try:
            # ask user for a grade
            grade_input = input("Enter grade (0-100): ")
            grade = float(grade_input)
            # Validate the grade is in the correct range, I didnt know if I should add a extra credit option here or make the range over 100 so I left it.
            if 0 <= grade <= 100:
                grades.append(grade)
                print(f"Grade {grade} added")
                return grades
            else:
                # Handle out of range input
                print("Error: Grade must be between 0 and 100.")
        except ValueError:
            # Handle non-numeric input
            print("Error: Invalid input. Please enter a number.")
def calculate_average(grades):
    """
    Calculate and return the average of grades.
    Handles empty lists to avoid division by zero.
    Parameters:
        grades (list): A list of grades (numbers).
    Returns:
        float: The average, or 0.0 if the list is empty.
    """
    if not grades:
        return 0.0
    return sum(grades) / len(grades)
def get_letter_grade(average):
    """
    Convert numeric average to letter grade.
    Parameters:
        average (float): The numeric average.
    Returns:
        str: The corresponding letter grade.
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"
def find_highest(grades):
    """
    Find and return the highest grade.
    Parameters:
        grades (list): The list of grades.
    Returns:
        float or None: The highest grade, or None if list is empty.
    """
    if not grades:
        return None
    return max(grades)
def find_lowest(grades):
    """
    Find and return the lowest grade.
    Parameters:
        grades (list): The list of grades.
    Returns:
        float or None: The lowest grade, or None if list is empty.
    """
    if not grades:
        return None
    return min(grades)
def display_report(grades):
    """Display complete grade report with statistics."""
    print("\n═══════════════")
    print(" Grade Report    ")
    print("═══════════════")
    # Handle case with no grades
    if not grades:
        print("No grades entered yet.")
        return
    # Calculate statistics
    average = calculate_average(grades)
    letter_grade = get_letter_grade(average)
    highest = find_highest(grades)
    lowest = find_lowest(grades)
    # Display results
    print(f"Grades: {', '.join(str(g) for g in grades)}")
    print(f"Number of assignments: {len(grades)}")
    print("---")
    print(f"Average: {average:.1f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
# --- Main program ---
def main():
    """Main function to run the grade calculator."""
    print("=== STUDENT GRADE CALCULATOR ===")
    student_grades = []
    while True:
        display_menu()
        choice = input("Choice: ").strip()
        if choice == '1':
            # Add_grade modifies the list in place, but we reassign
            # for clarity, showing it returns the modified list.
            student_grades = add_grade(student_grades)
        elif choice == '2':
            display_report(student_grades)
        elif choice == '3':
            print("Goodbye")
            break
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()