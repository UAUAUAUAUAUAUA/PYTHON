import random

wins = 0
losses = 0
# Start with the first number
current_num = random.randint(1, 100)

while True:
    print("-" * 20)
    print(f"Current number: {current_num}")
    guess = input("Will the next number be (h)igher or (l)ower? (q to quit): ").lower().strip()

    if guess == 'q':
        break
        
    if guess not in ('h', 'l'):
        print("Invalid input. Please enter 'h', 'l', or 'q'.")
        continue

    # Generate the next number
    next_num = random.randint(1, 100)
    
    # Optional: Re-roll if it's the same number to avoid a tie
    while next_num == current_num:
        next_num = random.randint(1, 100)
        
    print(f"Next number: {next_num}")

    # Check the user's guess
    is_higher = next_num > current_num
    
    if (guess == 'h' and is_higher) or (guess == 'l' and not is_higher):
        print("You win!")
        wins += 1
    else:
        print("You lose!")
        losses += 1

    print(f"Score: {wins} wins, {losses} losses")
    
    # The next number becomes the current number for the next round
    current_num = next_num

print("\nThanks for playing!")
print(f"Final Score: {wins} wins, {losses} losses")