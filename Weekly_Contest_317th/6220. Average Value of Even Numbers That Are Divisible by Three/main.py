class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for i in nums:
            if i %3==0 and i%2==0:
                temp.append(i)
        if len(temp) == 0:return 0
        else: return sum(temp)/len(temp)