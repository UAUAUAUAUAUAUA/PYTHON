import random

print("Flipping a coin 20 times...")
heads_count = 0
tails_count = 0

for _ in range(20):
    # 0 = Heads, 1 = Tails
    flip = random.randint(0, 1)
    
    if flip == 0:
        print("H", end=" ")
        heads_count += 1
    else:
        print("T", end=" ")
        tails_count += 1

# Print a newline to separate results from the flip string
print() 
print(f"Heads: {heads_count}")
print(f"Tails: {tails_count}")