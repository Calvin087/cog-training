# Python Refresh

- [Python Refresh](#python-refresh)
  - [Bug Tracking](#bug-tracking)
  - [String Fromatting](#string-fromatting)
  - [User Input + Int / Str](#user-input--int--str)
  - [Lists / Tuples / Sets](#lists--tuples--sets)
  - [Numbers, shuffle, randint](#numbers-shuffle-randint)
  - [Sets - Additional Methods](#sets---additional-methods)
  - [Booleans](#booleans)
  - [In Keyword + If Statements](#in-keyword--if-statements)
  - [Loops](#loops)
      - [Enumerate loop](#enumerate-loop)
      - [Zipping lists together](#zipping-lists-together)
      - [Tuple unpacking with Loops](#tuple-unpacking-with-loops)
  - [List Comprehensions (gooood shortcuts)](#list-comprehensions-gooood-shortcuts)
    - [startswith()](#startswith)
  - [Dictionaries](#dictionaries)
    - [Lists of Dictionaries](#lists-of-dictionaries)
    - [For Loops in Dictionaries / .values() .keys() / .items()](#for-loops-in-dictionaries--values-keys--items)
      - [continue:](#continue)
  - [Dictionary value checks](#dictionary-value-checks)
  - [Destructuring Variables](#destructuring-variables)
  - [Functions](#functions)
    - [Positional arguemnts](#positional-arguemnts)
    - [Default Values as Variables](#default-values-as-variables)
    - [Map(), Fiter(), Zip(), Reduce()](#map-fiter-zip-reduce)
  - [Generator Functions](#generator-functions)
  - [Ternary Operators](#ternary-operators)
- [DocStrings on Functions](#docstrings-on-functions)
- [Object Oriented Programming (refresher)](#object-oriented-programming-refresher)
      - [Object.methods()](#objectmethods)
    - [Magic Methods ```__str__``` / ```__repr__``` / ```__len__```- Object representation](#magic-methods-__str__--__repr__--__len__--object-representation)
    - [@ClassMethods / @StaticMethods (research more)](#classmethods--staticmethods-research-more)
      - [Class methods expanded](#class-methods-expanded)
    - [Inheritance (used less than composition)](#inheritance-used-less-than-composition)
    - [Class Composition (used more often than inheritance)?](#class-composition-used-more-often-than-inheritance)
  - [Private Methods](#private-methods)
- [Date and Time](#date-and-time)
- [Intermediate Section.](#intermediate-section)
  - [Lambda Functions / map(), filter()](#lambda-functions--map-filter)
      - [map()](#map)
      - [filter()](#filter)
  - [Dictionary Comprehension (goooood / new)](#dictionarycomprehension-goooood--new)
  - [Unpacking Arguments (forgotten info)](#unpacking-arguments-forgotten-info)
  - [Unpacking Keyword Arguments (new)](#unpacking-keyword-arguments-new)
  - [Type Hinting](#type-hinting)
  - [Imports](#imports)
      - [name / main](#name--main)
    - [Relative Imports](#relative-imports)
  - [Errors in Python (try / except)](#errors-in-python-try--except)
    - [Custom Error Classes](#custom-error-classes)
    - [Debugging ```__Trace__```](#debugging-__trace__)
  - [First Class Functions (Important)](#first-class-functions-important)
  - [Decorators in Python (more research)](#decorators-in-python-more-research)
  - [@ Decorator syntax (more research + links)](#-decorator-syntax-more-research--links)
  - [Mutability in Python and default parameters](#mutability-in-python-and-default-parameters)
    - [Default Params.](#default-params)
- [Modules](#modules)
- [Working With Files](#working-with-files)
    - [opening, reading, closing](#opening-reading-closing)
    - [with & as while working with files](#with--as-while-working-with-files)
    - [Methods that SAVE to csv](#methods-that-save-to-csv)
    - [Methods that LOAD from csv](#methods-that-load-from-csv)
    - [Methods that SAVE to JSON (better)?](#methods-that-save-to-json-better)
    - [Methods that LOAD from csv](#methods-that-load-from-csv-1)
    - [JSON *args **kwargs - Useful!](#json-args-kwargs---useful)
- [Working With Directories](#working-with-directories)
- [Working With Regular Expressions - more in another file](#working-with-regular-expressions---more-in-another-file)



Todo List
- Add GitBash to windows so that I can use familiar commands
- Look at the [windows terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab) instead maybe??

<br>

## Bug Tracking

<br>

Allows me to insert bug tracking. While a failure occurs i'm able to check the values of variables to see what's going wrong. Probably much faster than printing all the time.

```py

import pdb

pdb.set_trace()

# Use 'step' to move to next line, continue to move to next error, 'a' to see all values

```

--------------

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

```py

def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

print(hello("Dave"))
# >> Hello, Dave!

print(hello())
# >> Hello, World!

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

## Numbers, shuffle, randint

<br>

Same old, but didn't know you can import random integers and shuffles.

```py

from random import shuffle

sdf = [1, 2, 3, 5, 6, 7]
shuffle(sdf)
print(sdf)

# >> [1, 3, 2, 5, 7, 6]
# >> [2, 3, 1, 5, 6, 7]
# >> [2, 6, 7, 5, 1, 3]
# >> [6, 5, 7, 3, 2, 1]


pop = randint(0,100)

print(pop)

# >> 93
# >> 62
# >> 78

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

---

# Creating a unique selection

dupes = [1, 2, 2, 2, 2, 3, 4, 5, 6, 6, 6, 6]

de_dupe = set(dupes)

print(de_dupe)

# >> {1, 2, 3, 4, 5, 6}

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

#### Enumerate loop

seems to be able to pull out the index as well as the char/int.

```py

my_string = "Stand"

for i, letter in enumerate(my_string):
    if letter == ' ':
        continue
    print(f"something {i}, and then {letter}")

# >> something 0, and then S
# >> something 1, and then t
# >> something 2, and then a
# >> something 3, and then n
# >> something 4, and then d

```

#### Zipping lists together

```py

my_string = [1, 2, 3]
my_list = ['a', 'b', 'c']

for item in zip(my_string, my_list):
    print(item)


# >> (1, 'a')
# >> (2, 'b')
# >> (3, 'c')

# Will only go as far as the shortest list

my_string = [1, 2, 3]
my_list = ['a', 'b', 'c']

pop = list(zip(my_string, my_list))

print(pop)

# > [(1, 'a'), (2, 'b'), (3, 'c')]

```

#### Tuple unpacking with Loops

```py

list_of_tups = [(1,2), (3,4), (5,6), (7,8), (9,10)]

for tup1, tup2 in list_of_tups:
    print(str(tup1) + ' then print ' + str(tup2)) 


# >> 1 then print 2
# >> 3 then print 4
# >> 5 then print 6
# >> 7 then print 8
# >> 9 then print 10

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

# List comprehension and Loops

squares = [x for x in range(1,10)]

print(squares)

squares_2 = [x * 2 for x in range(1,10)]

print(squares_2)

# >> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >> [2, 4, 6, 8, 10, 12, 14, 16, 18]


# List comp + loops + if

squares = [a for a in range(1,20) if a % 2 == 0]

print(squares)

# >> [2, 4, 6, 8, 10, 12, 14, 16, 18]

```

Exercises

```py

my_string = 'Secret agents are super good at staying hidden'

for word in my_string.split():
    if word[0] == 's' or word[0] == 'S':
        print(word)

# >> Secret
# >> super
# >> staying

code = [x[0] for x in my_string.split()]

print(code)

# >> ['S', 'a', 'a', 's', 'g', 'a', 's', 'h']

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

First of all we can create a new dict on the fly

```py

user1 = dict(name = "calvin")

print(user1["name"])

# >> calvin

""

```

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

### For Loops in Dictionaries / .values() .keys() / .items()

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

Checking if values exist

```py

friends = {"Jon" : 24, "Sam" : 36, "Steve" : 41, "Rudy" : 33}

print("Jon" in friends)
print(24 in friends.values())
print("Sam" in friends.keys())

# >> True
# >> True
# >> True

```

Updating a key

```py

friends = {"Jon" : 24, "Sam" : 36, "Steve" : 41, "Rudy" : 33}

print(friends.update({"Jon" : 100}))
# >> {'Jon': 100, 'Sam': 36, 'Steve': 41, 'Rudy': 33}

```

#### continue:

```py

for person, age in friends.items():
    if person == "Jon":
        continue

    print(f"{person} is {age}")

# >> Sam is 36
# >> Steve is 41
# >> Rudy is 33

```

<br>

---

<br>

## Dictionary value checks

<br>

If I don't know if a dictionary has a certain value, I can either check or create it on the fly with a default.

```py

friends = {"Jon" : 24, "Sam" : 36, "Steve" : 41, "Rudy" : 33}

print(friends.get("Francis", 22))

```

If Francis exists, it will grab it from the dictionary, but if it doesn't exist, it will return my new value as a default.

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

## Functions

<br>

As always, make sure to define functions before you call them, and define variables before defining functions to be on the safe side.

```py

read_a_book() # <-- ERROR

def read_a_book():
    print("do something")


read_a_book() # <-- Good

```

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


### Map(), Fiter(), Zip(), Reduce()

Again, this sounds familiar. Map() calls the function that I pass it, so I don't have to. The second argument are the values to be mapped over.

It also doesn't affect the original variable. No side effects. It returns a new object instead of mutating the original.

**Map()**

```py

def multi_by_2(item):
    return item * 2

print(list(map(multi_by_2, [1, 2, 3])))

# >> [2, 4, 6]

# ----------------

my_list = [1, 2, 3]

def multi_by_2(item):
    return item * 2

print(list(map(multi_by_2, my_list)))
print(my_list)

# >> [2, 4, 6] - new.
# >> [1, 2, 3] - old remains the same.

```

Filter returns the values that are true.

**Filter()**

```py

my_list = [1, 2, 3, 4, 5, 6, 7]

def only_odd_nums(item):
    return item % 2 != 0

print(list(filter(only_odd_nums, my_list)))
print(my_list)

# >> [1, 3, 5, 7]
# >> [1, 2, 3, 4, 5, 6, 7]

# -------------------

names = ["dave", "dani", "sam", "tom"]

def names_with_d(item):
    return item.startswith("d")

print(list(filter(names_with_d, names)))
print(names)

# >> ['dave', 'dani']
# >> ['dave', 'dani', 'sam', 'tom']

```

**Zip()**

Zips together any iterables into tuples by index

```py

nums1 = [1, 2, 3]
nums2 = [10, 20, 30] # List
nums3 = (100, 200, 300) # Tuple

print(list(zip(nums2, nums3)))

# >> [(1, 10), (2, 20), (3, 30)]
# >> [(10, 100), (20, 200), (30, 300)]

# --------------------

nums = (100, 200, 300) # Tuple
names = ["Dave", "Sandy", "Tommy"] # List

print(list(zip(nums, names)))

# >> [(100, 'Dave'), (200, 'Sandy'), (300, 'Tommy')]

```

**Reduce()** - More Research

Have to import Reduce. First we need a function, then the data AND some kind of intial value. Apparently really useful and popular in the community with advanced programmers. Still not entirely sure of it's utility.

```py

from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

def accumulate(acc, item):
    return acc + item

print(reduce(accumulate, nums, 0))

# >> 21

```

---

<br>

## Generator Functions

<br>

Yield is something new here. Seems to save on memory by not running the complete function. You can continue the function by using next(function_name()) It also seems to hold the value in memory until it's called again.

Really good for speed and memory storage.

```py

def generator_function(num):
    for i in range(num):
        yield i

run_g = generator_function(10)
print(next(run_g)) # 0
print(next(run_g)) # 1
print(next(run_g)) # 2

# -----------------------------

def generator_function(num):
    for i in range(num):
        yield i

for item in generator_function(100):
    print(item)

```

```py

def fibonacci(num):
    num_a = 0
    num_b = 1
    for i in range(num):
        yield num_a
        temp = num_a
        num_a = num_b
        num_b = temp + num_b

for x in fibonacci(10):
    print(x)

```

---

<br>

## Ternary Operators

<br>

Something that I've forgotten to use while doing code wars if ternaries.

```py

# something if true IF condition ELSE condition if else

is_friend = True

can_message = "message allowed" if is_friend else "not allowed"

print(can_message)


```

---

<br>

# DocStrings on Functions

<br>

These seem pretty cool. Able to get some helper info on functions when called in a certain way.

```py

def killAllHumans(word):
    '''
    This function prints {word}
    In this space I can write comments and have them returned.
    '''
    return word

print(killAllHumans.__doc__)

# >> This function prints {word}
# >> In this space I can write comments and have them returned.

```

---

<br>

# Object Oriented Programming (refresher)

<br>

To make life easier, we make objects/classes. We can add methods to these objects to make the code look cleaner for human legibility.

It looks like we can store tuples inside the objects/classes also.

```py

class Student:
    
    # Class object attribute.
    # Available but not normal

    school = "Stanley Tech"

    def __init__(self, name, grades):
        self.name = name # indentation is important here also.
        self.grades = grades


cally = Student("Cally", (1,2,3,4,5))

print(cally.name)
print(cally.grades)
print(cally.school)

# >> Cally
# >> (1, 2, 3, 4, 5)
# >> Stanley Tech

```

#### Object.methods()

```py

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self): # always takes self
        return sum(self.grades) / len(self.grades)


cally = Student("Cally", (1,2,3,4,5))

print(cally.average) # stupid mistake, I activated the method but didn't call it.
print(cally.average()) # you have to call the class methods for them to run correctly ie: with "()"

# >> <bound method Student.average of <__main__.Student object at 0x10b658fa0>> <-- INCORRECT

# >> 3.0 <-- CORRECT    

```

---

<br>

### Magic Methods ```__str__``` / ```__repr__``` / ```__len__```- Object representation

<br>

Using the class from the last example, simply trying to print the info doesn't bring back anything that is useful for a human.

```py

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self): # always takes self
        return sum(self.grades) / len(self.grades)


cally = Student("Cally", (1,2,3,4,5))

print(cally)

# >> <__main__.Student object at 0x107588fa0>

```

Apparently Magic Methods allows us to get around this. ```__str__``` allows us to convert our method into a string representation.

```py

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return f"Student: {self.name}'s grades are {self.grades} which average out to {self.average()}"
        # turns out we can print functions inside strings!
        # Notice that I'm not calling Print()
        # I'm only printing the "Cally" child object.
        # This prints by default
    
    def average(self): # always takes self
        return sum(self.grades) / len(self.grades)


cally = Student("Cally", (1,2,3,4,5))

print(cally)

#  >> Student: Cally's grades are (1, 2, 3, 4, 5) which average out to 3.0

```

The ```__repr__``` method gives us another string type, that allows us to read and replicate the contents and layout of an object. NOT entirely sure the use of this yet.

```py

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __repr__(self):
        return f"<Student({self.name}, {self.grades})>"

cally = Student("Cally", (1,2,3,4,5))

print(cally)

# >> <Student(Cally, (1, 2, 3, 4, 5))>

```

The ```__len__``` method gives us another string type.

```py

class Student:
    def __init__(self, name, grades, height):
        self.name = name
        self.grades = grades
        self.height = height

    def __repr__(self):
        return f"<Student({self.name}, {self.grades})>"

    def __len__(self):
        return self.height

cally = Student("Cally", (1,2,3,4,5), 177)

print(len(cally))

# >> 177

```

---

<br>

### @ClassMethods / @StaticMethods (research more)

<br>

- **Instance methods** are used for most things. When you want to produce an action, using the data inside the object. Also if you want to call something to modify the data inside the ```self```.

- **Class** are used as **Factories** *(what?)*

- **Static** is just to place / organise methods (not used as much as the other two).

```py

class ClassTest:
    # classes don't always need init if you have nothing to instantiate.

    def instance_method(self):
        print(f"Called instance method of {self}")

    @classmethod
    def class_method(cls): # common practice to name param as "cls"
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method(): # Don't receive anything 
        print(f"Called static_method and it's boring")


Tally = ClassTest()


Tally.instance_method()
Tally.class_method() # automatically passes itself as a param
Tally.static_method()

# >> Called instance method of <__main__.ClassTest object at 0x10617bee0>
# >> Called class_method of <class '__main__.ClassTest'>
# >> Called static_method and it's boring

```

<br>

#### Class methods expanded

<br>

Looks like I can use these methods inside the class, without making a new object.

Allows me to assign various parts of a new object without it being passed in. All I have to do is call the correct method while making the new object and the ```@classmethod``` assigns things using the data stored within the class.


```py

class Book:
    TYPES = ("hardcover", "paperback")
    # Data stored in a class / organisation reasons

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book Title: {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 100)
        # cls refers to Book. ie: Book(name, ...)
        # cls refers to Book. ie: cls(name, ...) = same thing as above

    # This is using an internal method to create a new object.
    # Automatically assigns "Hardcover" to the new object I'm tying to
    # create outisde of this class ie: new_book.

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight + 50)


hard_book = Book.hardcover("Power",  1300)
# Only two arguments have been passed on to this,
# but the result is that it has been assigned hardcover using the 
# @classmethod of .hardcover.

light_book = Book.paperback("Python 101",  1000)

print(hard_book)
print(light_book)

# >> <Book Title: Power, hardcover, weighing 1400g>
# >> <Book Title: Python 101, paperback, weighing 1050g>

```

<br>

### Inheritance (used less than composition)

<br>

Super is what is used to call / copy all the functionality from the Parent class to be used in the child class

```py

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device: {self.name!r} ({self.connected_by})"
        # !r prints out the __repr__ version of the name
    
    def disconnected(self):
        self.connected = False
        print("discconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity): # All the same +1
        super().__init__(name, connected_by)
            # Gets / copies the parent class
        self.capacity = capacity
        self.remaining_pages = capacity
            # Adding our own unique setters

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining.)"

    def print(self, pages):
        if not self.connected:
            print("Printer is not connected")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages

printer = Printer("Printer", "USB", 500)
print(printer.print(20))
print(printer)
printer.disconnected()
print(printer.print(20))

# >> Printing 20 pages.
# >> None <--- Why is this happening
# >> Device: 'Printer' (USB) (480 pages remaining.)
# >> discconnected
# >> Printer is not connected
# >> None <--- Why is this happening

```

---

<br>

### Class Composition (used more often than inheritance)?

<br>

Typically with inheritance, we're treating it like evolutionary inheritance. As if the ```child``` is the same and something more than the ```parent```. All tigers are mammals but not all mammals are tigers.

There's no reason to inherit things if they're not going to be used.

With composition, I've created a class that accepts and organises other class objects, the same way a bookshelf organises books.

```py

class Bookshelf:
    def __init__(self, *books):
        # Accepts a number of books, not only one at a time
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book Title: '{self.name}'"


power = Book("Power")
ttown = Book("Toy Town")
shelf = Bookshelf(power, ttown)

print(power)
print(ttown)
print(shelf)
print(shelf.books) # Gives me all books on bookshelf

# >> Book Title: 'Power'
# >> Book Title: 'Toy Town'
# >> Bookshelf with 2 books.
# >> (<__main__.Book object at 0x107b65fa0>, <__main__.Book object at 0x107b65e80>) <-- What do i even do with this??

```

---

<br>

## Private Methods

<br>

Methods within objects that you don't want to be avaialable to users etc.

```py

def _private_method(self):
    print("Private Method")
    
    # The underscore makes it private but doesn't really hide it just guides people away from using it.

```
<br>

# Date and Time

<br>

```py

import datetime

time = datetime.time(1,14,4,1)

print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)

past = datetime.date(2018,10,11)
today = datetime.date.today()
right_now = datetime.datetime.now()

print(right_now)

```
**Cheap speed test**

```py
before = datetime.datetime.now()

test = [x ** 2 for x in range(100)]

after = datetime.datetime.now()

diff = after - before

print(diff)
```

---

<br>

# Intermediate Section.
All the things I don't have a clue about. Coffee break.

<br>

## Lambda Functions / map(), filter()

<br>

Difficult to read as the program grows, maybe not to be used too much.

Doesn't have a NAME and is only used to return VALUES. They **only** RETURN values, so a return is not written, it's implicit.

```py
lambda arg1, arg2 : arg1 + arg2
```

These have no names, so you CAN assign them to variables.

```py

add = lambda arg1, arg2 : arg1 + arg2

add(4, 4)

# >> 8 ???!!!

```

```py
times_200 = lambda num : num * 200

print(times_200(2))

#>> 400

```

```py

my_list = [2, 4, 5]

code = list(map(lambda x : x ** 2, my_list))

print(code)

# >> [4, 16, 25]

```

```py

code = list(filter(lambda x : x % 2 == 0, [1, 3, 10, 2, 4, 5]))

print(code)

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

#### map()

```py

my_nums = [1, 2, 3, 4, 5]

def square(num):
    return num ** 2

for item in map(square, my_nums):
    # Needs Two Functions
    # We also don't call the function being
    # passed because Map is doing that already
    print(item)

# >> 1
# >> 4
# >> 9
# >> 16
# >> 25

mapped = list(map(square, my_nums))

print(mapped)

# >> [1, 4, 9, 16, 25]

```

#### filter()

```py

my_nums = [1, 2, 3, 4, 5, 10, 100]

def check_even(num):
    return num % 2 == 0

filtered = list(filter(check_even, my_nums))

print(filtered)

# >> [2, 4, 10, 100]

```

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

# >> 24

```

<br>

---

<br>

## Unpacking Keyword Arguments (new)

<br>

Looks like we're able to create dictionaries using an undefined number of named arguments.

```py

def named(**kwargs): # Double ** to start this.
    print(kwargs)

named(name="Cally", age=100)

# >> {'name': 'Cally', 'age': 100}

```
We can do this in the opposite direction as well.

```py

def named_it(name, age, style): # Double ** to start this.
    print(name, age, style)

details = {"name" : "Cally", "age" : 100, "style" : "no-style"}

named_it(**details)

# >> Cally 100 no-style

```

```py

def named(**kwargs): # Double ** to start this.
    print(kwargs)

details = {"name" : "Cally", "age" : 100, "style" : "no-style"}

named(**details)

# >> {'name': 'Cally', 'age': 100, 'style': 'no-style'}

```
Unpacking and repacking. Looping over a packed dictionary. If you're using the Double ```**```, you have to pass a ```Dictionary```. Passing anything else will give an error.

```
function(**"Calvin") # >> ERROR
function(**None) # >> ERROR
```

```py

def named(**kwargs): # just to print an example first
    print(kwargs)

def print_nice(**kwargs):
    named(**kwargs) # just to show the original print style
    for arg, value in kwargs.items():
        print(f"\n {arg}: {value} \n") # shows the print style when looping with line breaks.

details = {"name" : "Steven", "age" : 200, "style" : "mad-style"}

print_nice(name="calvin", age=100, style="no-style")
print_nice(**details)

# >> {'name': 'calvin', 'age': 100, 'style': 'no-style'}

# >>  name: calvin 
# >>  age: 100 
# >>  style: no-style 

# >> {'name': 'Steven', 'age': 200, 'style': 'mad-style'}

# >>  name: Steven 
# >>  age: 200 
# >>  style: mad-style

```


---

<br>

## Type Hinting

<br>

Should probably look for a more in depth discussion about this as it's similar to Typescript for Javascript, which I need to learn.

You can import hinting modules that tell you whether you're passing incorrect types to functions ie: tuples, lists, strings.

```py



```

---

<br>

## Imports

<br>

#### name / main

```py
if __name__ == "__main__":
    run() # main function goes here.
```

```__name__``` is a global variable that changes depending on which file you're in. ```Sys``` allows me to see all the paths in my current folder and any things i have been imported at the top of the file.

Also to remember, imported files are run back to front. So the file I'm in gets run last and the import runs before hand.

So if have 3 files are importing from each other, the final one prints first, then they all run in reverse order.

```py

import sys

print(sys.path)

## >> '/Users/calvin/Documents/GitHub/cog-training/Automated Testing Python 1319746', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', '/Users/calvin/Library/Python/3.9/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages'


```

<br>

### Relative Imports

<br>

This apparently isn't really used but causes problems for noobs. You can only do relative imports when they're in a folder / denoted with a folder name by a (```.```) libraries.modules.

**Basically DON'T DO THIS** It seems annoying and messy.

```py
from .mymodule import xyz # <-- relative import, has to be in same folder...
from mymodule import xyz
```

---

<br>

## Errors in Python (try / except)

<br>

Using try / catch when sending info to functions can help to stop things breaking down later. Although I don't think it gives you a traceback so you can't see where exactly things broke down. Maybe later.

I guess good practice to place errors in the maths of the functions as well as catch it before it gets sent to the function - as below.

```py

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")
        # concerned with not dividing by 0
    
    return dividend / divisor

grades = []

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(e) # prints out more info
    print("There are no grades in your list.")
    # concerened with not allowing 0 into the function.
else:
    print(f"The average grade is {average}")
finally:
    print("This runs regardless of errors")

# >> Divisor cannot be 0
# >> There are no grades in your list.
# >> This runs regardless of errors

```

---

<br>

### Custom Error Classes

<br>

Most of the time you don't need to put anything inside the error classes, but you can if you want to get a little more advanced, but just giving them a new name is good enough most of the time.

```py

class TooManyPagesReadError(ValueError):
    # Creating my own error which inherits from the ValueError
    # Copy of ValueError, just with a different name
    pass


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
            )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read too many pages"
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")


new_book = Book("Power", 30)
new_book.read(30)
new_book.read(40)

# >>    new_book.read(40)
# >>     raise TooManyPagesReadError(
# >> __main__.TooManyPagesReadError: You tried to read too many pages

```

Here's a prettier way of displaying errors for users, by passing the error as ```e```.

```py

try:
    new_book = Book("Power", 30)
    new_book.read(30)
    new_book.read(40)
except TooManyPagesReadError as e:
    print(e)

# >> You have now read 30 pages out of 30
# >> You tried to read too many pages

```

---

<br>

### Debugging ```__Trace__```

<br>

We're able to stop the program in the middle of it's operations and play around in the shell to see what's going on.

```py

import pdb

pdb.set_trace()
# place this in the suspected area to check current variable types etc


```



---

<br>

## First Class Functions (Important)

<br>

Functions saved as variables, used as you would any other variable.

```py

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Div cannot be 0")

    return dividend / divisor

def calculate(*values, operator):
    # any number of values / unpacking
    return operator(*values)
    # passing a function as a parameter

result = calculate(20, 5, operator=divide)
    # the operator is not called using (),
    # it's simply passed and called later inside calculate

print(result)

# >> 4.0

```

Another example of passing functions, but this time we don't name it.

```py

def search(sequence, expected, finder):
    # list of dictionaries as seq
    # expected is a str
    # finder is really get_friend_name("Sam") is a passed function
    for elem in sequence:
        if finder(elem) == expected:
        # get_friend_name("Sam") = "Sam"
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")

friends = [
    {"name": "Dave", "age" : 30},
    {"name": "Sam", "age" : 27},
    {"name": "Tom", "age" : 41}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Sam", get_friend_name))
print(search(friends, "Dave", lambda friend : friend["name"]))
# lambda = unnamed function, friend is argument, return friend ["name"]
# Exactly the same as the print above it.

# >> {'name': 'Sam', 'age': 27}
# >> {'name': 'Dave', 'age': 30}

```

---

<br>

## Decorators in Python (more research)

<br>

First class functions to replace the values of other functions.....

```py

user = {"username" : "Cally", "access_level": "admin"}

def my_pass():
    return "1234"

def make_secure(func):
    def secure_function():
    # We're not calling secure_function, it seems to run just because
    # It's inside a running function already.
        if user["access_level"] == "admin":
            return func()
        else:
            return f"no admin access for {user['username']}"
    
    return secure_function
    # We're only returning the value of the already running secure_function

get_admin_password = make_secure(my_pass)
# This variable is equal to a function, so we can call it as a function.
# AKA First Class Function
# We're replacing get_admin_p with a secure function after checking.

print(get_admin_password())

```

---

<br>

## @ Decorator syntax (more research + links)

<br>

Links:
- [DataCamp Tuts](https://www.datacamp.com/community/tutorials/decorators-python)
- [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [Video on Decorators](https://www.youtube.com/watch?v=MYAEv3JoenI&ab_channel=howCode)

Placing the ```@``` above a function stops it from being used before it's supposed to be and sends it through the function defined with the ```@```. This however changes the name of the function inside python's brain to the name of the ```@ function```. To prevent this and keep the old name in memory, we need to import ```functools```.

```@functools.wrap``` tells the function that it's a wrapper for something else. This helps with tracebacks and avoids confusions with name changes.

```py

import functools

user = {"username" : "Cally", "access_level": "admin"}

def make_secure(func):
    # @ Tells python that secure is just a wrapper, maintain orig names.
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"no admin access for {user['username']}"
    
    return secure_function

# @ sends this to make secure immediately, effectively REPLACING with make_secure()
@make_secure
def my_pass():
    return "1234"

print(my_pass())

```

By default it's difficult to use paremeters on functions that have been decorated. It binds the two functions and stops them from being used elsewhere because of the specific nature that the parameters force them into.

To avoid this we can using the unpacking and unlimited params techniques ```*args + **kwargs```.

```py

import functools

user = {"username" : "Cally", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"no admin access for {user['username']}"
    
    return secure_function

@make_secure
def my_pass(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password."

print(my_pass("billing"))

```

Factory creates a place to CREATE Decorators **(MORE REASEARCH NEEDED)**

```py

import functools

user = {"username" : "Cally", "access_level": "guest"}

def make_secure(access_level):
    # FACTORY used to create decorators
    
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"no {access_level} access for {user['username']}"
        
        return secure_function

    return decorator

@make_secure("admin")
def my_pass():
    return "1234"

@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"

print(my_pass())
print(get_dashboard_password())

# >> no admin access for Cally
# >> user: user_password

user = {"username" : "Dave", "access_level": "admin"}

print(my_pass())
print(get_dashboard_password())

# >> 1234
# >> no guest access for Dave

```

---

<br>

## Mutability in Python and default parameters

<br>

Everything is mutable unless...they are ```tuples```, ```int```, ```floats```, ```strings```, ```booleans```

### Default Params.

<br>

NEVER make a default param a mutable value. In the example below. Sam did not take an exam and should not have a grade assigned. However when the program runs, Sam has the same grades as Bob (student1).

```py

from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = []):
        # BAAAAAAD
        # second student grades are the same as student 1 (copied)
        self.name = name
        self.grades = grades

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
sam = Student("Sam")
bob.take_exam(99)

# no exam for sam

print(bob.grades)
print(sam.grades)

# >> [99]
# >> [99] <-- This should be an empty list

```

Giving the mutable area a value of ```None``` at first and then allowing it to be assigned in the setters.

If you want to use defaults, use ```tuples```, ```int```, ```floats```, ```strings```, ```booleans```

```py

from typing import List

class Student:
    def __init__(self, name: str, grades: List[int] = None):
        # assigning NONE at first and then below giving the option of list
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student("Bob")
sam = Student("Sam")
bob.take_exam(99)

# no exam for sam

print(bob.grades)
print(sam.grades)

# >> [99]
# >> []

```

---

<br>

# Modules

<br>

asdasdasd

---

<br>

# Working With Files

<br>

**Checking if a file exists**

```py

import os

def file_exists(filename):
    return os.path.isfile(filename)

```

This text file is in the same directory as the script. Took a few seconds for it to be able to index it before being able to read it without errors.

> **Seeker**

There's a an invisible cursor that moves through the file after a read, this needs to be reset otherwise reading again will print a blank statement.

**BUT** not sure where this happens though because the terminal and VSCode both automatically seem to reset the seeker?

### opening, reading, closing

```py

my_file = open('test.txt')

print(my_file.read())

my_file.seek(0) # nothing
print(my_file.readlines()) # again nothing, probably a notebook feature.

# >> My lovely text file has nothing inside it.

my_file.close() # When you're done!

```

Executing code on a file as if we're making a function using ```with``` and ```as```. This also automatically **CLOSES** the file once executed.

### with & as while working with files

```py

# Reading
with open('test.txt', mode='r') as my_file:
    print(my_file.read())

```

Each time we write to a file, the cursor resets and starts writing from the beginning. 

__w__ overwrites everything and starts writing. **IF** the file doesn't exist, __W__ creates a new file and saves it.

```py

with open('test.txt', 'w') as f:
    f.write("hello world")

```

__r+__ resets the cursor and starts writing.


```py

# Reading & Writing
with open('test.txt', mode='r+') as my_file:
    text = my_file.write("Hey it's me")
    print(my_file.read())

```

Append to file

```py

# Reading & Writing
with open('test.txt', mode='a') as my_file:
    text = my_file.write("Hey it's me")
    print(my_file.read())

```

Errors finding files

```py

try:
    with open('test.txt', mode='a') as my_file:
        text = my_file.write("Hey it's me")
        print(my_file.read())
except FileNoteFouncError:
    print("Something here")

```

### Methods that SAVE to csv

```py

def save_to_file(self):
    with open(f"{self.name}.txt", 'w') as f: # File is named as the user's name
        f.write(self.name + "\n" )

        for movie in self.movies:
            f.write(f"{move.name},{movie.genre},{str(movie.watched)} etc '\n'")
            # self.movies.watched is a Boolean so have to string it.

```

### Methods that LOAD from csv

Could possibly just use [the module ```csv```](https://www.youtube.com/watch?v=W7QByFjVom8&ab_channel=teclado) instead. csv.writer etc

```py

# a method on User, not really referencing the individual user themselves
@classmethod
def load_from_file(cls, filename):
    with open(filename, 'r') as f:
        content = f.readlines() # returns a LIST of file content
        user_name = content[0]
        movies = []

        for line in content[1:]:
            data = line.split(',') # we split because data was saved as {},{},{}
            movies.append(Movie(data[0], data[1], data[2] == "True"))
            # [2] is a string of a Bool, so we == to return a bool from STR
            # creating new Movie object

        user = cls(user_name)
        user.movies = movies
        return user

        # --------------

uesr = User.load_from_file('calvin.txt')
print(user.name)
print(user.movies)


```

### Methods that SAVE to JSON (better)?

Basically a Python dictionary with lists in it. JSON supports ```Booleans```.

```py

# On Movie Class
# Just returns a dictionary

    # def m_json(self):
    #     return {
    #         'name': self.name,
    #         'genre': self.genre,
    #         'watched': self.watched
    #     }

# On User Class

def to_json(self):
    return {
        'name': self.name,
        'movies': [
            movie.m_json() for movie in self.movies
        ]
    }

    # --------------

import json

with open('calvin.txt', 'w') as f:
    json.dump(user.to_json(), f)


```

### Methods that LOAD from csv

```py

# On User Class
    # @classmethod
    # def from_json(cls, data):
    #     user = User(data['name'])
    #     movies = []

    #     for movie in data['movies']: # There's a list inside the json/dict file
    #         movies.append(Movie(movie['name'], movie['genre'], movie['watched']))

    #     user.movies = movies
    #     return user

# Next file
import json

with open('calvin.txt', 'r') as f:
    data = json.load(f)
    user = User.from_json(data) # passing dict to method called from_json() on User class


```

### JSON *args **kwargs - Useful!

Using kwargs on JSON data is super useful. It uses the ```Keys``` as the name for ```named parameters``` 


---

<br>

# Working With Directories

<br>

We can use ```pathlib```, allows me to work with macs and windows machines and their directory formats.

```py

./sibling_folder/fileIWant.txt
../parent_folder/fileIWant.txt

```

---

<br>

# Working With Regular Expressions - more in another file

[Interactive Tutorial](https://regexone.com/) ``` - Weekend Homework```

[link to cheatsheet](https://regex101.com/) ``` - quick reference / code generator```

<br>

```py

import re

pattern = re.compile('this')

string = "Yo this is the string with this in it twice, this. Three times."

a = pattern.findall(string)

print(a)

# >> ['this', 'this', 'this']

```