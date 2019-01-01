phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
plist1 = plist[1:3:1] + plist[5:6:1] + plist[4:5:1] + plist[7:8:1] + plist[6:7:1]
print(plist)

new_phrase = ''.join(plist1)
print(plist)
print(new_phrase)
