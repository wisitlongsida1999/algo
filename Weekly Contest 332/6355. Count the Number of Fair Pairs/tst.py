class Solution(object):
    def countFairPairs(self, n, l, u):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        res = 0
        for i in range(len(n)-1):
            
            for j in range(i+1,len(n)):
                
                if n[i]+n[j] >= l and n[i]+n[j] <= u:
                    
                    res +=1
        
        return res

inst = Solution()

print(inst.countFairPairs([0,0,0,0,0,0], 0, 0))