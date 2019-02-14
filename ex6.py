input_word = input("To be tested if palindrome(same backwards and forward, e.g., Otto):\n>>")
input_word = input_word.lower()
pal = ""

for letter in range(len(input_word)-1, -1, -1):
    pal += input_word[letter]

if pal == input_word:
    print("\nA palin to the drome!!!!\n\nWootWoot")
else:
    print("\nNo drome for your palin.")
