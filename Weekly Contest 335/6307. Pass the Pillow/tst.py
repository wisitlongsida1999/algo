class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        if ((time+1)//n)%2 == 0:
            return (time%(n-1))+1
        else:
            return n-(time%(n-1))