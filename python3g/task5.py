import random

secret_number = random.randint(1, 50)
guess_count = 0
print("I'm thinking of a number between 1 and 50...")

while True:
    guess = int(input("Your guess: "))
    guess_count += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! You got it in {guess_count} guesses!")
        break
