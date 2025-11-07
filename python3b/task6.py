try:
    # Get user input
    lower_bound = int(input("Enter lower bound: "))
    upper_bound = int(input("Enter upper bound: "))

    # Check and swap bounds if necessary
    if lower_bound > upper_bound:
        print("Error: Lower bound must be less than or equal to the upper bound. Swapping bounds.")
        lower_bound, upper_bound = upper_bound, lower_bound

    # Calculate the sum
    total_sum = 0
    # The range function is non-inclusive of the second argument, so we use upper_bound + 1
    for num in range(lower_bound, upper_bound + 1):
        total_sum += num

    # Print the final result (outside the loop)
    print(f"The sum of numbers from {lower_bound} to {upper_bound} is {total_sum}")

except ValueError:
    # Handle the error if input is not a whole number
    print("Invalid input. Please enter whole numbers only.")
