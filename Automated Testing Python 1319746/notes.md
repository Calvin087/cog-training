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
  - [Unpacking Keyword Arguments (new)](#unpacking-keyword-arguments-new)
  - [Object Oriented Programming (refresher)](#object-oriented-programming-refresher)
    - [Magic Methods ```__str__``` / ```__repr__``` - Object representation](#magic-methods-__str__--__repr__---object-representation)
    - [@ClassMethods / @StaticMethods (research more)](#classmethods--staticmethods-research-more)
      - [Class methods expanded](#class-methods-expanded)
    - [Inheritance (used less than composition)](#inheritance-used-less-than-composition)
    - [Class Composition (used more often than inheritance)?](#class-composition-used-more-often-than-inheritance)
  - [Type Hinting](#type-hinting)
  - [Imports](#imports)
    - [Relative Imports](#relative-imports)
  - [Errors in Python (try / catch)](#errors-in-python-try--catch)
    - [Custom Error Classes](#custom-error-classes)
  - [First Class Functions (Important)](#first-class-functions-important)
  - [Decorators in Python (more research)](#decorators-in-python-more-research)
  - [@ Decorator syntax (more research)](#-decorator-syntax-more-research)

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

## Object Oriented Programming (refresher)

<br>

To make life easier, we make objects/classes. We can add methods to these objects to make the code look cleaner for human legibility.

It looks like we can store tuples inside the objects/classes also.

```py

class Student:
    def __init__(self, name, grades):
        self.name = name # indentation is important here also.
        self.grades = grades


cally = Student("Cally", (1,2,3,4,5))

print(cally.name)
print(cally.grades)

# >> Cally
# >> (1, 2, 3, 4, 5)

```

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

### Magic Methods ```__str__``` / ```__repr__``` - Object representation

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

## Errors in Python (try / catch)

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

## @ Decorator syntax (more research)

<br>

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