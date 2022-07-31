class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        
        members = len(grades)

        if members <= 2 :
            return 1
    
        line =3
        point = 2
        
        while True :
            
            if members < line+point+1:
                
                break
            
            point+=1
            
            line=line+point
            
        return point