import json
from datetime import datetime
from book import Book
from member import Member
from librarian import Librarian
from borrow_transaction import BorrowTransaction

class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}  # {book_id: Book object}
        self.members = {}  # {member_id: Member object}
        self.librarians = {}  # {librarian_id: Librarian object}
        self.transactions = {}  # {transaction_id: BorrowTransaction object}
        self.next_book_id = 1
        self.next_member_id = 1
        self.next_librarian_id = 1
        self.next_transaction_id = 1
    
    def add_book(self, book):
        """Add a new book to the library"""
        if book.book_id in self.books:
            return False
        self.books[book.book_id] = book
        return True
    
    def remove_book(self, book_id):
        """Remove a book from the library"""
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
    
    def add_member(self, member):
        """Add a new member"""
        if member.member_id in self.members:
            return False
        self.members[member.member_id] = member
        return True
    
    def add_librarian(self, librarian):
        """Add a new librarian"""
        if librarian.librarian_id in self.librarians:
            return False
        self.librarians[librarian.librarian_id] = librarian
        return True
    
    def borrow_book(self, member_id, book_id, librarian_id):
        """Borrow a book"""
        if member_id not in self.members:
            return False, "Member not found"
        if book_id not in self.books:
            return False, "Book not found"
        if librarian_id not in self.librarians:
            return False, "Librarian not found"
        
        book = self.books[book_id]
        member = self.members[member_id]
        
        if not book.available:
            return False, "Book is not available"
        
        # Create transaction
        transaction = BorrowTransaction(
            self.next_transaction_id,
            book_id,
            member_id,
            librarian_id,
            datetime.now()
        )
        
        # Update book and member status
        book.borrow()
        member.borrow_book(book_id)
        
        # Store transaction
        self.transactions[self.next_transaction_id] = transaction
        self.next_transaction_id += 1
        
        return True, f"Book borrowed successfully. Transaction ID: {transaction.transaction_id}"
    
    def return_book(self, member_id, book_id):
        """Return a borrowed book"""
        if member_id not in self.members:
            return False, "Member not found"
        if book_id not in self.books:
            return False, "Book not found"
        
        book = self.books[book_id]
        member = self.members[member_id]
        
        # Find the active transaction for this book and member
        active_transaction = None
        for transaction in self.transactions.values():
            if (transaction.book_id == book_id and 
                transaction.member_id == member_id and 
                not transaction.is_returned):
                active_transaction = transaction
                break
        
        if not active_transaction:
            return False, "No active borrowing transaction found"
        
        # Update transaction, book, and member
        active_transaction.return_book()
        book.return_book()
        member.return_book(book_id)
        
        return True, f"Book returned successfully. Transaction ID: {active_transaction.transaction_id}"
    
    def get_all_books(self):
        """Get all books"""
        return list(self.books.values())
    
    def get_available_books(self):
        """Get all available books"""
        return [book for book in self.books.values() if book.available]
    
    def get_borrowed_books(self):
        """Get all borrowed books"""
        return [book for book in self.books.values() if not book.available]
    
    def get_all_members(self):
        """Get all members"""
        return list(self.members.values())
    
    def get_all_librarians(self):
        """Get all librarians"""
        return list(self.librarians.values())
    
    def get_all_transactions(self):
        """Get all transactions"""
        return list(self.transactions.values())
    
    def get_member_borrowed_books(self, member_id):
        """Get books borrowed by a specific member"""
        if member_id not in self.members:
            return []
        
        member = self.members[member_id]
        borrowed_books = []
        for book_id in member.borrowed_books:
            if book_id in self.books:
                borrowed_books.append(self.books[book_id])
        
        return borrowed_books
    
    def search_books(self, query):
        """Search books by title or author"""
        query = query.lower()
        results = []
        for book in self.books.values():
            if (query in book.title.lower() or 
                query in book.author.lower() or 
                query in book.isbn.lower()):
                results.append(book)
        return results
    
    def save_to_file(self, filename):
        """Save library data to JSON file"""
        data = {
            'name': self.name,
            'books': [book.to_dict() for book in self.books.values()],
            'members': [member.to_dict() for member in self.members.values()],
            'librarians': [librarian.to_dict() for librarian in self.librarians.values()],
            'transactions': [transaction.to_dict() for transaction in self.transactions.values()],
            'next_ids': {
                'book': self.next_book_id,
                'member': self.next_member_id,
                'librarian': self.next_librarian_id,
                'transaction': self.next_transaction_id
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename):
        """Load library data from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.name = data['name']
            
            # Load books
            self.books = {}
            for book_data in data['books']:
                book = Book.from_dict(book_data)
                self.books[book.book_id] = book
            
            # Load members
            self.members = {}
            for member_data in data['members']:
                member = Member.from_dict(member_data)
                self.members[member.member_id] = member
            
            # Load librarians
            self.librarians = {}
            for librarian_data in data['librarians']:
                librarian = Librarian.from_dict(librarian_data)
                self.librarians[librarian.librarian_id] = librarian
            
            # Load transactions
            self.transactions = {}
            for transaction_data in data['transactions']:
                transaction = BorrowTransaction.from_dict(transaction_data)
                self.transactions[transaction.transaction_id] = transaction
            
            # Load next IDs
            next_ids = data.get('next_ids', {})
            self.next_book_id = next_ids.get('book', 1)
            self.next_member_id = next_ids.get('member', 1)
            self.next_librarian_id = next_ids.get('librarian', 1)
            self.next_transaction_id = next_ids.get('transaction', 1)
            
            return True
        except (FileNotFoundError, json.JSONDecodeError):
            return False
