
class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        import math
        return (int)(math.sqrt(len(grades) * 2 + 0.25) - 0.5)