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
  - [Dictionaries](#dictionaries)
    - [Lists of Dictionaries](#lists-of-dictionaries)
    - [For Loops in Dictionaries / .values() .keys() / items()](#for-loops-in-dictionaries--values-keys--items)
  - [Destructuring Variables](#destructuring-variables)
  - [Functions (new)](#functions-new)
    - [Positional arguemnts](#positional-arguemnts)
    - [Default Values as Variables](#default-values-as-variables)
- [Intermediate Section.](#intermediate-section)
  - [Lambda Functions](#lambda-functions)
  - [Dictionary Comprehension (goooood / new)](#dictionarycomprehension-goooood--new)
  - [Unpacking Arguments (forgotten info)](#unpacking-arguments-forgotten-info)

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

This basically removes the need for us to do .append() where it's not absolutely necessary

---

<br>

## Dictionaries

These look a lot like objects in Javascript, but work quite differently.

Again like ```Ruby``` these are called key value pairs.

```py

friends = {"Jon" : 24, "Sam" : 36, "Steve" : 41, "Rudy" : 33}

print(friends["Jon"])
print(friends[0])

# >> 24
# >> Error

```

You can't access the elements of the ```Dictionary``` using index or bracket notation. ONLY the ```keys``` themselves can be used to access their value pair.

```py

friends = {"Jon" : 24, "Sam" : 36, "Steve" : 41, "Rudy" : 33}

friends["Simon"] = 100
friends["Simon"] = 200
# can add new elements, but only if they DON'T exist

print(friends)

# >> {'Jon': 24, 'Sam': 36, 'Steve': 41, 'Rudy': 33, 'Simon': 200}

```

### Lists of Dictionaries

You can have a list with [] and add mini dictionaries inside like an address book.

```py

address_book = [
    {"name" : "Jon", "age" : 24},
    {"name" : "Sam", "age" : 36},
    {"name" : "Steve", "age" : 41},
    {"name" : "Rudy", "age" : 33}
]

print(address_book[0]["name"])
print(address_book[2]["age"])
print(address_book["name"])

# >> Jon
# >> 41
# >> ERROR

```

You have to first locate the item in the LIST using index numbers and [] notation and THEN access the keys.

<br>

### For Loops in Dictionaries / .values() .keys() / items()

I suppose this is how we access the value - by using .items() gives us all the items in the dictionary.

But this doesn't really help with ```Lists``` of ```Dictionaries```

<br>

```py

friends = {"Jon" : 24, "Sam" : 36, "Steve" : 41, "Rudy" : 33}

for person, age in friends.items():
    print(f"{person} is {age}")

# >> Jon is 24
# >> Sam is 36
# >> Steve is 41
# >> Rudy is 33

print(friends.keys())
print(friends.values())

# >> dict_keys(['Jon', 'Sam', 'Steve', 'Rudy'])
# >> dict_values([24, 36, 41, 33])

```

<br>

---

<br>

## Destructuring Variables

Just like in the last section with .items() being used. We can destructure the tuples that are returned by looping and printing the dictionary.

```py

friends = {"Jon" : 24, "Sam" : 36, "Steve" : 41, "Rudy" : 33}

for friend in friends.items():
    print(f"{friend}")

# These are ```Tuples```
# >> ('Jon', 24)
# >> ('Sam', 36)
# >> ('Steve', 41)
# >> ('Rudy', 33)

```

Now that I have a list of Tuples which have two items inside of them, I can extract them (destructure) and assign them elsewhere.

Looping over a list of ```tuples```.
```py

friend_speeds = [("Jon", 24, "Fast"), ("Sam", 36, "Slow")]

for name, age, speed in friend_speeds:
    print(f"{name} is {age} years old and {speed}")

```
The same as Javascript, we can define the names with commas between and place the variable we are unpacking/destructuring at the end

```py

person = ("Bob", 42, "Dr")

name, _, profession = person

print(name)
print(_) # <----
print(profession

# >> Bob
# >> 42  <----
# >> Dr

```

The ```_``` still prints out the value it's assigned to but because of it's appearance, the community have decided that ```_``` is universally ignored.

So that's how we know that it's not to be used.

The ```*``` seems to act as some kind of collector, like ```rest```. 

```py

head, mid, *tail = [1, 2, 3, 4]

print(head)
print(mid)
print(tail)

# >>  1
# >>  2
# >> [3, 4]

*head, mid, tail = [1, 2, 3, 4]

print(head)
print(mid)
print(tail)

# >> [1, 2]
# >> 3
# >> 4

```

---

<br>

## Functions (new)

<br>

Something to note is not to reuse variable names even inside functions. This may be valid in other languages but not ```Python```.

```py

book_name = "Power" # <--

def read_a_book():
    book_name = book_name + "something" # <--

```

The variable scope is a little different here than JS and variables seem to be reachable in various ways inside functions. There will be a crash.

```py

read_a_book() # <-- ERROR

def read_a_book():
    print("do something")


read_a_book() # <-- Good

```

As always, make sure to define functions before you call them, and define variables before defining functions to be on the safe side.

```PASS``` means do nothing?? Need to know when to use this.

```py

book_name = "Power" # <--

def read_a_book():
    pass

```

Arguments work the same as JS

```py

def read_a_book(whichBook, when):
    print(f"start reading {whichBook} {when}")



read_a_book("Chicken Lickin", "now")

# >> Chicken Lickin now


```

### Positional arguemnts

*This seems interesting.*

It actually makes more sense this way, but maybe it's just faster to do it the other way?

```py

def find_book_quote(title, when, page):
    print(f"Go to page {page} in {title}, {when}")


find_book_quote(when="now", page="14", title="Chicken Lickin") # <-- no space before = or after

# >> Go to page 14 in Chicken Lickin now

```

So regardless of which order I pass the arguments, I'm able to specify the names of the arguments which in turn makes their position unimportant.

### Default Values as Variables

Probably bad, but new.

Haven't seen this before but could be useful. Assigning a value to a variable and then using that as a default.

This possibly makes things harder to test when you're not sure of the orig variable. Side effects possibly?

**BUT**

Reassigning the Variable after it's been used as a default, does not change the value!! Interesting.

```py

default_num = 4

def add(num1, num2=default_num):
    sum = num1 + num2
    print(sum)

add(4)

# >> 8

default_num = 10

add(4)

# >> 8 ?????!!!!

```

A good reason to not use this one. Better practice would be to define it in the function rather than using a variable.

Too risky and confusing for others.

<br>

# Intermediate Section.
All the things I don't have a clue about. Coffee break.

<br>

## Lambda Functions

<br>

Difficult to read as the program grows, maybe not to be used too much.

Doesn't have a NAME and is only used to return VALUES. They **only** RETURN values, so a return is not written, it's implicit.

```py
lambda arg1, arg2 : arg1 + arg2
```

These have no names, so you CAN assign them to variables.

```py
add = lambda arg1, arg2 : arg1 + arg2
```

```py

add = lambda arg1, arg2 : arg1 + arg2

add(4, 4)

# >> 8 ???!!!

```

They are **supposed** to be **short** and **simple** with **NO NAME**

List comprehension example with typcial ```map()``` that does the same thing, but not typically used in Python.

```py

def double(x):
    return x * 2

sequence = [1, 2, 3, 4]

doubled = [double(x) for x in sequence]

print(doubled)

doubled2 = list(map(lambda  x : x *2, sequence))

print(doubled2)

# >> [2, 4, 6, 8]
# >> [2, 4, 6, 8]

```

Have to use ```list``` to print out something readable with the ```map()``` example.

---

<br>

## Dictionary Comprehension (goooood / new)

<br>

Something that will be used quite often apparently.

```py

users = [
    (0, "Bob", "password"),
    (1, "Dave", "someg276"),
    (2, "Sam", "long687uhb"),
    (3, "Tom", "Copsm129^.")
] # List of Tuples.

username_mapping = {user[1] : user for user in users}

username_mapping = {z[1] : z for z in users} # does the same

# start dictionary with curly braces
# Define the Key then the Value
# Define where to get these two from using for loop

print(username_mapping)

# >> {'Bob': (0, 'Bob', 'password'), 'Dave': (1, 'Dave', 'someg276'), 'Sam': (2, 'Sam', 'long687uhb'), 'Tom': (3, 'Tom', 'Copsm129^.')}

print(username_mapping["Dave"])

# >> (1, 'Dave', 'someg276')


```

Destructuring from the mapping

```py

_, username, password = username_mapping["Dave"]

print(username)
print(password)

# >> Dave
# >> someg276

```

Another example using the input of the user to search through the mapped dictionary and checking their passwowrd matches what's on file.

```py

users = [
    (0, "Bob", "password"),
    (1, "Dave", "someg276"),
    (2, "Sam", "long687uhb"),
    (3, "Tom", "Copsm129^.")
] # List of Tuples.

username_mapping = {z[1] : z for z in users}

user_name_input = input("Enter username: ")
user_passw_input = input("Enter password: ")

_, username, password = username_mapping[user_name_input]
# First destructure and assign variables from mapped info
# Users input then gives me a key to search the dictionary by.

if user_passw_input == password:
    print(f"Thank you {user_name_input}, correct pw")
else:
    print(f"You're not {user_name_input} Imposter!")

```

---

<br>

## Unpacking Arguments (forgotten info)

Functions that take in any number of ```args```. As many as you want.

```py

def lots_of_args(*args):
    total = 0
    for arg in args:
        total += arg

    print(f"{total} of Everything")

lots_of_args(1, 2, 5, 100)

# >> 108 of Everything

```

Interesting unpacking / destructuring of variables.

```py

def lots_of_args(*args):
    total = 0
    for arg in args:
        total += arg

    print(f"{total} of Everything")

numbers_to_use = [20, 40, 50]

lots_of_args(*numbers_to_use)

# >> 108 of Everything

```

Even more interesting is using the ```key``` of a dictionary as the ```named arguemnt``` to pass.

```py

def lots_of_args(y, x):
    total = x * y

    print(f"{total} of Everything")

numbers_to_use = {"x" : 10, "y" : 10}

lots_of_args(**numbers_to_use)
# The ** makes this executeble

```

This one is a head trip, remembering to place the ```*``` while passing the args to a helper function ```multiply()```

```py

def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg
    
    return total


def confusion_engine(*args, operator):
# any number of args but operator
# must! be supplied as a NAMED argument
    if operator == "*":
        return multiply(*args)
        # Have to use * to pass in 4 args
        # instead of one tuple
        # Unpacking the args and passing using *
    elif operator == "+":
        return sum(args)
    else:
        return "You're doing it wrong"

print(confusion_engine(1, 2, 3, 4, operator="*"))


```

<br>