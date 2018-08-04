phrase = "don't panic!"
plist = list(phrase)

new_phrase = ''.join(plist[1:3])
new_phrase += ''.join([plist[5], plist[4], plist[7], plist[6]])

print(new_phrase)

for char in plist:
    print('\t', char)

# now backwords
for char in plist[::-1]:
    print('\t' * 2, char)