

library = {}

def add_book():
    """
    Prompts the user to enter the title, genre, and price of a book separated by vertical bars.
    Adds the book to the library dictionary with the title as the key and the genre and price as the value.
    Prints a message indicating that the book has been added.
    Returns True to indicate that the book was successfully added.
    """
    try:
        entry = input("Enter the title, genre, and price of the book separated by vertical bars (|): ")
        title, genre, price = map(str.strip, entry.split("|"))
        library[title] = (genre, float(price))
        print(f"\nThe book '{title}' has been added to the library.\n")
        return True
    except ValueError:
        print("\nInvalid input format. Please enter the title, genre, and price separated by vertical bars.\n")
        return False

def remove_book():
    """
    Prompts the user to enter the title of a book to remove.
    Removes the book from the library if it is found and prints a message indicating that the book has been removed.
    If the book is not found, prints an error message and returns False.
    Returns True if the book is successfully removed.
    """
    title = input("Enter the title of the book to remove: ").strip()
    if title in library:
        del library[title]
        print(f"\nThe book '{title}' has been removed from the library.\n")
        return True
    else:
        print(f"\nThe book '{title}' was not found in the library.\n")
        return False

def get_book_info():
    """
    Prompts the user to enter the title of a book to get information about.
    Prints the title, genre, and price of the book if it is found in the library.
    If the book is not found, prints an error message.
    """
    title = input("Enter the title of the book to get information about: ").strip()
    if title in library:
        genre, price = library[title]
        print(f"\nTitle: {title}\nGenre: {genre}\nPrice: ${price:.2f}\n")
    else:
        print(f"\nThe book '{title}' was not found in the library.\n")

def list_books():
    """
    Lists all books in the library in alphabetical order by title.
    If the library is empty, prints a message indicating that it is empty and returns False.
    Returns True if there are books in the library.
    """
    if not library:
        print("\nThe library is empty.\n")
        return False
    print()
    for title, (genre, price) in sorted(library.items()):
        print("%s (%s, $%.2f)" % (title, genre, price))
    print()
    return True

def list_books_by_genre():
    """
    Prompts the user to enter a genre to search for.
    Lists all books in the library that match the specified genre in alphabetical order by title.
    If no books are found in the specified genre, prints an error message and returns False.
    Returns True if at least one book is found in the specified genre.
    """
    genre_search = input("Enter the genre to list books by: ").strip()
    books_in_genre = [(title, genre, price) for title, (genre, price) in library.items() if genre == genre_search]
    if books_in_genre:
        print()
        for title, genre, price in sorted(books_in_genre):
            print(f"{title} ({genre}, ${price:.2f})")
        print()
        return True
    else:
        print(f"\nNo books found in the genre '{genre_search}'.\n")
        return False

while True:
    print("Menu:\n1. Add a book\n2. Remove a book\n3. Get book information\n4. List all books\n5. List books by genre\n6. Quit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        add_book_return = add_book()
        if add_book_return:
            list_books()
    elif choice == "2":
        remove_book_return = remove_book()
        if remove_book_return:
            list_books()
    elif choice == "3":
        get_book_info()
    elif choice == "4":
        list_books()
    elif choice == "5":
        list_books_by_genre()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

print("Goodbye!")