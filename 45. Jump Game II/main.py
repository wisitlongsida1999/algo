class Solution:
    def jump(self, nums):
        # Initialize reach (maximum reachable index), count (number of jumps), and last (rightmost index reached)
        reach, count, last = 0, 0, 0
        
        # Loop through the array excluding the last element
        for i in range(len(nums)-1):    
            # Update reach to the maximum between reach and i + nums[i]
            reach = max(reach, i + nums[i])
        
            # If i has reached the last index that can be reached with the current number of jumps
            if i == last:
                # Update last to the new maximum reachable index
                last = reach
                # Increment the number of jumps made so far
                count += 1
        
        # Return the minimum number of jumps required
        return count