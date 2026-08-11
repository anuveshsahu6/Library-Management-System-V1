# Library Management System

A small Library Management System built in Python as my second OOP project.

The main purpose of this project wasn't to build a production-ready library application. I built it to understand how different objects should interact with each other, how responsibilities should be divided between classes, and how to structure a project across multiple files.

## What the system can do

* Add and remove books
* Register and remove members
* Search for books and members
* Issue books to members
* Return books
* Track which books are currently issued
* Enforce a maximum borrowing limit of 3 books per member
* Prevent unavailable books from being issued
* Prevent a member from returning someone else's book
* Prevent removing a member while they still have borrowed books

## Project Structure

```text
Library-Management-System/
│
├── main.py
├── library.py
├── book.py
└── member.py
```

### `library.py`

The `Library` class acts as the main controller of the system.

It is responsible for:

* Maintaining the collection of books
* Maintaining registered members
* Validating requests
* Issuing and accepting books
* Tracking allocated books
* Managing borrowing limits

### `book.py`

Contains the `Book` class.

A book stores its:

* Title
* Author
* Genre
* ISBN
* Availability status

The `Book` class doesn't manage members or library operations. Those responsibilities belong to the `Library`.

### `member.py`

Contains the `Member` class.

A member stores:

* Name
* Member ID
* Books currently borrowed

The member doesn't directly change the state of a book. Instead, it sends requests to the `Library`.

### `main.py`

Used to run the system and test different scenarios.

I also used it to test both successful operations and invalid requests.

## A design decision I made

One important part of the design is `allocated_books`.

```python
allocated_books = {
    ISBN: Member_ID
}
```

I initially considered relying only on each member's `borrowed_books` list, but keeping a separate allocation record gives the library a direct way to determine who currently has a particular book.

This also helped when validating book returns.

## Borrowing Flow

The basic flow is:

```text
Member
   ↓
Requests a book
   ↓
Library validates the request
   ↓
Checks member + book + borrowing limit
   ↓
Book is issued
   ↓
Library updates the required records
```

The member doesn't directly modify the book's availability or their borrowed-books list.

## Testing

I tested both normal and failure cases, including:

* Normal issue and return
* Borrowing the maximum 3 books
* Attempting to borrow a fourth book
* Invalid member
* Unavailable book
* Wrong member trying to return a book
* Non-existent book
* Removing a member with borrowed books
* Removing a member after returning all books
* Removing available and issued books

The final test run passed these scenarios.

## What I learned

This project helped me understand that writing classes isn't the same thing as designing a system.

Some of the main things I learned were:

* Different classes should have clear responsibilities.
* A class shouldn't control something that belongs to another class.
* Breaking a project into modules makes it easier to manage.
* Object references can be used to represent relationships between objects.
* Dictionaries can act as useful registries for objects.
* Testing invalid situations is just as important as testing successful ones.
* A working program isn't necessarily a well-designed program.

This was also my first time properly separating a project into multiple Python files instead of putting everything into one file.

## Current Status

**Version 1 — Complete**

The goal of V1 was learning OOP, modularization and basic system design rather than adding a large number of features.

Future improvements can be considered in a V2, but for now the project is intentionally being kept simple.
