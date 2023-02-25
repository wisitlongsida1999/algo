class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """

        mx = [p[0],0]
        mn = [p[0],0]
        dt = 0

        for i,j in enumerate(p[1:]):
            i+=1
            if j< mn[0]:
                mn[0] = j
                mn[1] = i
            
            if j > mn[0] and i > mn[1]:

                mx[0] = j
                mx[1] = i

            if mx[0]-mn[0] > dt and mx[1] > mn[1]:
                dt = mx[0]-mn[0]

        return dt

inst = Solution()
print(inst.maxProfit([7,1,5,3,6,4]))
