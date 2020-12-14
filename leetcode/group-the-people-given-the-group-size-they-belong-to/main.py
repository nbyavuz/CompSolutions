class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        personList = []
        classDict = {}
        uniqueCount = 0
        for i, person in enumerate(groupSizes):
            if not person in classDict.keys():
                personList.append([i])
                classDict[person] = uniqueCount
                uniqueCount = uniqueCount + 1
            else:
                personList[classDict[person]].append(i)
                
        resultList = []
        for groupSize in classDict.keys():
            arrayIndex = classDict[groupSize]
            for i, personIndex in enumerate(personList[arrayIndex]):
                if i % groupSize == 0:
                    resultList.append([])
                resultList[len(resultList) - 1].append(personIndex)
                
        return resultList 
