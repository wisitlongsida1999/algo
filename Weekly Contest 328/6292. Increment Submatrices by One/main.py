# #time limit exceeded
# class Solution(object):
#     def rangeAddQueries(self, n, queries):
#         """
#         :type n: int
#         :type queries: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         ansMat = [[0 for col in range(n)] for row in range(n)]
        
#         for target in queries:
            
#             row1,col1,row2,col2 = target
            
#             for row in range(row1,row2+1):
                
#                 for col in range(col1,col2+1):
                    
#                     ansMat[row][col]+=1
                    
#         return ansMat

        

# revise by implement with numpy

import numpy as np

class Solution(object):
    def rangeAddQueries(self, n, queries):

        ansMat = np.zeros((n, n), dtype=int)
        
        for target in queries:
            
            row1,col1,row2,col2 = target
            
            ansMat[row1:row2+1, col1:col2+1] += 1
                    
        return ansMat