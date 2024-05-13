class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        a = a2-a1
        s = a1+(n-1)*a
        return s
        
