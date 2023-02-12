class Solution:
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        concat_value = 0
        while nums:
            if len(nums) > 1:
                first = nums.pop(0)
                last = nums.pop(-1)
                concat_value += int(str(first) + str(last))
            else:
                concat_value += nums.pop(0)
        return concat_value
