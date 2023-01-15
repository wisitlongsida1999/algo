class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumDigit = int()
        for num in nums:
    
            sumDigit += sum([int(x) for x in str(num)])
        
        return abs(sum(nums)-sumDigit)