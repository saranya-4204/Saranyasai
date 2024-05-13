class Solution:
	def find_median(self, v):
		# Code here
		v.sort()
		a = len(v)
		if(a%2==0):
		    s = ((v[a//2])+(v[(a//2)-1]))//2
		    return s
		    
		else:
		    return v[a//2]
