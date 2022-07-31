class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = set(nums)
        
        temp.remove(0)

        return len(temp)
        
        
        