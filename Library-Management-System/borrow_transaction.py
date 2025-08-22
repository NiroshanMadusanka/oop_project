from datetime import datetime, timedelta

class BorrowTransaction:
    def __init__(self, transaction_id, book_id, member_id, librarian_id, borrow_date, due_date=None, return_date=None):
        self.transaction_id = transaction_id
        self.book_id = book_id
        self.member_id = member_id
        self.librarian_id = librarian_id
        self.borrow_date = borrow_date
        self.due_date = due_date if due_date else borrow_date + timedelta(days=14)  # Default 2 weeks
        self.return_date = return_date
        self.is_returned = return_date is not None
    
    def __str__(self):
        status = "Returned" if self.is_returned else "Active"
        return_date_str = self.return_date.strftime("%Y-%m-%d") if self.return_date else "Not returned"
        return f"Transaction ID: {self.transaction_id}, Book: {self.book_id}, Member: {self.member_id}, Status: {status}, Borrowed: {self.borrow_date.strftime('%Y-%m-%d')}, Due: {self.due_date.strftime('%Y-%m-%d')}, Returned: {return_date_str}"
    
    def return_book(self, return_date=None):
        """Mark the book as returned"""
        self.return_date = return_date if return_date else datetime.now()
        self.is_returned = True
    
    def is_overdue(self):
        """Check if the book is overdue"""
        if self.is_returned:
            return self.return_date > self.due_date
        return datetime.now() > self.due_date
    
    def get_days_overdue(self):
        """Get number of days overdue"""
        if not self.is_returned:
            if datetime.now() > self.due_date:
                return (datetime.now() - self.due_date).days
            return 0
        else:
            if self.return_date > self.due_date:
                return (self.return_date - self.due_date).days
            return 0
    
    def to_dict(self):
        return {
            'transaction_id': self.transaction_id,
            'book_id': self.book_id,
            'member_id': self.member_id,
            'librarian_id': self.librarian_id,
            'borrow_date': self.borrow_date.isoformat(),
            'due_date': self.due_date.isoformat(),
            'return_date': self.return_date.isoformat() if self.return_date else None,
            'is_returned': self.is_returned
        }
    
    @classmethod
    def from_dict(cls, data):
        borrow_date = datetime.fromisoformat(data['borrow_date'])
        due_date = datetime.fromisoformat(data['due_date'])
        return_date = datetime.fromisoformat(data['return_date']) if data['return_date'] else None
        
        return cls(
            data['transaction_id'],
            data['book_id'],
            data['member_id'],
            data['librarian_id'],
            borrow_date,
            due_date,
            return_date
        )
