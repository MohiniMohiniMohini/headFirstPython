vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []
vowel = set(word).intersection(vowels)

if len(vowel) == 0:
    print("No vowels found in the word: ", word)
else:
    for letter in vowel:
        print(letter)
