
class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def view(self):
        print(f"Title {self.title} \nAuthor: {self.author} \nPrice: {self.price}")


book = Book("Book", "Foo Bar", "$20")
book.view()