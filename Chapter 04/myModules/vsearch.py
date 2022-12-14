def commVowels(word:str):

  """Displays vowels found in the word"""

  vowels = set("aeiou")
  cv = vowels.intersection(set(word))
  for vowel in sorted(cv):
    print(vowel)

def isVowelPresent(word:str)->bool:
  
  """Returns true if vowel is present"""

  vowels = set("aeiou")
  cv = vowels.intersection(set(word))
  return (bool(cv))

def vowelSet(word:str)->set:
  
  """Returns true if vowel is present"""

  vowels = set("aeiou")
  cv = vowels.intersection(set(word))
  return (cv)

def search4letters(phrase:str, letters:str="aeiou") ->set :
  """ returns a set of \'letters\' found in \'phrase\'"""
  return set(phrase).intersection(set(letters))

def commVowelsInp():
  
  """Displays vowels found in the input word"""

  vowels = set("aeiou")
  word = input("Enter the word ")
  cv = vowels.intersection(set(word))
  for vowel in sorted(cv):
    print(vowel)
