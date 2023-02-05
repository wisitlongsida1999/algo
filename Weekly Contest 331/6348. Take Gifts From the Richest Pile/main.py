class Solution(object):
    def pickGifts(self, g, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        import math
        for i in range(k):
            g[g.index(max(g))]= int(math.sqrt(max(g)))
        
        return sum(g)