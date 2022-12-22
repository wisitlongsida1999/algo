class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        g1 = set()
        g2 = set()
        for i in dislikes:

            if set(i).issubset(g1) or set(i).issubset(g2): 

                return False

            if i[0] in g1:
                g2.add(i[1])

            elif i[0] in g2:
                g1.add(i[1])

            elif i[1] in g1:
                g2.add(i[0])
            
            elif i[1] in g2:
                g1.add(i[0])

            else:
                g1.add(i[0])
                g2.add(i[1])

        return True

inst_tst = Solution()
print(inst_tst.possibleBipartition(10,[[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]))