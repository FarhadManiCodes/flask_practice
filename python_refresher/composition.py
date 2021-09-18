""" to practice composition in python """


class Book():
    """A book object"""
    def __init__(self, title: str):
        """Construct"""
        self.name = title

    def __str__(self) -> str:
        """Return a string representation of a book object"""
        return f"Book: {self.name}"


class BookShelf:
    """The Book shelf class """
    def __init__(self, *books):
        """Constructor """
        self.books = books

    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."


book1 = Book("ABC")
book2 = Book("Farhad")

shelf = BookShelf(book1, book2)

print(shelf)
