# q2_library_system.py

def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed successfully.")
    else:
        print(f"Book {book_id} cannot be borrowed.")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} was not borrowed.")


def register_member(members, member_id):
    members.add(member_id)  # duplicates ignored automatically


def show_available(catalog, borrowed_books):
    print("\nAvailable Books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"ID: {book_id}, Title: {title}, Author: {author}, Year: {year}")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    # Add 4 books
    add_book(catalog, 101, "Python Basics", "John Doe", 2023)
    add_book(catalog, 102, "Data Structures", "Jane Smith", 2022)
    add_book(catalog, 103, "Machine Learning", "Andrew Ng", 2021)
    add_book(catalog, 104, "Artificial Intelligence", "Stuart Russell", 2020)

    # Register 3 members (one duplicate)
    register_member(members, 1001)
    register_member(members, 1002)
    register_member(members, 1003)
    register_member(members, 1001)  # duplicate

    print("Registered Members:", members)

    # Borrow 2 books
    borrow_book(catalog, borrowed_books, 101)
    borrow_book(catalog, borrowed_books, 103)

    print("Borrowed Books:", borrowed_books)

    # Return 1 book
    return_book(borrowed_books, 101)

    print("Borrowed Books after return:", borrowed_books)

    # Display available books
    show_available(catalog, borrowed_books)


if __name__ == "__main__":
    main()