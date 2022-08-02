class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        temp_ls = []
        for i in matrix:
            temp_ls.extend(i)
            
        temp_ls.sort()
        
        return temp_ls[k-1]