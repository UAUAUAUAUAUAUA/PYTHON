# Ask the user for a word
word = input("Enter a word: ")

# Start with an empty string for the reversed word
reversed_str = ""

# Loop through each character in the original word
for char in word:
    reversed_str = char + reversed_str  # Add each character to the front

# Display the reversed string
print(reversed_str)
