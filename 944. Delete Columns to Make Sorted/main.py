class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count_col = 0
        for i in range(len(strs[0])):
            prev = strs[0][i]
            curr = ''
            for j in range(1,len(strs)):
                curr = strs[j][i]
                if ord(prev) > ord(curr):
                    count_col+=1
                    break
                else:
                    prev = curr
        return count_col

            
inst_tst = Solution()


print(inst_tst.minDeletionSize(["rrjk","furt","guzm"]))