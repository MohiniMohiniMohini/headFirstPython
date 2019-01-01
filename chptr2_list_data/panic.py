phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist.remove('D')
plist.remove('\'')
plist.remove(' ')
plist.insert(2, ' ')
plist.insert(4, 'a')
for i in range(len(plist), 6, -1):
    plist.pop()

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
