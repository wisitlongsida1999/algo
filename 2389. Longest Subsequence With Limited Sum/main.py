class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        res = []
        for ans in queries:
            total = 0
            c = 0
            for i in nums:
                if total+i > ans:
                    break
                else: 
                    total+=i
                    c+=1
            res.append(c)
        return res