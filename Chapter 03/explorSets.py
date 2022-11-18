##GTG

vowels = set("aeeiouu") #creating a set from a string, the elements are the character in the set

word = "hello"

u = vowels.union(set(word)) # finds the union between vowels and set("hello")
print("Union :", u)

d = vowels.difference(set(word)) # finds those vowels that are not present in word
print("Diffrence :", d)

i = vowels.intersection(set(word)) # finds the vowels present in word
print("Intersection :", i)

##TYJC
