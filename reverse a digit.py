class Solution:
	def reverse_digit(self, n):
		# Code here
		reverse=0
		for i in str(n):
		    digit = n % 10
            reverse = reverse * 10 + digit
            n //= 10
		return abs(reverse)
