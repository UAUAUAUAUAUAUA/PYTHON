number = int(input("Enter a number: "))
original_number = number  # Save for the final print message
product = 1
count = 1

while count <= number:
    product *= count  # product = product * count
    count += 1        # count = count + 1

print(f"{original_number}! = {product}")2