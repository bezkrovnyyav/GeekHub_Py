'''
5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
'''

class Library(object):
    def __init__(self, books_list):
        self.books_list = books_list

    def show_books(self):
        if self.books_list:
            print('Our library has next books:\n')
            for item in self.books_list:
                print(item)
        else:
            print("Unfortunately! We don't have any book at the moment!")
    
    def take_book(self, book):
        if book in self.books_list:
            print(f"Please, take this book - {book}. Have a nice reading!\n")
            self.books_list.remove(book)
        else:
            print(f"Sorry, but the book - {book} is not in the our library now!\n")
    
    def return_book(self, book):
        print("Thank You for returning our book!")
        self.books_list.append(book)


class LibraryOperation(object):
      def request_book(self):
            print("Enter the name of the book you'd like to borrow: ")
            self.book=input()
            return self.book

      def return_book(self):
            print("Enter the name of the book you'd like to return: ")
            self.book=input()
            return self.book


def main():
    print("Welcome to our Library!\n")
    library=Library(["The Hobbit","The Fellowship of the Ring","The Two Towers", "The Return of the King"])
    operations=LibraryOperation()

    while True:
        print("""    ========LIBRARY MENU=======
    1. Show all available books
    2. Take a book
    3. Return a book
    4. Exit
    """)
        choice = input("Enter Choice: ")
        if choice == "1":
            library.show_books()
            print()
        elif choice == "2":
            library.take_book(operations.request_book())
        elif choice == "3":
            library.return_book(operations.return_book())
        elif choice == "4":
            break
        else:
            print('There is no such menu item')     

if __name__ == "__main__":
    main()  
