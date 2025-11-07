import random

print("Rolling a die 10 times:")
for _ in range(10):
    roll = random.randint(1, 6)
    print(roll, end=" ")