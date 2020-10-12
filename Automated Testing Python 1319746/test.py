# ctrl alt m - terminate code runner
print("\n") # formatting

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

print("\n") # formatting