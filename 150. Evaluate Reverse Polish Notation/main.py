class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        while len(tokens) != 1:

            for i, j in enumerate(tokens):

                if j in ['+','-','*','/']:
                    
                    tokens[i-2]= str(self.revert_operator(int(tokens[i-2]),int(tokens[i-1]),tokens[i]))
                    
                    tokens.pop(i-1)
                    tokens.pop(i-1)
                    
                    break

                
        
        return tokens[0]



    def revert_operator(self,num1,num2,opr):
        
        if opr == '+':
            
            return int(num1+num2)
        elif opr == '-':
            
            return int(num1-num2)

        elif opr == '*':
            return int(num1*num2)

        elif opr == '/':
            return int(num1/num2)
        
        
test = Solution()


print(test.evalRPN(["4","13","5","/","+"]))