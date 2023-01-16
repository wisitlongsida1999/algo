class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = list()

        for interval in intervals:
            if newInterval[0] > interval[1] or interval[0] > newInterval[1]:
                res.append(interval)
            else:
                newInterval = [min(newInterval[0],interval[0]),max(newInterval[1],interval[1])]
        res.append(newInterval)
        res.sort()
        return res