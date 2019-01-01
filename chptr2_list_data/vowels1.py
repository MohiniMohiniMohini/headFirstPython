vowels = ['a', 'e', 'i', 'o', 'u']
vowels = list(vowels)
word = input("Provide a word to search for vowels: ")
found = []
for letter in word:
    if letter in vowels:
        print(letter)
        vowels.remove(letter)

if len(vowels) == 5:
    print("No Vowels found in the word: ", word)
