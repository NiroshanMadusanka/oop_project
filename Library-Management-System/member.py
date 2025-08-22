class Member:
    def __init__(self, member_id, name, email, phone):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = []  # List of book IDs currently borrowed
    
    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Borrowed Books: {len(self.borrowed_books)}"
    
    def borrow_book(self, book_id):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            return True
        return False
    
    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False
    
    def get_borrowed_books_count(self):
        return len(self.borrowed_books)
    
    def to_dict(self):
        return {
            'member_id': self.member_id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'borrowed_books': self.borrowed_books.copy()
        }
    
    @classmethod
    def from_dict(cls, data):
        member = cls(
            data['member_id'],
            data['name'],
            data['email'],
            data['phone']
        )
        member.borrowed_books = data['borrowed_books']
        return member
