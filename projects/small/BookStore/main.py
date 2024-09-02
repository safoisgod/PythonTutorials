def main():

    # use try except to catch no existent file+
    try:
        bookList = []
        #initializing booklist.text
        importfile = open("theBooksList.txt", "r")
        line = importfile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = importfile.readline()
        importfile.close()
    except FileNotFoundError:
        print("<theBooksList.txt> file not Available")
        print("starting a new book list")
        bookList = []

    choice = 0

    while choice != 4:

        print("""*** Books Library ***
    1) Add a book
    2) Find a book
    3) Display all books
    4) Quit""")
        choice = int(input(">>>: "))

        if choice ==  1:
            print("Adding a book .......")
            BookName = input("Enter name of book: ")
            BookAuthor = input("Enter name of Author: ")
            Pages = input("Enter number of pages: ")
            bookList. append([BookName, BookAuthor, Pages])

        elif choice == 2:
            keyword = input("Enter search term: ")
            print("Looking for book .............")
            for book in bookList:
                if keyword in book:
                    print(("""
    Book Name : {}
    Author : {}
    No. of pages : {}
    """).format(book[0],book[1],book[2]))


        elif choice == 3:
            print("Displaying all books.........")
            booknumber = 0
            for book in bookList:
                booknumber += 1
                print(("""
    Book No.: {}                           
    Book Name : {}
    Author : {}
    No. of pages : {}
    """).format(booknumber,book[0],book[1],book[2]))
            
        elif choice == 4:
            print("Quitting Program..............")

    print("Program Terminated Successfully!!!")


    # saving books in a txt file
    exportfile = open("theBooksList.txt", "w")
    for book in bookList:
        exportfile.write(",". join(book) + "\n")
    exportfile.close()

if __name__ == "__main__":
    main()


