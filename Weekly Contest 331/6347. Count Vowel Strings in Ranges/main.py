class Solution(object):
    def vowelStrings(self, w, q):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        x = list()
        for l,r in  q:
            c=0
            for i in range(l,r+1):
                if w[i][0] in  ['a','e','i','o','u'] and w[i][-1] in  ['a','e','i','o','u']:

                        c+=1
            x.append(c)

        return x
                        

inst_tst = Solution()             

print(inst_tst.vowelStrings(["bzmxvzjxfddcuznspdcbwiojiqf","mwguoaskvramwgiweogzulcinycosovozppl","uigevazgbrddbcsvrvnngfrvkhmqszjicpieahs","uivcdsboxnraqpokjzaayedf","yalc","bbhlbmpskgxmxosft","vigplemkoni","krdrlctodtmprpxwditvcps","gqjwokkskrb","bslxxpabivbvzkozzvdaykaatzrpe","qwhzcwkchluwdnqjwhabroyyxbtsrsxqjnfpadi","siqbezhkohmgbenbkikcxmvz","ddmaireeouzcvffkcohxus","kjzguljbwsxlrd","gqzuqcljvcpmoqlnrxvzqwoyas","vadguvpsubcwbfbaviedr","nxnorutztxfnpvmukpwuraen","imgvujjeygsiymdxp","rdzkpk","cuap","qcojjumwp","pyqzshwykhtyzdwzakjejqyxbganow","cvxuskhcloxykcu","ul","axzscbjajazvbxffrydajapweci"],[[4, 4],[6, 17],[10, 17],[9, 18],[17, 22],[5, 23],[2, 5],[17, 21],[5, 17],[4, 8],[7, 17],[16, 19],[7, 12],[9, 20],[13, 23],[1, 5],[19, 19]]))