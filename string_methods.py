## string methods
# .len()
# .find()
# .lower()
# .upper()
# .title()
# .replace()
# '....' in string



sample_string = "Pythons for Beginners"

print("==========.len()==========")
print(f'The length of string "{sample_string}" is {len(sample_string)}')
print()
print("==========.find()==========")
word_to_be_find = input(f"Enter the character or word, to find the index from '{sample_string}': ")
print(f'''
You have input: {word_to_be_find}.

The index of {word_to_be_find} is: {sample_string.find(word_to_be_find)}
''')

print()
print("==========.lower()==========")
print(f"The lowercase of the '{sample_string}': {sample_string.lower()}")

print()
print("==========.upper()==========")
print(f"The uppercase of the '{sample_string}': {sample_string.upper()}")

print()
print("==========.title()==========")
print(sample_string.title())


print()
print("==========.replace()==========")
new_word = input("Enter new word: ")
old_word= input("Enter old word: ")
replaced_string = sample_string.replace(old_word, new_word)
print(replaced_string)

print()
print("=========='.....' in string==========")
word_to_check = input("Enter the word to check in the string?")
print(word_to_check in sample_string)