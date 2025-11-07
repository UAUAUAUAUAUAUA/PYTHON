# Prints all even numbers from 0 to 20 on one line, separated by spaces.

# Use range(start, stop, step) -> range(0, 21, 2)
# The loop will go from 0, 2, 4, ..., 20.
for even_num in range(0, 21, 2):
    # Print the number, followed by a space instead of a newline
    print(even_num, end=" ")

# Print a final newline character to clean up the output after the loop finishes
print()

