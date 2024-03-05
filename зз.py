# Input word for checking
word = input("Enter a word: ")

# Convert the word to lowercase for simplification of the check
word = word.lower()

# Variable to store the result of the check
is_palindrome = True

# Loop for palindrome check
for i in range(len(word) // 2):
    if word[i] != word[len(word) - i - 1]:
        is_palindrome = False
        break

# Output the result
if is_palindrome:
    print("The word", word, "is a palindrome.")
else:
    print("The word", word, "is not a palindrome.")
