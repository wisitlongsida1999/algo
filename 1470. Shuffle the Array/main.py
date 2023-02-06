class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        t = list()
        for i in range(n):
            t.append(nums[i])
            t.append(nums[i+n])
        return t