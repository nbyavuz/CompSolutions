class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        count = 0
        returnList = []
        lenOfBoxes = len(boxes)
        totalElement = 0
        leftWise = 1 if boxes[0] == '1' else 0
        rightWise = 0 if boxes[0] == '1' else 0
        for i, elem in enumerate(boxes):
            count += int(elem) * i
            if elem == '1':
                rightWise += 1
        
        returnList.append(count)
        
        for elem in enumerate(boxes[1:]):
            if elem == '1':
                rightWise -= 1
            count = count + leftWise - rightWise - int(elem)
            if elem == '1':
                leftWise += 1
            returnList.append(count)
        return returnList
