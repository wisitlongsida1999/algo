class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """

        allGroup = [set()]

        for charIdx in range(len(s1)):
            
            for groupIdx, group in enumerate(allGroup):

                if s1[charIdx] in group or s2[charIdx] in group:
                    
                    allGroup[groupIdx].add(s1[charIdx])
                    allGroup[groupIdx].add(s2[charIdx])
                    break

                allGroup.append({s1[charIdx],s2[charIdx]})



        
        
        res = str()

        for char in baseStr:
            
            notFoundChar = True 
            
            for group in allGroup:
                
                if char in group:
                    
                    lsGroup = list(group)
                    
                    lsGroup.sort()
                    
                    res+=lsGroup[0]

                    notFoundChar = False
                    break

            if notFoundChar:
                res+=char

        return res




insTst = Solution()


print(insTst.smallestEquivalentString(s1 ="cgokcgerolkgksgbhgmaaealacnsshofjinidiigbjerdnkolc",s2 = "rjjlkbmnprkslilqmbnlasardrossiogrcboomrbcmgmglsrsj",baseStr = "bxbwjlbdazfejdsaacsjgrlxqhiddwaeguxhqoupicyzfeupcn") == "axawaaaaazaaaaaaaaaaaaaxaaaaawaaauxaaauaaayzaauaaa" )


# 99 / 116 testcases passed
