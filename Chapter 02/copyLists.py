##GTG

# making copies in lists

first = [1, 2, 3, 4, 5]

second = first
second.append(6)

print(first)
print(second)

# now first is also changed to [1, 2, 3, 4, 5, 6] as both are refering to the same object

# to make a copy
third = second.copy()
third.append(7)

print(first)
print(second)
print(third)

##TYJC
