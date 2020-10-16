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