class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if lower <= nums[i] + nums[j] <= upper:
                    res += 1
        return res
