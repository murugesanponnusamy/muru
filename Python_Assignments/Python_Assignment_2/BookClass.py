class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.price:.2f}"

book = Book("Python Basics", "John Smith", 29.99)
print(book)
