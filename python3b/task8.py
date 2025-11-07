# Line 1: Counting Up (1 to 10)
up_string = ""
# range(1, 11) generates numbers 1, 2, 3, ..., 10
for i in range(1, 11):
    # Append the number and a space
    up_string += str(i) + " "

# Print the line, stripping the trailing space
print(up_string.strip())

# ---

# Line 2: Counting Down (10 to 1)
down_string = ""
# range(10, 0, -1) generates numbers 10, 9, 8, ..., 1
for i in range(10, 0, -1):
    # Append the number and a space
    down_string += str(i) + " "

# Print the line, stripping the trailing space
print(down_string.strip())
