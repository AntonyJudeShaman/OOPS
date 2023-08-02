# library.py
import streamlit as st

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_book_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def search_book_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def display_books(self):
        for book in self.books:
            st.write(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")

def main():
    st.title("Library Management System")

    library = Library()

    while True:
        st.subheader("Add a Book")
        title = st.text_input("Title", key="title_input")
        author = st.text_input("Author", key="author_input")
        isbn = st.text_input("ISBN", key="isbn_input")
        if st.button("Add"):
            book = Book(title, author, isbn)
            library.add_book(book)

        st.subheader("Search Books")
        search_option = st.selectbox("Search by:", ("Title", "Author"))
        search_term = st.text_input("Enter search term", key="search_input")
        if st.button("Search"):
            if search_option == "Title":
                results = library.search_book_by_title(search_term)
            else:
                results = library.search_book_by_author(search_term)

            if results:
                st.write("Search Results:")
                for book in results:
                    st.write(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
            else:
                st.write("No results found.")

        library.display_books()

        if st.button("Clear Library"):
            library.books = []


if __name__ == "__main__":
    main()
