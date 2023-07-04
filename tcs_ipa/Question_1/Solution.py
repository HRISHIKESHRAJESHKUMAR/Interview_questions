class Account:
    def __init__(self,cardNo,pin,balance,lastWithAmount,accountType):
        self.cardNo = cardNo
        self.pin = pin
        self.balance = balance
        self.lastWithAmount = lastWithAmount
        self.accountType = accountType
        
    def withdrawal(self,withAmount):
        if withAmount<=self.balance:
            newBalance = self.balance - withAmount
            self.balance = newBalance
            self.lastWithAmount = withAmount
            print(self.cardNo,self.balance,self.lastWithAmount)
        
class ATM:
    def __init__(self,branchName,accountList):
        self.branchName = branchName
        self.accountList = accountList
        
    def withdrawal(self,cardNo,pin,withAmount):
        for account in self.accountList:
            if account.cardNo == cardNo and account.pin == pin:
                account.withdrawal(withAmount)
                return
        
        print("No account exists")
        
    
    def filterAccounts(self,accountType):
        details={}
        flag = 0 
        for account in self.accountList:
            if account.accountType == accountType:
                details[account.cardNo] = account.balance
                flag = 1
        if flag==0:
            print("No match found")
            return
            
        return details
        
accObjList=[]

for _ in range(int(input())):
    cardNo = int(input())
    pin = int(input())
    balance = float(input())
    withAmount = float(input())
    accountType = input()
    
    accObjList.append(Account(cardNo,pin,balance,withAmount,accountType))
    
atm = ATM('HDFC',accObjList)

cardNo = int(input())
pin = int(input())
withAmount = float(input())
accountType = input()

atm.withdrawal(cardNo,pin,withAmount)

details = atm.filterAccounts(accountType)

for k,v in details.items():
    print(k,v)