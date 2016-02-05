#!/usr/bin/env python

# 3-1 - 3-3
born_year = 1989
years_list = []
for y in range(6):
    years_list.append(born_year + y)

print(years_list)
print("I was three years old at", years_list[3])
print("I was most old at", years_list[-1])

# 3-4 - 3-7
things = ["mozzarella", "cinderlla", "salmonella"]
print(things)
things[1] = things[1].capitalize()
things[0] = things[0].upper()
del things[2]
print(things)

# 3-8 - 3-9
surprise = ["Groucho", "chico", "Harpo"]
print(surprise)
print(surprise[-1].lower()[-1::-1].capitalize())

# 3-10 - 3-14
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}
print(e2f)
print(e2f["walrus"])
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)
print(f2e["chien"])
print(set(e2f.keys()))

# 3-15 - 3-18
life = {
    "animals": {},
    "plants": {},
    "other": {}
}
life["animals"] = {
  "cats": ["Henri", "Grumpy", "Lucy"],
  "octopi": {},
  "emus": {}
}
print(life)
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])
