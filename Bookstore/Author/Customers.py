import datetime

class Purchase:
    def __init__(self,bookID,price,dateOfPurchase):
        self.bookID=bookID
        self.price=price
        self.dateOfPurchase=dateOfPurchase


class Customer:
    def __init__(self,customerID,name,status,membership):
        self.customerID=customerID
        self.name=name
        self.status=status
        self.membership=membership
        self.purchaseHistory=[]

    def updateCustomer(self,name,satus,membership):
        self.name=name
        self.status=status
        self.membership=membership5

    def registerPurchase(self,bookID,price,dateOfPurchase):
        newPurchase= Purchase(bookID,price,dateOfPurchase)
        self.purchaseHistory.append(newPurchase)

    


class Customers:
    def __init__(self,customers=[]):
        self.customers=customers

    def AddCustomer(self,name,membership='Bronze'):
        if not membership in ['Bronze', 'Silver','Gold']:
            return False 
        if self.GetCustomerByName(name) is None:
            newKey = str(len(self.customers)+1)
            newCustomer = Customer(newKey,name,'Active',membership)
            self.customers.append(newCustomer)
            return newKey
        return False
    def GetCustomerByName(self, customerName):
        for customer in self.customers:
            if customer.name == customerName:
                return customer
        return None

    def BanMember(self,name):
        currentCustomer=self.GetCustomerByName(name)
        if currentCustomer is None:
            return False
        currentCustomer.status='Banned'

    def ActivateMember(self,name):
        currentCustomer=self.GetCustomerByName(name)
        if currentCustomer is None:
            return False
        currentCustomer.status='Active'

    def DeactivateMember(self,name):
        currentCustomer=self.GetCustomerByName(name)
        if currentCustomer is None:
            return False
        currentCustomer.status='Inactive'

    def GetBannedCustomers(self):
        outList = []
        for customer in self.customers:
            if customer.status == 'Banned':
                outList.append(customer)
        return outList

    def GetBannedCustomerName(self):
        outList = []
        for customer in self.customers:
            print (customer.name)
            if customer.status == 'Banned':
                outList.append(customer.name)
        return outList



Add=Customers()
Add.AddCustomer('Pedro')
'1'
Add.GetCustomerByName
Add.GetCustomerByName('Pedro')
Add.GetCustomerByName('Pedro').purchaseHistory
Add.GetCustomerByName('Pedro').registerPurchase
Add.GetCustomerByName('Pedro').registerPurchase('34',24.50,datetime.datetime.now())
Add.AddCustomer('Maria')
Add.AddCustomer('José')
Add.AddCustomer('Gabriel')
