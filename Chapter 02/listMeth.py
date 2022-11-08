##GTG

# following are some list methods

num = []

# append

for i in range(1, 6):
  num.append(i)

print(num)
# now the list is 1, 2, 3, 4, 5

# remove, removes the object in the list which is has the same value as provided in the paranthesis

num.remove(1)
num.remove(5)

print(num)
# now num is 2, 3, 4

#pop, removes last element by default, if index is provided, removes the element present at the index. Also pop returns the element that is deleted

num.pop()
num.pop(1)

print(num)
# now num is 2

#extend, add the elements of the list in paranthesis to the original list

num.extend([3, 4, 5])

print(num)
# now num is 2, 3, 4, 5

# insert will insert the element before the element that is currently in that index

num.insert(0, 1)
num.insert(2, "two-and-a-half")

print(num)
#now num is 1, 2, two-and-a-half, 3, 4, 5

##TYJC
