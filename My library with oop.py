#Library management with oop

class Books:                            #Creating class
    my_books = [["Python", 92], ["Html", 100], ["Javascript", 125], ["Php", 120]] #THis is the Main storage of my library
    def __init__(self, book):           #constructor
        for i in Books.my_books:
            for x in i:
                if x==book:             #defining that which books is wanted and set the title and pages
                    self.title = i[0]
                    self.pages = i[1]
    def change_title(self, new_title):  # Update the title  of a book available
        self.title = new_title
    def my_book():                      # Return all available books data
        string = ""
        for i in Books.my_books:
            string = string + "".join(str(i)) + "\n"
        return string
    def add_book(title, pages):             #Adding book in list
        Books.my_books.append([title, pages])

    def remove_book(title):             #remove spacific book
            l = len(Books.my_books)
            for i in Books.my_books:
                if i[0] == title:
                    Books.my_books.remove(i)
            if len(Books.my_books) == l:
                return "Boook not find"
            else:
                return "Book removed sucsessfully"



    def __str__(self):                  #Return the Object data
        try:
            return f"{self.title} is {self.pages} long"
        except:
            return "The book is not availble"
book1 = Books("Php")
print(book1)                                        #create objects and do operations
print(Books.remove_book("Php"))