total_sum = 0
while (number := int(input("Enter a number (0 to stop): "))) != 0:
    total_sum += number
print(f"Total sum: {total_sum}")