inpStr = input("Enter the string to check ")
vowels = ['a', 'e', 'i', 'o', 'u']
found = {};

for vowel in vowels:
  found[vowel] = 0

for letter in inpStr:
  if letter in vowels:
    found[letter] += 1
    
for k, v in sorted(found.items()):
  print(k, " was found ", v, " times ")
