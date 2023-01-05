class Solution(object):

    def findMinArrowShots(self, points):

        points.sort(key=lambda p: p[1])

        arr = points[0][1]

        arr_cnt =1 

        for i in range(1,len(points)):

            if points[i][0] <= arr <= points[i][1]:

                continue
            
            else:

                arr = points[i][1]

                arr_cnt+=1

        return arr_cnt

        
inst_tst = Solution()


print(inst_tst.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))