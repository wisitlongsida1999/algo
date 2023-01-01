class Solution(object):
    def minimumPartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        ls_ans = list()
        idx = 0 
        while(idx < len(s) ):
            
            if int(s[idx]) > k :
                
                return -1
            
            elif int(s[idx]) == k:
                
                ls_ans.append(s[idx])
            
                idx +=1
                
                continue


            elif idx == len(s) - 1:
                
                ls_ans.append(s[idx])
                
                return len(ls_ans)
            
            part_prev = part_curr = s[idx]
            
            for idx_next in range(idx+1,len(s)):
                
                part_curr+=s[idx_next]
                
                if int(part_curr) > k:
                    
                    ls_ans.append(part_prev)
                      
                    idx_next -= 1
                    break
                
                elif int(part_curr) == k:
                    
                    ls_ans.append(part_curr)
                    
                    break
                
                elif idx_next == len(s) - 1:
                    
                    ls_ans.append(part_curr)
                    
                    return len(ls_ans)
                
                part_prev = part_curr
                
            idx+=idx_next-idx+1
            
        
        return len(ls_ans)


inst_tst = Solution()
print(inst_tst.minimumPartition("2995624428278123422153476983795874268215311982758939386251",128))