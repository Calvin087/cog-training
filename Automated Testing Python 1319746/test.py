from typing import List, Optional

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
#
print(bob.grades)
print(sam.grades)

# >> [99]
# >> []