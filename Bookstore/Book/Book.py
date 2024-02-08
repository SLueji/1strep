

class Book:
    def __init__(self,bookID,bookTitle,Author,nPages,bVersion,bGenre,bprice):
        self.bookID=bookID
        self.bookTitle=bookTitle
        self.bAuthor=Author#vai-se buscar à classe feita anteriormente?porque se sim, tenho que mudar a pasta
        self.nPages=nPages
        self.bVersion=bVersion
        self.bprice=bprice

    def updateInformation(self,bookID,bookTitle,Author,nPages,bVersion,bGenre,bprice):
        self.bookID=bookID
        self.bookTitle=bookTitle
        self.bAuthor=Author#vai-se buscar à classe feita anteriormente?
        self.nPages=nPages
        self.bVersion=bVersion
        self.bprice=bprice
        
# Creating a Book instance
book = Book(
    book_id="ABC123",
    title="Serena's tears",
    author=Author,
    n_pages=300,
    version="Version 2 - Hardcover",
    genres=["Drama"],
    price=99.99
)

L=Author("1234","João","Portuguesa",False)
N=Author("456","Sara","Italiana")
