class Book:
    def __init__(self, title):
        self.title = title

class BookCollection:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)

class BookIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration

collection = BookCollection()
collection.add_book(Book("Гарри Поттер"))
collection.add_book(Book("Властелин Колец"))

for book in collection:
    print(book.title)