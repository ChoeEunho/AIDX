class Book:
    def __init__(self, title, isbn):
        self.__title = title
        self.__isbn = isbn
    def __repr__(self):
        return "isbn." + self.__isbn+ ", name : "+self.__title
book = Book("The Python Tutorial", "442456789" )
book2 = Book("the machine language", "7894561")
print(book)
print(book2)