class Solution(object):
    def divisibilityArray(self, w, m):
        t = list()
        for i in range(0,len(w)):
            if int(w[:i+1]) %m == 0:
                t+=[1]
            else:
                t+=[0]
        return t