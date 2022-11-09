## GTG

phrase = "Don't panic!" 
plist = list(phrase) 
print(phrase) 
print(plist)

plist.remove('D')
plist.remove('\'')

for i in range(4):
  plist.pop()

plist.insert(2, plist.pop(3))
plist.insert(4, plist.pop())

new_phrase = ''.join(plist)
print(new_phrase)
## TYJC
