from library import Library
from book import Book
from member import Member
from librarian import Librarian
import json

def main():
    # Initialize library
    library = Library("City Central Library")
    
    # Add some sample data
    add_sample_data(library)
    
    # Main menu
    while True:
        print("\n=== Library Management System ===")
        print("1. Librarian Menu")
        print("2. Member Menu")
        print("3. View Library Status")
        print("4. Search Books")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            librarian_menu(library)
        elif choice == '2':
            member_menu(library)
        elif choice == '3':
            view_library_status(library)
        elif choice == '4':
            search_books(library)
        elif choice == '5':
            save_data(library)
        elif choice == '6':
            load_data(library)
        elif choice == '7':
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

def librarian_menu(library):
    """Librarian operations menu"""
    while True:
        print("\n=== Librarian Menu ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Register Member")
        print("4. Process Book Borrow")
        print("5. Process Book Return")
        print("6. Generate Reports")
        print("7. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            register_member(library)
        elif choice == '4':
            process_borrow(library)
        elif choice == '5':
            process_return(library)
        elif choice == '6':
            generate_reports(library)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def member_menu(library):
    """Member operations menu"""
    while True:
        print("\n=== Member Menu ===")
        print("1. View Available Books")
        print("2. View My Borrowed Books")
        print("3. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_available_books(library)
        elif choice == '2':
            view_my_borrowed_books(library)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def add_sample_data(library):
    """Add sample data to the library"""
    # Add librarians
    librarian1 = Librarian(1, "Alice Johnson", "alice@library.com")
    librarian2 = Librarian(2, "Bob Smith", "bob@library.com")
    library.add_librarian(librarian1)
    library.add_librarian(librarian2)
    
    # Add books
    books = [
        Book(1, "The Great Gatsby", "F. Scott Fitzgerald", "978-0-7432-7356-5", 1925),
        Book(2, "To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", 1960),
        Book(3, "1984", "George Orwell", "978-0-452-28423-4", 1949),
        Book(4, "Pride and Prejudice", "Jane Austen", "978-0-14-143951-8", 1813),
        Book(5, "The Catcher in the Rye", "J.D. Salinger", "978-0-316-76948-0", 1951)
    ]
    
    for book in books:
        library.add_book(book)
    
    # Add members
    members = [
        Member(1, "John Doe", "john@email.com", "555-0101"),
        Member(2, "Jane Smith", "jane@email.com", "555-0102"),
        Member(3, "Mike Wilson", "mike@email.com", "555-0103")
    ]
    
    for member in members:
        library.add_member(member)
    
    print("Sample data loaded successfully!")

def add_book(library):
    """Add a new book to the library"""
    print("\n=== Add New Book ===")
    try:
        book_id = int(input("Enter book ID: "))
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        year = int(input("Enter publication year: "))
        
        book = Book(book_id, title, author, isbn, year)
        if library.add_book(book):
            print("Book added successfully!")
        else:
            print("Book ID already exists!")
    except ValueError:
        print("Invalid input. Please enter valid numbers for ID and year.")

def remove_book(library):
    """Remove a book from the library"""
    print("\n=== Remove Book ===")
    try:
        book_id = int(input("Enter book ID to remove: "))
        if library.remove_book(book_id):
            print("Book removed successfully!")
        else:
            print("Book not found!")
    except ValueError:
        print("Invalid book ID!")

def register_member(library):
    """Register a new member"""
    print("\n=== Register New Member ===")
    try:
        member_id = int(input("Enter member ID: "))
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        
        member = Member(member_id, name, email, phone)
        if library.add_member(member):
            print("Member registered successfully!")
        else:
            print("Member ID already exists!")
    except ValueError:
        print("Invalid member ID!")

def process_borrow(library):
    """Process book borrowing"""
    print("\n=== Process Book Borrow ===")
    try:
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        librarian_id = int(input("Enter your librarian ID: "))
        
        success, message = library.borrow_book(member_id, book_id, librarian_id)
        print(message)
    except ValueError:
        print("Invalid input!")

def process_return(library):
    """Process book return"""
    print("\n=== Process Book Return ===")
    try:
        member_id = int(input("Enter member ID: "))
        book_id = int(input("Enter book ID: "))
        
        success, message = library.return_book(member_id, book_id)
        print(message)
    except ValueError:
        print("Invalid input!")

def generate_reports(library):
    """Generate library reports"""
    print("\n=== Library Reports ===")
    print("1. All Books")
    print("2. All Members")
    print("3. All Transactions")
    print("4. Available Books")
    print("5. Borrowed Books")
    
    choice = input("Enter report type: ")
    
    if choice == '1':
        books = library.get_all_books()
        print("\nAll Books:")
        for book in books:
            print(f"  - {book}")
    elif choice == '2':
        members = library.get_all_members()
        print("\nAll Members:")
        for member in members:
            print(f"  - {member}")
    elif choice == '3':
        transactions = library.get_all_transactions()
        print("\nAll Transactions:")
        for transaction in transactions:
            print(f"  - {transaction}")
    elif choice == '4':
        books = library.get_available_books()
        print("\nAvailable Books:")
        for book in books:
            print(f"  - {book}")
    elif choice == '5':
        books = library.get_borrowed_books()
        print("\nBorrowed Books:")
        for book in books:
            print(f"  - {book}")
    else:
        print("Invalid choice!")

def view_library_status(library):
    """View library status"""
    print(f"\n=== {library.name} Status ===")
    print(f"Total Books: {len(library.get_all_books())}")
    print(f"Available Books: {len(library.get_available_books())}")
    print(f"Borrowed Books: {len(library.get_borrowed_books())}")
    print(f"Total Members: {len(library.get_all_members())}")
    print(f"Total Librarians: {len(library.get_all_librarians())}")
    print(f"Total Transactions: {len(library.get_all_transactions())}")

def search_books(library):
    """Search for books"""
    query = input("\nEnter search query (title, author, or ISBN): ")
    results = library.search_books(query)
    
    if results:
        print(f"\nSearch Results ({len(results)} found):")
        for book in results:
            print(f"  - {book}")
    else:
        print("No books found matching your search.")

def view_available_books(library):
    """View available books"""
    books = library.get_available_books()
    print("\nAvailable Books:")
    if books:
        for book in books:
            print(f"  - {book}")
    else:
        print("No books available at the moment.")

def view_my_borrowed_books(library):
    """View books borrowed by current member"""
    try:
        member_id = int(input("Enter your member ID: "))
        books = library.get_member_borrowed_books(member_id)
        
        if books:
            print(f"\nYour Borrowed Books ({len(books)}):")
            for book in books:
                print(f"  - {book}")
        else:
            print("You have no borrowed books.")
    except ValueError:
        print("Invalid member ID!")

def save_data(library):
    """Save library data to file"""
    filename = input("Enter filename to save (default: library_data.json): ") or "library_data.json"
    library.save_to_file(filename)
    print(f"Data saved to {filename}")

def load_data(library):
    """Load library data from file"""
    filename = input("Enter filename to load (default: library_data.json): ") or "library_data.json"
    if library.load_from_file(filename):
        print(f"Data loaded from {filename}")
    else:
        print(f"Failed to load data from {filename}")

if __name__ == "__main__":
    main()
