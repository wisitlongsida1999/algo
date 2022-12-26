class Solution(object):

    def canJump(self, nums):
        # Concept - Instead of starting from the first element of the
        # Array, think if you have already reached the end, Now check
        # from where have you reached there. In the end your destination
        # should be equal to 0 as we needed to start from first index
        destination = len(nums)-1
        source = destination-1
        
        while source >= 0:
            if source + nums[source] >= destination:
                destination = source
                source-=1
            else:
                source-=1
        return destination == 0

        
inst_tst = Solution()


print(inst_tst.canJump([2,0]))