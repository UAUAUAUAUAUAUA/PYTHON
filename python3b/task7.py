try:
    # 1. Get user input
    limit = int(input("Enter a number: "))

    # 2. Initialize sum
    odd_sum = 0

    # 3. Calculate the sum of odd numbers
    # The range function efficiently steps through only odd numbers (1, 3, 5, ...)
    # We use limit + 1 to include the limit if it is an odd number.
    for num in range(1, limit + 1, 2):
        odd_sum += num

    # 4. Print the final result (outside the loop)
    print(f"The sum of odd numbers from 1 to {limit} is {odd_sum}")

except ValueError:
    # 5. Handle the error if input is not a valid integer
    print("Invalid input. Please enter a whole number.")
