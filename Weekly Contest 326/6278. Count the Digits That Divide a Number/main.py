class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res_buf = list()
        
        str_num = str(num)
        
        for digit in str_num:
            
            if num % int(digit) == 0:
            
                res_buf.append(digit)
                
        return len(res_buf)