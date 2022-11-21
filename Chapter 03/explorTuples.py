## GTG

t = (1,)

print(type(t))

# tuples are immuatble

t = (1, 2, 3, 4)

try:
  t[1] = 2
except:
  print("Couldn\'t mutate tuple")

#in non mutable operations just like strings

print("length", len(t))
print("slice", t[1:])

## TYJC
