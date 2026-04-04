class LibraryBook:
    is_available = True
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"You borrowed {self.title}")
        else:
            print(f"Sorry, {self.title} is already borrowed")
    def return_book(self):
        self.is_available = True

book = LibraryBook("Book","Author")
book.borrow_book()
book.borrow_book()

