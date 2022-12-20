## GTG

# method 1 of file processing : open -> process -> close
tasks = open("todo.txt")

for chore in tasks:
  print(chore, end = '')

tasks.close()

# method 2 of file processing : automatic context

with open("todo.txt") as tasks:
  for chore in tasks:
    print(chore, end='')


## TYJC
