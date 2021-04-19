class Solution:
    def reverseWords(self, s: str) -> str:

        if s  == '':
            return ''

        stringList = s.split(' ')

        stringList = [elem for elem in stringList if elem != '']

        return ' '.join(stringList[::-1])
