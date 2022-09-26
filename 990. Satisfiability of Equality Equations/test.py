class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        ls_op = [equations[0][1],equations[1][1]]
        ls_val = [equations[0][0],equations[0][-1],equations[1][0],equations[1][-1]]

        
        #test 2 states :> equal & not equal

        for i in range(2):
            ls_val_str = ''.join(ls_val)
            ls_val_str = ls_val_str.replace('a','0')
            
            if i == 0:
                ls_val_str = ls_val_str.replace('b','0')
            else:
                ls_val_str = ls_val_str.replace('b','1')
            
            if ls_op[0] == '!':
                
                res_1 = int(ls_val_str[0]) != int(ls_val_str[1])

            else:
                
                res_1 = int(ls_val_str[0]) == int(ls_val_str[1])

            if ls_op[1] == '!':
                
                res_2 = int(ls_val_str[2]) != int(ls_val_str[3])

            else:
                
                res_2 = int(ls_val_str[2]) == int(ls_val_str[3])

            if res_1 and res_2:
                
                return True

                
        return False