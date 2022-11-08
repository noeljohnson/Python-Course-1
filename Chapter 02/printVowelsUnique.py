##GTG

# Following program is to print all vowels in a wor d only once

vowels = ['a', 'e', 'i', 'o', 'u']
found = []

word = input("Provide a word to search for vowels: ")

for letter in word:
  if (letter in vowels):
    if not(letter in found):
      found.append(letter)

for vowel in found:
  print(vowel)

##TYJC
