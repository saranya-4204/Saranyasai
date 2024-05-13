class Solution:
    def armstrongNumber (self, n):
        # code here 
        sum = 0
        temp = n
        while temp > 0:
           digit = temp % 10
           sum += digit ** 3
           temp //= 10
        if n == sum:
            return("Yes")
        else:
            return("No")
