from Author import Author
L=Author("1234","João","Portuguesa",False)
N=Author("456","Sara","Italiana")


def testCase1():
    if L.authorID != "1234":
        return False
    if L.authorName !="João":
        return False
    if L.nationality !="Portuguesa":
        return False
    if L.aliveStatus == True:
        return False
    return True

def testCase2():
    if N.authorID !="456" or N.authorName !="Sara" or N.nationality !="Italiana" or N.aliveStatus !=True:
        return False
    return True

def testCase3():
    L.updateInformation(L.authorID,L.authorName,"Espanhola",True)
    if L.nationality !="Espanhola"or L.aliveStatus != True:
        return False
    return True


def runtest():
    if not testCase1():
        print ("testCase1 fail")
    else:
        print ("testCase1 pass")
    if not testCase2():
        print ("testCase2 fail")
    else:
        print ("testCase2 pass")
    if not testCase3 ():
        print ("testCase3 fail")
    else:
        print ("testCase3 pass")
    
    
