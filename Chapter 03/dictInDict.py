##GTG

# putting a dictionary inside a dictionary

import pprint

people = {}

people["ford"] = {
  "Occupation" : "Researcher",
  "Gender" : "Male",
  "Home Planet" : "Betelguese Seven",
  "Name" : "Ford Perfect",
}


people["Arthur"] = {
  "Occupation" : "Sandwich-Maker",
  "Gender" : "Male",
  "Home Planet" : "Earth",
  "Name" : "Arthur Dent",
}

people["Trillian"] = {
  "Occupation" : "Mathematician",
  "Gender" : "Female",
  "Home Planet" : "Earth",
  "Name" : "Tricia McMillan",
}

people["Robot"] = {
  "Occupation" : "Paranoid Android",
  "Gender" : "Unknown",
  "Home Planet" : "Unknown",
  "Name" : "Marvin",
}

pprint.pprint(people)
##TYJC
