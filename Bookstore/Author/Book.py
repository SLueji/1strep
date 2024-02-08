from Author import Author
L=Author("1234","João","Portuguesa",False)
N=Author("456","Sara","Italiana")

class Book:
    def __init__(self,bookID,bookTitle,Author,nPages,bVersion,bGenre,bprice):
        self.bookID=bookID
        self.bookTitle=bookTitle
        self.Author=Author
        self.nPages=nPages
        self.bVersion=bVersion
        self.bprice=bprice

    def updateInformation(self,bookID,bookTitle,Author,nPages,bVersion,bGenre,bprice):
        self.bookID=bookID
        self.bookTitle=bookTitle
        self.Author=Author
        self.nPages=nPages
        self.bVersion=bVersion
        self.bprice=bprice

    def __str__(self):
        output=""
        output=output+'Author Name:'+self.Author.authorName+";"+self.bookTitle+";"+str(self.bprice)+'$-'
        return output

    def __repr__(self):
        return str(self)
    
    
#Creating a Book 
book=Book(
    bookID="ABC123",
    bookTitle="Serena's tears",
    Author=N,
    nPages=300,
    bVersion="Version 2 - Hardcover",
    bGenre=["Drama"],
    bprice=99.99
)

L=Author("1234","João","Portuguesa",False)
N=Author("456","Sara","Italiana")
