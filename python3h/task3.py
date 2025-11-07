import random

print("Think of a number between 1 and 100...")

low = 1
high = 100
guess_count = 0
feedback = ""

while feedback != "correct":
    guess_count += 1
    # Make a guess in the middle of the current range
    guess = (low + high) // 2
    
    feedback = input(f"My guess is {guess}. (higher/lower/correct): ").lower().strip()
    
    if feedback == "higher":
        # If your number is higher, the new low is one above our guess
        low = guess + 1
    elif feedback == "lower":
        # If your number is lower, the new high is one below our guess
        high = guess - 1
    elif feedback != "correct":
        print("Sorry, I didn't understand. Please enter 'higher', 'lower', or 'correct'.")

print(f"I got it in {guess_count} guesses!")