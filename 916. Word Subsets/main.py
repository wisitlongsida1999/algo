class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
        temp = []

        for i in words1:
            
            found_word = True
            
            for j in words2:
                
                temp_i = i
                
                for k in j:
                    
                    if k not in temp_i:
                        
                        found_word = False
                        
                        break
                    
                    temp_i = temp_i.replace(k,'',1)
                    
                if not found_word:
                    
                    break
            
            if found_word:
                temp.append(i)
                
        return temp
        
        