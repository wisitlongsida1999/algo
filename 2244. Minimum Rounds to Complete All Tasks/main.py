
import math

#Approach 1 User for to loop
class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """

        tasks_set = set(tasks)

        min_round = 0

        for lv in tasks_set:

            num_of_lv = tasks.count(lv)

            if num_of_lv == 1 :

                return -1

            min_round+= num_of_lv//3 + math.ceil((num_of_lv%3)/2)

        return int(min_round)




# Approach 2 : Use Two pointers to loop
# class Solution(object):
#     def minimumRounds(self, tasks):
#         """
#         :type tasks: List[int]
#         :rtype: int
#         """

#         tasks_set = set(tasks)

#         tasks_set = list(tasks_set)

#         min_round = 0

#         counter = 0

#         l = 0

#         r = len(tasks_set) -1

#         while l<=r:


#             if l == r:

#                 num_of_lv = tasks.count(tasks_set[l])

#                 if num_of_lv == 1 :

#                     return -1

#                 min_round+= num_of_lv//3 + math.ceil((num_of_lv%3)/2)

#                 break


#             num_of_lv = tasks.count(tasks_set[l])

#             if num_of_lv == 1 :

#                 return -1

#             min_round+= num_of_lv//3 + math.ceil((num_of_lv%3)/2)


#             num_of_lv = tasks.count(tasks_set[r])

#             if num_of_lv == 1 :

#                 return -1

#             min_round+= num_of_lv//3 + math.ceil((num_of_lv%3)/2)



#             l+=1
#             r-=1

#         return int(min_round)

from collections import Counter

class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        freq = Counter(tasks).values()
        return -1 if 1 in freq else sum((a + 2) // 3 for a in freq)

inst_tst = Solution()        

print(inst_tst.minimumRounds([2,3,3]))
