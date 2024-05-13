class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        n = str(n)
        digit_sum = sum(int(digit) for digit in n)
        if(str(digit_sum) == str(digit_sum)[::-1]):
            return 1
        else:
            return 0
