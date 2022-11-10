## GTG

phrase = "Don't panic!" 
plist = list(phrase) 
print(phrase) 
print(plist)

plist = plist[1:-4]
plist.remove('\'')
plist.extend([plist.pop(), plist.pop(), plist.pop()] )
plist.insert(2, plist.pop())
new_phrase = ''.join(plist)
print(new_phrase)
## TYJC
