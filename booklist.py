def main():
    try:
        booksList = []
        infile = open("theBooksList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("THe <theBookList.txt> file not found")
        print("Starting a new book list")
        booksList = []



    choice = 0
    while choice != 6:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display book")
        print("4) Delete a book")
        print("5) Update Book Details")
        print("6) Exit")
        choice = int(input())

        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the Book >>>")
            nAuthor = input("Enter the name of the Author >>>")
            nPages = input("Enter the number of pages >>>")
            booksList.append([nBook, nAuthor, nPages])
        elif choice == 2:
            print("Looking up for a book...")
            keyWord = input("Enter search term: ")
            for book in booksList:
                if keyWord in book:
                    print(book)

        elif choice == 3:
            print("Displaying all books...")
            for book in booksList:
                print(book)

        elif choice == 4:
            print("Deleting book...")
            keyWord = input("Enter book to delete: ")
            found = False
            for book in booksList:
                if keyWord in book:
                    found = True
                    booksList.remove((book))
                    break
            if not found:
                print("Book doesn't exist")
        elif choice == 5:
            print("Updating book details...")
            keyWord = input("Enter book to be updated: ")
            found = False

            for book in booksList:
                if keyWord in book:
                    found = True
                    detail = input("Enter details to be updated(Name, Author, Pages): ").lower()
                    if detail == 'name':
                        new = input("Enter new name")
                        book[0] = str(new)
                        break
                    elif detail == 'author':
                        new = input("Enter new author")
                        book[1] = str(new)
                        break
                    elif detail == 'pages':
                        new = input("Enter no of pages")
                        book[2] = str(new)
                        break
                if not found:
                    print("Book doesnt exist")
    print("Program terminated")

    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()
