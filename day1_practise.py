class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")

book1= Book("1984", "George Orwell", 328)
book2= Book("To Kill a Mockingbird", "Harper Lee", 281)
book1.display_info()
book2.display_info()