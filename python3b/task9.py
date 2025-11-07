try:
    # Ask how many numbers the user wants to enter
    count = int(input("How many numbers? "))

    # Check for invalid count and proceed only if count > 0
    if count <= 0:
        # Instead of 'return', simply print the error and the program will end normally
        print("The number of inputs must be greater than zero.")
    else:
        total_sum = 0.0 # Use float to ensure accurate division later

        # Loop for the specified number of times
        for i in range(1, count + 1):
            # Prompt for and read each number
            num_input = float(input(f"Enter number {i}: "))
            # Add the number to the running total
            total_sum += num_input

        # Calculate the average
        average = total_sum / count

        print(f"The average is {average:.1f}") # Print with one decimal place

except ValueError:
    print("Invalid input. Please ensure you enter whole numbers for the count and valid numbers for the inputs.")
