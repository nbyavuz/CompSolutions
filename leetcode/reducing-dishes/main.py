class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        maxNumber = satisfaction[-1]
        zeroPos = 0
        if maxNumber <= 0:
            return 0
        for i, number in enumerate(satisfaction):
            if number >= 0:
                zeroPos = i
                break
        negativeList = satisfaction[ : zeroPos]
        positiveList = satisfaction[zeroPos : ]
        positiveSum = sum(positiveList)
        negativeSum = 0
        minIndex = 0
        for i, number in enumerate(reversed(negativeList)):
            negativeSum = negativeSum - number
            if(negativeSum >= positiveSum):
                minIndex = len(negativeList) - i
                break
        resultList = satisfaction[minIndex : ]
        result = 0
        for i, number in enumerate(resultList):
            result = result + (i + 1) * number
        return result
        
