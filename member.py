import uuid

class Member:
    """Represents a library member who can request and return books."""

    def __init__(self, name):
        self.name = name
        # Generate a unique identifier for the member
        self.member_id = str(uuid.uuid4())
        # Store ISBNs of books currently borrowed by this member
        self.borrowed_books = [] 

    def request_book(self, isbn, library):
        """Attempts to issue a book from the library to this member."""
        if library.issue_book(isbn, self.member_id):
            print("Book Issued!")
            return True
        else:
            print("Library Rejected The Request!")
            return False

    def return_book(self, isbn, library):
        """Attempts to return a borrowed book back to the library."""
        if library.accept_book(isbn, self.member_id):
            print("Book Returned!")
            return True
        else:
            print("Library Rejected The Request!")
            return False