import math

class Solution(object):
    def smallestValue(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        while True:
            
            sum_bf = n
            
            n = self.prime_factors(sum_bf)
            
            sum_af = sum(n)
            
            n = sum(n)
            
            
            if sum_bf ==  sum_af:

                return sum_af
            
            

            
            
        
        
        
    def prime_factors(self,num):  
        
        res = []
        # Using the while loop, we will print the number of two's that divide n  
        while num % 2 == 0:  
            res.append(2)
            num = num / 2  

        for i in range(3, int(math.sqrt(num)) + 1, 2):  

            # while i divides n , print i ad divide n  
            while num % i == 0:  
                res.append(i)
                num = num / i  
        if num > 2:  
            res.append(num)
            
        return res

        
tst = Solution()


print(tst.smallestValue(15))