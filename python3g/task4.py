total = 0      # keeps track of the sum of all numbers
count = 0      # keeps track of how many numbers were entered

while True:
    num = int(input("Enter any number (-1 to stop): "))
    if num == -1:
        print("You're done!")
        break  # exit the loop when -1 is entered
    
    total += num   # add the number to the running total
    count += 1     # count how many valid numbers were entered

print(f"Average = {total / count}")
