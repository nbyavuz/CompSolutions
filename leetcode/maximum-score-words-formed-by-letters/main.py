class Solution:
    
    def getIntFromChar(self, letter: str) -> int:
        return ord(letter) - ord('a')
    
    def getPoints(self, word: str, letterDict: dict) -> int:
        
        returnVal = 0
        for elem in word:
            if elem not in letterDict or letterDict[elem] == 0:
                return 0, letterDict
            else:
                returnVal += self.SCORELIST[self.getIntFromChar(elem)]
                letterDict[elem] -= 1
        return returnVal, letterDict
    
    def helperFunc(self, words, letterDict, newLetterDict, turn):
        
        if turn == len(words):
            return 0
        
        calculatedPoints, tempDict  = self.getPoints(words[turn], newLetterDict.copy())
        
        returnVal = 0
        
        if calculatedPoints:
            returnVal = max(returnVal, calculatedPoints + self.helperFunc(words, letterDict, tempDict, turn + 1))
            
        returnVal = max(returnVal, self.helperFunc(words, letterDict, newLetterDict, turn + 1))
        
        return returnVal
    
    
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        letterDict = {}
        self.SCORELIST = score

        for letter in letters:

            if letter not in letterDict:
                letterDict[letter] = 1
            else:
                letterDict[letter] += 1
                
        return self.helperFunc(words, letterDict, letterDict.copy(), 0)
