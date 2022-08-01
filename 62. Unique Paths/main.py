class Solution: 
        def uniquePaths(self, m, n):
            import math
            return math.factorial(m+n-2)//math.factorial(m-1)//math.factorial(n-1)