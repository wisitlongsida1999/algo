class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_index = len(nums)-1

        jump_index = 0

        while jump_index < last_index:

            if (nums[jump_index] == 0 and  jump_index != last_index ) or (jump_index > last_index):

                return False

            jump_index += nums[jump_index]
            
            if jump_index >= last_index:
                
                return True

        return True