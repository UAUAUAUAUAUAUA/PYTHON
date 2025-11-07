# 1. Get the user's number
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

# 2. total = 0 (The accumulator starts at zero)
total = 0

# 3. Use range(1, number + 1) to loop through each number
for i in range(1, number + 1):
    total = total + i  # Add the current number (i) to the running total

# Output the final result
print(f"The final sum is: {total}")

