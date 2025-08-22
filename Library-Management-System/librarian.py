from datetime import datetime, timedelta

class Librarian:
    def __init__(self, librarian_id, name, email):
        self.librarian_id = librarian_id
        self.name = name
        self.email = email
    
    def __str__(self):
        return f"Librarian ID: {self.librarian_id}, Name: {self.name}, Email: {self.email}"
    
    def add_book(self, library, book):
        """Add a new book to the library"""
        return library.add_book(book)
    
    def remove_book(self, library, book_id):
        """Remove a book from the library"""
        return library.remove_book(book_id)
    
    def register_member(self, library, member):
        """Register a new member"""
        return library.add_member(member)
    
    def process_borrow(self, library, member_id, book_id):
        """Process a book borrowing transaction"""
        return library.borrow_book(member_id, book_id, self.librarian_id)
    
    def process_return(self, library, member_id, book_id):
        """Process a book return transaction"""
        return library.return_book(member_id, book_id)
    
    def generate_report(self, library, report_type="all"):
        """Generate various reports"""
        if report_type == "books":
            return library.get_all_books()
        elif report_type == "members":
            return library.get_all_members()
        elif report_type == "transactions":
            return library.get_all_transactions()
        else:
            return {
                "books": library.get_all_books(),
                "members": library.get_all_members(),
                "transactions": library.get_all_transactions()
            }
    
    def to_dict(self):
        return {
            'librarian_id': self.librarian_id,
            'name': self.name,
            'email': self.email
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            data['librarian_id'],
            data['name'],
            data['email']
        )
