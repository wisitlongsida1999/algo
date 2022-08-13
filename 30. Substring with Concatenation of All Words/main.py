class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        
        temp = []
        
        res = []

        l_words = len(words[0])


        for i in range(len(s)):

            for k in words:
                temp.append(k)
            j= i
            while True:
                
                if len(temp) == 0:
                    
                    res.append(i)
                    
                    break
                
                if s[j:j+l_words] in temp: 

                    temp.remove(s[j:j+l_words])

                    j+=l_words

                else:
                    
                    break
                
            temp = []
                
        return res
                    
                    


            
            
test = Solution()

print(test.findSubstring("barfoothefoobarman", ["foo","bar"]))