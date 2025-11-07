while True:
    grade = int(input("Enter a grade (0-100): "))

    if 0 <= grade <= 100:
        print(f"Valid grade accepted: {grade}")
        break  # Exit the loop
    else:
        print("Invalid! Must be between 0 and 100.")-4