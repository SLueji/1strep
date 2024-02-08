class Author:
    def __init__(self,authorID,authorName,nationality,aliveStatus=True):
        self.authorID=authorID
        self.authorName=authorName
        self.nationality=nationality+" "
        self.aliveStatus=aliveStatus
        self.books=[]

    def updateInformation(self,authorID,authorName,nationality,aliveStatus=True):
        self.authorID=authorID
        self.authorName=authorName
        self.nationality=nationality
        self.aliveStatus=aliveStatus

    def __str__(self):
        output=""
        output=output+self.authorID+":"+self.authorName+","+self.nationality
        if self.aliveStatus:
            output=output+" "+"Is alive"
        else:
            output=output+" "+"RIP"
        output=output+"."+self.authorName+" has written"+" "+str(len(self.books))+" books"
        return output

