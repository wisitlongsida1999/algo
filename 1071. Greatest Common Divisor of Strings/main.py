class Solution(object):
    def gcdOfStrings(self, s1, s2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        for i in range(len(s2),0,-1):
            for j in range(0,len(s2),i):
                if s2[j:j+i]*(len(s1)//i) == s1 and  s2[j:j+i]*(len(s2)//i)== s2 :
                    return s2[j:j+i]
        return ''