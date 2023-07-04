class Professor:
    def __init__(self,profId,profName,subjectsDict):
        self.profId = profId
        self.profName = profName
        self.subjectsDict = subjectsDict

class University:
    def getTotalExperience(self,profObjList,profId):
        for obj in profObjList:
            if obj.profId ==profId:
                experience = 0
                for k,v in obj.subjectsDict.items():
                    experience += v
                return experience
            
        return 0
    
    def selectSeniorProfessorBySubject(self,profObjList,subject):
        senior = ''
        mostExp = 0
        for obj in profObjList:
            for k,v in obj.subjectsDict.items():
                if k.lower()==subject.lower():
                    if v > mostExp:
                        v=mostExp
                        senior = obj.profName

        if senior=='':
            return None
        return senior
    
listObj = []
for _ in range(int(input())):
    profId = int(input())
    profName = input()
    n_sub = int(input())
    subjectsDict = {}

    for i in range(n_sub):
        k = input()
        v = int(input())
        subjectsDict[k] = v

    listObj.append(Professor(profId,profName,subjectsDict))

profId = int(input())
subject = input()

university = University()
print(university.getTotalExperience(listObj,profId))
print(university.selectSeniorProfessorBySubject(listObj,subject))


