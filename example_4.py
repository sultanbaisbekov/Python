class Book:
    def __init__(self, title, year, author, is_available = True):
        self.title = title
        self.year = year
        self.author = author
        self.is_available = is_available

    def _str_(self):
        available_str = 'Yes' if self.is_available else 'No'
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Available: {available_str}"
        
    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Book {self.titel} was given")

        else:
            print(f"Book {self.title} is not available")

    def return_book(self):
        if not self.is_available:
            self.is_available = True 
            print('Book was returned')
        else:
            print('Book is already in the library')         

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {self.title} was added to the library")

    def list_of_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        if not available_books:
            print("There are no available books")
        else:
            print("Available books:")
            for book in available_books:
                print(book)

    def find_book_by_title(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
            return None
        
def main():
    library = Library()

    while True:
        print("\n---Library menu---")
        print("1. Add a book")
        print("2. Show the available books")
        print("3. Take a book")
        print("4. Return a book")
        print("5. Find a book by title")
        print("6. Exit")

        choice = input('Enter an option 1-6: ')

        if choice == '1':
            title = input('Enter a title of the book: ')
            author = input('Enter an author of the book: ')
            year = input('Enter a year of the book: ')
            if not year.isdigit():
                print("Book's year should be digit")
                continue
            year = int(year)
            book = Book(title, author, year)
            library.add_book(book)

        elif choice == "2":
            library.list_of_available_books()
        
        elif choice == "3":
            title = input('Enter a title to take a book: ')
            book = Library.find_book_by_title(title)
            if book:
                book.borrow()
            else:
                print("Book was not found")

        elif choice == "4":
            title = input('Enter a title of the book to return: ')
            book = Library.find_book_by_title(title)
            if book:
                book.return_book
            else:
                print('Book was not found')

        elif choice == "5":
            title = input('Enter a title of the book to return: ')
            book = Library.find_book_by_title(title)
            if book:
                 print("The book has been found")
                 print(book)
            else:
                print('Book was not found')

        elif choice == "6":
            print('Exit the programm. Goodbye!')
            break

        else:
            print('Incorrect choice. Try again.')

if __name__ == "__main__":
    main()
