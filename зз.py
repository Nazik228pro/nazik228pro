# Enter a word to check
word = input("Enter word: ")
 
# Convert the word to lowercase to simplify verification
word = word.lower()
 
# Variable to store the result of the check
is_palindrome = True
 
# Loop to check palindrome
for i in range(len(word) // 2):
    if word[i] != word[len(word) - i - 1]:
        is_palindrome = False
        break
 
# Output the result
if is_palindrome:
    print("Word", word, "is a palindrome.")
else:
    print("Word", word, "is not a palindrome.")