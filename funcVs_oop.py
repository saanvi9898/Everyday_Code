# "Library System" ka basic version banao — dono tarike se:

# Functional Approach:
# Add book (title, author)

# Borrow book (by title)

# Show all books
books=[]

def add_book(title, author):
    book={'b_title':title, 'b_lekhak':author}
    books.append(book)

def borrow_book(title):
    for book in books:
        if book['b_title']==title:
            return book
        else:
            return "book not exists"
def show_all_books():
    for book in books:
        print('book title',book['b_title'])
        print('book author',book['b_lekhak'])


#===============================
# function calling


add_book("Python Basics", "Guido")
add_book("Django Mastery", "Adrian")

show_all_books()

borrowed = borrow_book("Python Basics")
print("Borrowed:", borrowed)

missing = borrow_book("Flask in Action")
print("Borrowed:", missing)



