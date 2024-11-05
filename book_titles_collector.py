# Book Titles Collector assignment
# Create main function
def main():
    print("Hello I am a book title collector.\nI will sort any book titles you give me.\nPlease input the titles of ten books.")
    books=[]
    while len(books)!=10:
        book=input("Please input a book title:")
        book_title=book.title()
        books.append(book_title)
    books_sorted=sorted(books)
    print("Here is a list of your titles in alphabetic order.")
    for x in books_sorted:
        print(x,end=", ")
main()