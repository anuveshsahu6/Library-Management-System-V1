from member import Member
from book import Book

class Library:
    """A class representing a library management system to handle books and members."""
    
    def __init__(self, name):
        self.name = name
        # Store members using their ID as the key and the Member object as the value
        self.members = {} 
        # Store books using their ISBN as the key and the Book object as the value
        self.books = {} 
        # Track which books are borrowed. Key = ISBN, Value = Member ID
        self.allocated_books = {} 

    # --- Book Management ---

    def add_book(self, title, author, genre):
        """Creates a new book and adds it to the library's catalog if it doesn't already exist."""
        new_book = Book(title, author, genre)
        
        # Check if the book's ISBN is already in the system
        if self.existing_book(new_book.isbn) is False:
            self.books.update({new_book.isbn: new_book})
            return new_book
        else:
            print("Book Already Exists!")
            return False

    def existing_book(self, isbn):
        """Checks if a book exists in the library catalog by its ISBN."""
        if self.books.get(isbn) == None:
            return False
        else:
            return True

    def remove_book(self, isbn):
        """Removes a book from the catalog, but only if it is currently available (not borrowed)."""
        if self.book_availability(isbn):
            # pop() removes the key and returns its value. None prevents KeyError if not found.
            self.books.pop(isbn, None)
            return True
        else:
            # Fails if the book is currently borrowed or doesn't exist
            return False

    def search_book(self, isbn):
        """Retrieves a Book object from the catalog using its ISBN."""
        return self.books.get(isbn)

    def book_availability(self, isbn):
        """Checks if a book exists AND is currently available to be borrowed."""
        book = self.search_book(isbn)
        if book is None:
            return False
        return book.available

    # --- Member Management ---
    
    def register_member(self, name):
        """Creates a new member and registers them in the system."""
        new_member = Member(name)
        
        # Ensure we don't overwrite an existing member with the same ID
        if self.valid_member(new_member.member_id) is False:
            self.members[new_member.member_id] = new_member
            return new_member
        else:
            print("User Already exists!")
            return False

    def valid_member(self, member_id):
        """Checks if a member ID is officially registered in the library."""
        if self.members.get(member_id) is None:
            return False
        else:
            return True

    def search_member(self, member_id):
        """Retrieves a Member object using their member ID."""
        return self.members.get(member_id)

    def remove_member(self, member_id):
        """Removes a member from the system, provided they have returned all their books."""
        if self.valid_member(member_id):
            member = self.search_member(member_id)
            
            # Prevent removal if the member still has unreturned books
            if len(member.borrowed_books) == 0:
                self.members.pop(member_id)
                print("Member Removed!")
                return True
            else:
                return False
        else:
            return False

    def valid_borrow_limit(self, member_id):
        """Validates whether a member is under the maximum borrowing limit (3 books)."""
        if self.valid_member(member_id):
            member = self.search_member(member_id)
            if len(member.borrowed_books) < 3:
                print("Valid Borrow Limit!")
                return True
            else:
                print("Borrow Limit Exceeded!")
                return False
        else:
            print("Invalid Member ID")
            return False

    # --- Borrowing and Returning ---

    def issue_book(self, isbn, member_id):
        """Issues a book to a member, updating availability and allocations."""
        # Ensure both the book and the member exist in the system
        if self.existing_book(isbn) and self.valid_member(member_id):
            book = self.search_book(isbn)
            member = self.search_member(member_id)
            
            # Check if the book isn't already taken AND the member hasn't hit their limit
            if self.book_availability(book.isbn) and self.valid_borrow_limit(member_id):
                # Update member's borrowed list
                member.borrowed_books.append(book.isbn)
                # Mark book as checked out
                book.available = False
                # Track who has the book
                self.allocated_books.update({book.isbn: member_id})
                return True
            else:
                return False
        else:
            return False

    def accept_book(self, isbn, member_id):
        """Processes a returned book, making it available again."""
        # Ensure both the book and the member exist
        if self.existing_book(isbn) and self.valid_member(member_id):
            member = self.search_member(member_id)
            book = self.search_book(isbn)

            # Security check: Make sure this specific member is the one who actually borrowed it
            if self.allocated_books.get(isbn) == member_id:
                # Revert book status to available
                book.available = True
                # Remove from member's personal list
                member.borrowed_books.remove(book.isbn)
                # Remove from the library's active allocations list
                self.allocated_books.pop(book.isbn, None)
                return True
            else:
                return False
        else:
            return False