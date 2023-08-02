import streamlit as st
from datetime import datetime, timedelta

class User:
    def __init__(self, name, age, year, gender) -> None:
        self.name = name
        self.age = age
        self.year = year
        self.gender = gender

    def __str__(self) -> str:
        return f"{self.name}({self.age}) of {self.year} year, gender - {self.gender}"

class Professor(User): 
    def __init__(self, name, age, year, gender, department) -> None:
        super().__init__(name, age, year, gender)
        self.department = department

    def __str__(self) -> str:
        return f"{super().__str__()}, department - {self.department}"

class Librarian:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}"

class Book:
    def __init__(self, book_author, book_title) -> None:
        self.book_author = book_author
        self.book_title = book_title
        self.assigned = None
        self.due = None

    def __str__(self):
        return f"{self.book_author} - {self.book_title}"

class Library:
    def __init__(self) -> None:
        self.books = []
        self.validity = 0

    def add(self, book):
        self.books.append(book)

    def remove(self, book):
        self.books.remove(book)

    def borrow(self, user, book, duration=14):
        if book.assigned is None:
            book.assigned = user
            due = datetime.now() + timedelta(days=duration)
            book.due = due
            return True, due
        return False, None

    def searchbytitle(self, title):
        return [book for book in self.books if book.book_title.lower() == title.lower()]

    def searchbyauthor(self, author):
        return [book for book in self.books if book.book_author.lower() == author.lower()]

def main():
    user1 = User('Antony', 20, 4, 'Male')
    user2 = User('Jude', 21, 4, 'Male')
    user3 = User('Anu', 20, 4, 'Female')
    professor1 = Professor('John', 40, 10, 'Male', 'Computer Science')

    book1 = Book("Gog", "idk")
    book2 = Book("Eg", 'idk2')
    library = Library()
    library.add(book1)
    library.add(book2)

    st.header("Library System")
    option = st.sidebar.selectbox("Select an option", ['Get a book', 'Renew book', 'Pay for book'])

    if option == 'Get a book':
        option1 = st.selectbox("Search by name or author", ['author', 'title'])
        results = []  
        if option1 == 'author':
            author = st.text_input("Enter author name")
            if st.button("Search"):
                if author:
                    results = library.searchbyauthor(author)
                    if results:
                        for r in results:
                            st.write(r)
                    else:
                        st.write("No results found.")
        elif option1 == 'title':
            title = st.text_input("Enter title name")
            if st.button("Search"):
                if title:
                    results = library.searchbytitle(title)
                    if results:
                        for r in results:
                            st.write(r)
                    else:
                        st.write("No results found.")

        if st.button("Borrow"):
            if results:
                s, due_date = library.borrow(user1, results[0])  
                if s:
                    st.success(f"Book assigned to {user1.name}, due on {due_date.strftime('%Y-%m-%d')}")
                else:
                    st.write("Book not assigned")

    elif option == 'Renew book':
        title = st.text_input("Enter Title")
        author = st.text_input("Enter Author")

        if st.button("Renew"):
            if title and author:
                res = library.searchbytitle(title)
                if res:
                    for r in res:
                        if r.book_author == author:
                            selected_book = r
                            if selected_book.assigned == user1: 
                                if selected_book.due:
                                    selected_book.due = selected_book.due + timedelta(days=5)  
                                    st.success("Renewed for 5 extra days")
                                else:
                                    st.write("The selected book has not been assigned yet, or its due date is not set.")
                            else:
                                st.write("You can only renew a book that is currently assigned to you.")
                            break
                    else:
                        st.write("No matching book found.")
                else:
                    st.write("No matching book found.")
            else:
                st.write("Please enter both title and author to renew a book.")

    elif option == 'Pay for book':
        st.write("Payment")
        st.selectbox("Card Type", ['Credit card', 'Debit card'])
        if st.button("Pay now"):
            st.success("Payment successful")


if __name__ == "__main__":
    main()
