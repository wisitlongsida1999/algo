class Solution(object):
    def findTheArrayConcVal(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = list()
        while len(n) > 0:
           if len(n)>1:
               t.append(int(str(n.pop(0)) + str(n.pop(-1))  )) 
           else:
               t.append(n.pop(0))
        
        return sum(t)
            