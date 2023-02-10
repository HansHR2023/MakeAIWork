

# # Define the string “paard”
# word = "paard"
# result = 0

# # > Loop over each letter in string:
# for char in word:
#     # Check if character is vowel:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y':
# 	# If so then increment counter
#         result = result + 1
# # Print result
# print(f"The word {word} contains {result} vowels")



# Define the string “paard”
word = input("Enter a word:  ")
word = word.lower()
vowel = ['a', 'e', 'i', 'ij','o', 'u','y']
result = 0

# > Loop over each letter in string:
for char in word:
    # Check if character is vowel:
    if char in vowel:
	# If so then increment counter
        result = result + 1
# Print result
print(f"The word {word} contains {result} vowels")

#improvement: convert string to string.lower() zodat je ook hoofdletters meeneemt. Dan speciale tekens als a met umlaut etc