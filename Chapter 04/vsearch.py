def commVowels(word):
  
  """Displays vowels found in the word"""

  vowels = set("aeiou")
  cv = vowels.intersection(set(word))
  for vowel in sorted(cv):
    print(vowel)


def commVowelsInp():
  
  """Displays vowels found in the input word"""

  vowels = set("aeiou")
  word = input("Enter the word ")
  cv = vowels.intersection(set(word))
  for vowel in sorted(cv):
    print(vowel)
