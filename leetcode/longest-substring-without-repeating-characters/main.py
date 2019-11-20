class Solution:
    def lengthOfLongestSubstring(self, inputString: str) -> int:
        stringLength = len(inputString)
        if stringLength == 0:
            return 0
        templateString = ''
        result = 0
        for i in range(0, stringLength):
            element = inputString[i]
            if element not in templateString:
                templateString = templateString + element
                tempMax = len(templateString)
            else:
                templateString = templateString + element
                templateString = templateString[templateString.find(element) + 1:]
                if tempMax > result:
                    result = tempMax
        if tempMax > result:
            result = tempMax
        if result == 0:
            return tempMax
        else:
            return result
