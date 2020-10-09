# Python Refresh

- [Python Refresh](#python-refresh)
  - [String Fromatting](#string-fromatting)
  - [User Input + Int / Str](#user-input--int--str)
  - [Lists / Tuples / Sets](#lists--tuples--sets)
  - [Sets - Additional Methods](#sets---additional-methods)
  - [Booleans](#booleans)
  - [In Keyword + If Statements](#in-keyword--if-statements)
  - [Loops](#loops)
  - [List Comprehensions (gooood shortcuts)](#list-comprehensions-gooood-shortcuts)
    - [startswith()](#startswith)

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
# 24 is your shoe size?
# 24.00 is your shoe size?


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

sum(my_money)
# A reminder of the sum function >> 2441

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
---

<br>

## Booleans

<br>

The two lists below contain the same data and in the same format ```lists```. The ```is``` keyword checks if the two elements are the same thing in memory, not if they equal the same as in values.

**BUT**

The reccommended way to check values would be to use double ```==``` sign. NOT ```is```.

```py

psychology = ["jon", "sam", "steve", "rudy"]
history = ["jon", "sam", "steve", "rudy"]

print(psychology is history)
print(history is history)

# >> False
# >> True

```

<br>

---

<br>

## In Keyword + If Statements

<br>

Works in ```lists```, ```tuples``` and ```sets```. Returns a ```boolen```.

```py

history = ["jon", "sam", "steve", "rudy"]

print("jon" in history)

# >> True

---

name = "jon"

history = ["jon", "sam", "steve", "rudy"]

if name in history:
    print(f"{name} studies history")
else:
    print("no")

# >> jon studies history

```

<br>

---

<br>

## Loops

<br>

Only new idea here is to start using ```break``` in my loops.

```py

while True:
    print("something something")
    break

# prints Once instead of infinately.
  ```

```While True``` creates an infinite ```loop``` that will continue until the user or something else changes the ```boolean``` to ```False```.

This can be a pain but once the it hits a ```break```, this automatically stops the entire process and continues past this code block.

Below, usual ```foor loop``` using ```in```.

```py

history = ["jon", "sam", "steve", "rudy"]

for name in history:
    print(f"{name} studies history")

# >> jon studies history
# >> sam studies history
# >> steve studies history
# >> rudy studies history

```

---

<br>

## List Comprehensions (gooood shortcuts)

<br>

Interesting idea on making ```lists``` using calculations inside an empty brackets.

```py

nums = [20, 100, 300, 2021]

doubled = [i * 2 for i in nums]
# an empty list being filled using an equation AND a for loop

combined = sum(doubled)

print(doubled)
print(combined)

# >> [40, 200, 600, 4042]
# >> 4882

```

This is quite a useful idea. One to remember.

### startswith()

```py

friends = ["Jon", "Sam", "Steve", "Rudy"]

friends_with_S = [friend for friend in friends if friend.startswith("S")]

friends_with_J = [x for x in friends if x.startswith("J")]
# looks like first and second parameters need to be the same, then the thing i'm searching, then if statement

print(friends_with_S)
print(friends_with_J)

# >> ['Sam', 'Steve']
# >> ['Jon']

# Same seems to work with {} + ()

```
