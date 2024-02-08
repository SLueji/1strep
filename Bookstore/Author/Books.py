from Book import Book,Author

class BooksandAuthors:
    def __init__(self,books=[],authors=[]):
        self.books=books
        self.authors=authors

    ###Write methods####################################33
    ####AddAuthor - Receives author informantion, verifies if there is another author with same name,
    ###if not, insert author to current list
    ##inputs: authorName : str - name of the author
    ##nationality: str - self obvious
    #aliveStatus: Boolean - is them alive
    def AddAuthor(self,name,nationality,alive):
        if self.GetAuthorByName(name) is None:
            newKey = str(len(self.authors)+1)
            newAuthor = Author(newKey,name,nationality,alive)
            self.authors.append(newAuthor)
            return newKey
        return False

    

    def AddBook(self,title,authorname,npages,version,genre,price):
        author=self.GetAuthorByName(authorname)
        if author is None:
            return "Author does not exist"
        if len(self.GetBooksbyTitle(title))==0:
            newKey = str(len(self.books)+1)
            newBook = Book(newKey,title,author,npages,version,genre,price)
            self.books.append(newBook)
            return newKey
        return "Title already exists"    
        


    ### Read methods#############################################
        ##3get books by author ID
        ###Inputs: authorID: str - id of the author
        ##outputs: Returns a list of books:Book whose author is identified
        ##By the input authorID
        ###
    def GetBooksbyAuthorID(self,authorID):
        outList = []
        for book in self.books:
            if book.Author.authorID == authorID:
                outList.append(book)
        return outList

    def GetBooksbyBookID(self,bookID):
        outList = []
        for book in self.books:
            if book.bookID == bookID:
                return book
        return None
    
    def GetBooksbyTitle(self, bookTitle):
        outList = []
        for book in self.books:
            if book.bookTitle == bookTitle:
                outList.append(book)
        return outList
    
    def GetBooksbyAuthorName(self, authorName):
        outList = []
        for book in self.books:
            if book.Author.authorName == authorName:
                outList.append(book)
        return outList

    def GetAuthorByName(self, authorName):
        for author in self.authors:
            if author.authorName == authorName:
                return author
        return None
    
    def GetAuthorByauthorID(self, authorID):
        for author in self.authors:
            if author.authorID == authorID:
                return author
        return None
    def AuthorIDexists(self, authorID:str):
        return not self.GetAuthorByauthorID(authorID) is None


    ####################################################################
            

        

L=Author("1234","João","Portuguesa",False)
N=Author("456","Sara","Italiana")
A=Book(
    bookID="ABC123",
    bookTitle="Serena's tears",
    Author=N,
    nPages=300,
    bVersion="Version 2 - Hardcover",
    bGenre=["Drama"],
    bprice=99.99
)
B=Book(
    bookID="DEF1234",
    bookTitle="Andre is mean",
    Author=N,
    nPages=150,
    bVersion="Version 2 - Hardcover",
    bGenre=["Drama"],
    bprice=99.99
)
C=Book(
    bookID="DEF1235",
    bookTitle="Andre is not so mean",
    Author=L,
    nPages=150,
    bVersion="Version 2 - Hardcover",
    bGenre=["Drama"],
    bprice=99.99
)

bookList = [A,B,C]
authorsList = [N,L]

books = BooksandAuthors(bookList,authorsList)

bookid = books.GetBooksbyBookID ("DEF1234")
booktitle = books.GetBooksbyTitle ("Andre is mean")
authorName = books.GetBooksbyAuthorName (N.authorName)
authorID = books.GetBooksbyAuthorID ("456")


author = Author(authorID="456", authorName="Sara", nationality="Italiana", aliveStatus=True)

