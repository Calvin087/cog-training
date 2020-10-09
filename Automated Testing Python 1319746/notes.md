# Python Refresh

- [Python Refresh](#python-refresh)
  - [String Fromatting](#string-fromatting)
  - [User Input + Int / Str](#user-input--int--str)
  - [Lists / Tuples / Sets](#lists--tuples--sets)
  - [Sets - Additional Methods](#sets---additional-methods)

<br>

## String Fromatting

<br>

String formatting in Python 3.xx onwards comes with f"STRING". Giving me string interpolation. Took a while to find the settings to have code runner change the interpreter.
*Note, settings -> Search for MAP.*

```py

name = "Dave"

message = f"My name is, {name}"

print(message)

# My name is, Dave

```

Another version of this to use later is to create a template. new_message is a template which can be called again and again with different values passed in.

```py

name1 = "Bob"

new_message = "My name is {}"

with_name = new_message.format(name1)

print(with_name)

# My name is Bob
```

*fStrings* are most commonly used.

---

<br>

## User Input + Int / Str

<br>

Not forgetting that when working with user input they return strings, so we need to convert numbers into ```int``` to perform calcs and then back to ```str``` to print them out.

**BUT**

When using fStrings, it seems we don't need to go through all of those conversions.

```py

your_name = input("Type your name: ")

shoe_size = input("What is your shoe size: ")

size_int = int(shoe_size) * 2 # Calcs


print(f"{your_name} is your name")

print(f"{size_int} is your shoe size?")

print(f"{size_int:.2f} is your shoe size?")  # 2 Decimal places added / inline float conversion?

# Dave is your name
# 12 is your shoe size?


```

---
<br>

## Lists / Tuples / Sets

<br>

```py
lists = ["Dave", "Sam", "Chicken"]
# Can add and remove elements.
# Maintain Order
# [] notation available
# lists[0] = "Dog" >> modifies
# append() remove()

tuples = ("Dave", "Sam", "Chicken")
# Can NOT add and remove elements
# Maintain Order
# [] notation available

sets = {"Dave", "Sam", "Chicken"}
# Can add and remove but can't have DUPES
# No order so no [] targeting
# Can not reassign values
# .add() only once on a DUPE
```
---
<br>

## Sets - Additional Methods

<br>

```py
friends = {"Dave", "Sam", "Pete"}
abroad = {"Dave", "Pete"}

invite_for_drinks = friends.difference(abroad)
invite_for_drinks1 = abroad.difference(friends) # returns nothing

print(invite_for_drinks)
print(invite_for_drinks1)

# >> {'Sam'}
# >> set()

---

my_money = {20, 100, 300, 2021}
her_money = {20, 400, 2300}

together = my_money.union(her_money)
# merges both together but removes DUPES

print(together)

# >> {400, 100, 2021, 20, 2300, 300}

---

art = {"jon", "sam", "steve", "rudy"}
science = {"jon", "anne", "steve", "rudy"}

both = art.intersection(science)

print(both)

# >> {'steve', 'jon', 'rudy'}

```



