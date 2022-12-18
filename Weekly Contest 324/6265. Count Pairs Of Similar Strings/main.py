class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        ls_of_set = [set(i) for i in words]
        
        res = 0
        
        for i in range(len(ls_of_set)-1):
            
            for j in range(i+1,len(ls_of_set)):
                
                if ls_of_set[i] == ls_of_set[j]:
                    
                    res +=1
                    
        return res


test = Solution()

print(test.similarPairs(["aba","aabb","abcd","bac","aabc"]))