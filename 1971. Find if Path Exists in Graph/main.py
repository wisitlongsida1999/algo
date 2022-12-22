class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        if source == destination:
            
            return True
        
        temp_ls = [source]
        
        for x in temp_ls:
            
            wait_pop = []

            for a ,b in enumerate(edges):
                i,j = b

                if i == x:
                    if destination == j:
                        
                        return True
                    
                    temp_ls.append(j)
                    wait_pop.append(a)

                elif j == x:

                    if destination == i :
                        
                        return True
                    
                    temp_ls.append(i)
                    wait_pop.append(a)
                    
            temp = 0
            for i in wait_pop:
                
                edges.pop(i-temp)
                temp+=1


        return False