class Book:
    def __init__(self, book_id, title, author, isbn, publication_year, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.available = available
    
    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Year: {self.publication_year}, Status: {status}"
    
    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False
    
    def return_book(self):
        self.available = True
    
    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'publication_year': self.publication_year,
            'available': self.available
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['book_id'],
            data['title'],
            data['author'],
            data['isbn'],
            data['publication_year'],
            data['available']
        )
