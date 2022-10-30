class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        
        temp = {'pop_creator':[creators[0]]}

        for idx, creator in enumerate(creators):
            if creator not in temp:
                temp.update({creator: {'total_view':views[idx],'clip_idx':idx}})
            else: 
                temp[creator]['total_view'] += views[idx]
                if views[idx]>views[temp[creator]['clip_idx']] or (views[idx]==views[temp[creator]['clip_idx']] and ids[idx] <=ids[temp[creator]['clip_idx']]): 
                        temp[creator]['clip_idx']=idx
                        
            if  temp[creator]['total_view'] == temp[temp['pop_creator'][0]]['total_view'] and creator not in temp['pop_creator']:
                temp['pop_creator'].append(creator)
            elif temp[creator]['total_view'] > temp[temp['pop_creator'][0]]['total_view']:
                temp['pop_creator'] = [creator]
                
        res = []

        for creator in temp['pop_creator']:
            
            res.append([creator,ids[temp[creator]['clip_idx']]])
                
        return res

        

test = Solution()
print(test.mostPopularCreator(creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]))