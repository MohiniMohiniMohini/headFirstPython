vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = {}
#initialize found dict.
#for letter in vowels:
 #   found[letter] = 0
    
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    if(v == 1):
        grammer = "time"
    else:
        grammer = "times"
    print(k, 'was found', v, grammer)
