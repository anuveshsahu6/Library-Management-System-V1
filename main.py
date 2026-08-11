from library import Library


# Create library
library = Library("Central Library")


# Register members
member1 = library.register_member("Anuvesh")
member2 = library.register_member("Rahul")


# Add books
book1 = library.add_book("Python Basics", "Author 1", "Programming")
book2 = library.add_book("Clean Code", "Author 2", "Programming")
book3 = library.add_book("Atomic Habits", "Author 3", "Self Help")
book4 = library.add_book("The Hobbit", "Author 4", "Fantasy")


# --------------------------------------------------
# TEST 1: Normal Issue
# --------------------------------------------------

print("\n--- TEST 1: Normal Issue ---")

member1.request_book(book1.isbn, library)

print("Borrowed Books:", member1.borrowed_books)
print("Book Available:", book1.available)
print("Allocated Books:", library.allocated_books)


# --------------------------------------------------
# TEST 2: Normal Return
# --------------------------------------------------

print("\n--- TEST 2: Normal Return ---")

member1.return_book(book1.isbn, library)

print("Borrowed Books:", member1.borrowed_books)
print("Book Available:", book1.available)
print("Allocated Books:", library.allocated_books)


# --------------------------------------------------
# TEST 3: Borrow Limit
# --------------------------------------------------

print("\n--- TEST 3: Borrow Limit ---")

member1.request_book(book1.isbn, library)
member1.request_book(book2.isbn, library)
member1.request_book(book3.isbn, library)

print("\nTrying to borrow a fourth book:")
member1.request_book(book4.isbn, library)

print("Borrowed Books:", member1.borrowed_books)


# --------------------------------------------------
# TEST 4: Invalid Member
# --------------------------------------------------

print("\n--- TEST 4: Invalid Member ---")

invalid_member_id = "invalid-member-id"

result = library.issue_book(book4.isbn, invalid_member_id)

print("Result:", result)


# --------------------------------------------------
# TEST 5: Unavailable Book
# --------------------------------------------------

print("\n--- TEST 5: Unavailable Book ---")

# book1 is currently borrowed by member1.
# member2 attempts to borrow it.

member2.request_book(book1.isbn, library)


# --------------------------------------------------
# TEST 6: Wrong Member Returns Book
# --------------------------------------------------

print("\n--- TEST 6: Wrong Member Returns Book ---")

# member2 tries to return member1's book.

member2.return_book(book1.isbn, library)

print("Book Available:", book1.available)
print("Book Owner:", library.allocated_books.get(book1.isbn))


# --------------------------------------------------
# TEST 7: Nonexistent Book
# --------------------------------------------------

print("\n--- TEST 7: Nonexistent Book ---")

invalid_isbn = "invalid-isbn"

result = library.issue_book(invalid_isbn, member2.member_id)

print("Issue Result:", result)

result = library.accept_book(invalid_isbn, member2.member_id)

print("Return Result:", result)


# --------------------------------------------------
# TEST 8: Remove Member With Borrowed Books
# --------------------------------------------------

print("\n--- TEST 8: Remove Member With Borrowed Books ---")

result = library.remove_member(member1.member_id)

print("Remove Result:", result)
print("Member Still Exists:", library.valid_member(member1.member_id))


# --------------------------------------------------
# TEST 9: Return All Books
# --------------------------------------------------

print("\n--- TEST 9: Return All Books ---")

for isbn in member1.borrowed_books.copy():
    member1.return_book(isbn, library)

print("Borrowed Books:", member1.borrowed_books)


# --------------------------------------------------
# TEST 10: Remove Member After Returning Books
# --------------------------------------------------

print("\n--- TEST 10: Remove Member After Returning Books ---")

result = library.remove_member(member1.member_id)

print("Remove Result:", result)
print("Member Still Exists:", library.valid_member(member1.member_id))