class Solution:
    def isUgly(self, n):
        if n>1: 
            for i in [2,3,5]:
                while n%i==0:
                    n/=i
        return n==1