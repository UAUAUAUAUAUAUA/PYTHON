# 1. Ask the user to type something
text = input("Enter text: ")

# 2. Create "boxes" (variables) to store our counts, starting at 0
vowel_count = 0
consonant_count = 0

# 3. Create a list of all the vowels we want to check
vowels = "aeiou"

# 4. Start a loop to check every single character in the user's text
for char in text:
    
    # 5. First, check if the character is a letter (A-Z or a-z)
    #    This .isalpha() check ignores spaces, numbers, and "!"
    if char.isalpha():
        
        # 6. Convert the letter to lowercase so we only have to check once
        #    This turns 'H' into 'h' and keeps 'e' as 'e'
        char_lower = char.lower() 
        
        # 7. Check if this lowercase letter is in our vowel list
        if char_lower in vowels:
            # If it is, add 1 to the vowel box
            vowel_count += 1 
        else:
            # If it's a letter but NOT a vowel, it must be a consonant
            consonant_count += 1

# 8. After the loop is all done, print the final totals
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
