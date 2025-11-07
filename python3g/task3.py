correct_password = "python123"
# Get the *first* password *before* the loop
password = input("Enter password: ")

# Loop *while* the password is not correct
while password != correct_password:
    print("Incorrect! Try again.")
    # Get the *next* password *inside* the loop
    password = input("Enter password: ")

# This line only runs when the loop condition is false (password is correct)
print("Access granted!")