class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Solution 1 walk through array
        buf = 0
        res = []
        for i in nums:
            buf+=i
            res.append(buf)

        return res
        
        
        