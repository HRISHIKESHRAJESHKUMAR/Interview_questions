class Employee:
    def __init__(self,emp_no,emp_name,leaves):
        self.emp_no = emp_no
        self.emp_name = emp_name
        self.leaves = leaves

class Company:
    def __init__(self,cname,emps):
        self.cname = cname
        self.emps = emps
    
    def leave_available(self,emp_no,leaveType):
        for obj in self.emps:
            if  obj.emp_no == emp_no:
                remainL = obj.leaves[leaveType]
                print(remainL)
                return remainL
            
    def leave_permission(self,emp_no,leaveType,noLeaves):
        
        remainL =  self.leave_available(emp_no,leaveType)
        if remainL < noLeaves:
            print("Rejected")

        else:
            print("Granted")

lisObj = []
for _ in range(int(input())):
    emp_no = int(input())
    emp_name = input()
    leaves={}
    leaves['EL'] = int(input())
    leaves['CL'] = int(input())
    leaves['SL'] = int(input())

    lisObj.append(Employee(emp_no,emp_name,leaves))

emp_no = int(input())
leaveType = input()
noLeaves = int(input())

company = Company('Amazon',lisObj)
company.leave_permission(emp_no,leaveType,noLeaves)

