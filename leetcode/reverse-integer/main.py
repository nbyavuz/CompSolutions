class Solution:
    def reverse(self, number: int) -> int:
        negativeFlag = False
        if number == 0:
            return 0
        stringNumber = str(number)
        if stringNumber[0] == '-':
            negativeFlag = True
            stringNumber = stringNumber[1:]
        stringNumber = stringNumber[::-1].lstrip('0')
        if negativeFlag:
            stringNumber = '-' + stringNumber
        if -2147483648 < int(stringNumber) < 2147483648:
            return stringNumber
        return 0
