class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        remain = [x - y for x, y in zip(capacity, rocks)]

        remain.sort()

        fullBag = 0
        
        for i in remain:

            additionalRocks-=i
            
            if additionalRocks < 0:

                return fullBag
            
            fullBag +=1

        return fullBag