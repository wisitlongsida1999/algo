class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0

        buf_sum = 0
        seq = 0
        for i,j in enumerate(nums):
            if j == 0:
                seq+=1
            else:
                seq=0

            buf_sum+=seq

        return buf_sum
