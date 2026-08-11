import uuid

class Book:
    """Represents a book item in the library catalog."""

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        
        # Track whether the book can be checked out (defaults to True upon creation)
        self.available = True
        
        # Generate a unique identifier (UUID v4) as a surrogate ISBN
        self.isbn = str(uuid.uuid4())