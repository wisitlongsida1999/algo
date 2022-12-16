class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Approach 1 : Walk through all index to check pivot
        
        # if sum(nums[1:]) ==0: return 0
        
        # for i in range(1,len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i

        # return -1
        
        # Approach 2 : Similar with the approach 1 but more efficient
        
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1
        
        
        
        # 2 way from mid but not work
        # if sum(nums[1:]) ==0: return 0

        # mid = len(nums)//2-1

        # for i in range(len(nums)):
            
        #     if sum(nums[:mid-i]) == sum(nums[mid-i+1:]):
        #         return mid-i
            
        #     if sum(nums[:mid+i]) == sum(nums[mid+i+1:]):
        #         return mid+i
            
        # return -1



            
        