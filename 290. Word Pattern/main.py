class Solution(object):
    def wordPattern(self, pattern, s):

        map_dict = dict()

        s = s.split(' ')

        if len(set(pattern))!= len(set(s)) or len(s) != len(pattern):

            return False

        for i,j  in enumerate(pattern):  

            if j in map_dict:

                if map_dict[j] != s[i]:

                    return False
                
            else:

                map_dict[j] = s[i]

        return True