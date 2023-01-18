class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxMain = minMain = 0
        maxTemp = minTemp = nums[0]

        for num in nums[1:]:
            if maxTemp < num:
                maxMain = maxTemp
                maxTemp = num
                
            else:
                maxTemp += num
                
            if minTemp > num:
                minMain = minTemp
                minTemp = num
                
            else:
                minTemp+=num
            
        minMain = min(minTemp,minMain)
        maxMain = max(maxTemp,maxMain)
        sumTotal = sum(nums)

        return max(maxMain,sumTotal-minMain)




insTst = Solution()

print(insTst.maxSubarraySumCircular([1,-2,3,-2]))