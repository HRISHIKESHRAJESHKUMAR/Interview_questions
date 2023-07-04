class Employee:
    def __init__(self,empName,designation,salary,overTimeContribution):
        self.empName = empName
        self.designation = designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = False

class Organization:
    def __init__(self,empList):
        self.empList = empList

    def isEligible(self,overTimeThreshold):

        for obj in self.empList:
            totalOverTime = 0
            for k,v in obj.overTimeContribution.items():
                totalOverTime = totalOverTime + v
            
            if totalOverTime >= overTimeThreshold:
                obj.overTimeStatus = True
            
    def totalBonus(self,rate):
        total = 0
        for obj in self.empList:
            if obj.overTimeStatus == True:
                for k,v in obj.overTimeContribution.items():
                    total = total + v*rate
        return total

n=int(input())

obj_list = []
for _ in range(n):
    employee_name = input()
    designation = input()
    salary = int(input())
    overTimeContribution = {}
    for _ in range(int(input())):
        key = input()
        value = int(input())
        overTimeContribution[key] = value
    obj_list.append(Employee(employee_name,designation,salary,overTimeContribution))

org_obj = Organization(obj_list)
overTimeThreshold = int(input())
ratePerHour = int(input())

org_obj.isEligible(overTimeThreshold)
totalBonus = org_obj.totalBonus(ratePerHour)
for i in obj_list:
    print(i.empName,i.overTimeStatus,sep=" ")
print(totalBonus)

