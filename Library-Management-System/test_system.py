#!/usr/bin/env python3
"""
Test script for Library Management System
"""

from library import Library
from book import Book
from member import Member
from librarian import Librarian
from borrow_transaction import BorrowTransaction
from datetime import datetime, timedelta

def test_basic_functionality():
    """Test basic library functionality"""
    print("=== Testing Basic Library Functionality ===")
    
    # Create library
    library = Library("Test Library")
    
    # Test adding books
    book1 = Book(1, "Test Book 1", "Author 1", "123-456", 2023)
    book2 = Book(2, "Test Book 2", "Author 2", "789-012", 2022)
    
    assert library.add_book(book1), "Failed to add book 1"
    assert library.add_book(book2), "Failed to add book 2"
    assert not library.add_book(book1), "Should not add duplicate book"
    
    print("✓ Book addition test passed")
    
    # Test adding members
    member1 = Member(1, "John Doe", "john@test.com", "555-1234")
    member2 = Member(2, "Jane Smith", "jane@test.com", "555-5678")
    
    assert library.add_member(member1), "Failed to add member 1"
    assert library.add_member(member2), "Failed to add member 2"
    assert not library.add_member(member1), "Should not add duplicate member"
    
    print("✓ Member addition test passed")
    
    # Test adding librarians
    librarian1 = Librarian(1, "Alice Librarian", "alice@library.com")
    librarian2 = Librarian(2, "Bob Librarian", "bob@library.com")
    
    assert library.add_librarian(librarian1), "Failed to add librarian 1"
    assert library.add_librarian(librarian2), "Failed to add librarian 2"
    assert not library.add_librarian(librarian1), "Should not add duplicate librarian"
    
    print("✓ Librarian addition test passed")
    
    # Test book borrowing
    success, message = library.borrow_book(1, 1, 1)
    assert success, f"Borrow failed: {message}"
    print("✓ Book borrowing test passed")
    
    # Test book return
    success, message = library.return_book(1, 1)
    assert success, f"Return failed: {message}"
    print("✓ Book return test passed")
    
    # Test search functionality
    results = library.search_books("Test")
    assert len(results) == 2, f"Expected 2 results, got {len(results)}"
    print("✓ Search functionality test passed")
    
    print("All basic functionality tests passed! ✅")

def test_error_cases():
    """Test error handling"""
    print("\n=== Testing Error Cases ===")
    
    library = Library("Test Library")
    
    # Add some data first
    book = Book(1, "Test Book", "Test Author", "123", 2023)
    member = Member(1, "Test Member", "test@test.com", "555-0000")
    librarian = Librarian(1, "Test Librarian", "librarian@test.com")
    
    library.add_book(book)
    library.add_member(member)
    library.add_librarian(librarian)
    
    # Test borrowing non-existent book
    success, message = library.borrow_book(1, 999, 1)
    assert not success, "Should fail to borrow non-existent book"
    print("✓ Non-existent book borrowing test passed")
    
    # Test borrowing with non-existent member
    success, message = library.borrow_book(999, 1, 1)
    assert not success, "Should fail to borrow with non-existent member"
    print("✓ Non-existent member borrowing test passed")
    
    # Test borrowing with non-existent librarian
    success, message = library.borrow_book(1, 1, 999)
    assert not success, "Should fail to borrow with non-existent librarian"
    print("✓ Non-existent librarian borrowing test passed")
    
    # Test returning non-borrowed book
    success, message = library.return_book(1, 1)
    assert not success, "Should fail to return non-borrowed book"
    print("✓ Non-borrowed book return test passed")
    
    print("All error case tests passed! ✅")

def test_data_persistence():
    """Test data save/load functionality"""
    print("\n=== Testing Data Persistence ===")
    
    # Create test data
    library = Library("Persistence Test Library")
    
    # Add books
    books = [
        Book(1, "Persistent Book 1", "Author A", "111-111", 2020),
        Book(2, "Persistent Book 2", "Author B", "222-222", 2021)
    ]
    for book in books:
        library.add_book(book)
    
    # Add members
    members = [
        Member(1, "Persistent Member 1", "member1@test.com", "555-1111"),
        Member(2, "Persistent Member 2", "member2@test.com", "555-2222")
    ]
    for member in members:
        library.add_member(member)
    
    # Add librarians
    librarians = [
        Librarian(1, "Persistent Librarian 1", "lib1@test.com"),
        Librarian(2, "Persistent Librarian 2", "lib2@test.com")
    ]
    for librarian in librarians:
        library.add_librarian(librarian)
    
    # Save data
    library.save_to_file("test_data.json")
    print("✓ Data saved successfully")
    
    # Create new library and load data
    new_library = Library("New Library")
    success = new_library.load_from_file("test_data.json")
    assert success, "Failed to load data from file"
    
    # Verify loaded data
    assert len(new_library.get_all_books()) == 2, "Books not loaded correctly"
    assert len(new_library.get_all_members()) == 2, "Members not loaded correctly"
    assert len(new_library.get_all_librarians()) == 2, "Librarians not loaded correctly"
    
    print("✓ Data loaded successfully and verified")
    print("Data persistence tests passed! ✅")

def test_transaction_functionality():
    """Test transaction-related functionality"""
    print("\n=== Testing Transaction Functionality ===")
    
    library = Library("Transaction Test Library")
    
    # Setup
    book = Book(1, "Transaction Book", "Transaction Author", "333-333", 2022)
    member = Member(1, "Transaction Member", "transaction@test.com", "555-3333")
    librarian = Librarian(1, "Transaction Librarian", "transaction@lib.com")
    
    library.add_book(book)
    library.add_member(member)
    library.add_librarian(librarian)
    
    # Borrow book
    success, message = library.borrow_book(1, 1, 1)
    assert success, f"Borrow failed: {message}"
    
    # Check transaction was created
    transactions = library.get_all_transactions()
    assert len(transactions) == 1, "Transaction not created"
    
    transaction = transactions[0]
    assert transaction.book_id == 1, "Wrong book ID in transaction"
    assert transaction.member_id == 1, "Wrong member ID in transaction"
    assert transaction.librarian_id == 1, "Wrong librarian ID in transaction"
    assert not transaction.is_returned, "Transaction should not be returned yet"
    
    print("✓ Transaction creation test passed")
    
    # Test overdue calculation
    assert not transaction.is_overdue(), "New transaction should not be overdue"
    print("✓ Overdue calculation test passed")
    
    # Return book
    success, message = library.return_book(1, 1)
    assert success, f"Return failed: {message}"
    
    # Check transaction was updated
    transaction = library.get_all_transactions()[0]
    assert transaction.is_returned, "Transaction should be marked as returned"
    
    print("✓ Transaction completion test passed")
    print("Transaction functionality tests passed! ✅")

if __name__ == "__main__":
    try:
        test_basic_functionality()
        test_error_cases()
        test_data_persistence()
        test_transaction_functionality()
        
        print("\n🎉 All tests passed successfully!")
        print("\nThe Library Management System is working correctly.")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
