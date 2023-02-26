class Solution(object):
    def leftRigthDifference(self, n):
        t = list()
        for i ,j in enumerate(n):
            t.append(abs(sum(n[:i])-sum(n[i+1:])))
        return t