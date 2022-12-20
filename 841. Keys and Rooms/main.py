class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        keys = [x for x in rooms[0]]

        for i in keys:
            
            for j in rooms[i]:
                
                if j not in keys:

                    keys.append(j)
                
        lock_room = []

        for  i,j in enumerate(rooms):

            if j != [] and i != 0:
                lock_room.append(i)

        return set(keys) & set(lock_room) == set(lock_room)




inst_tst = Solution()

print(inst_tst.canVisitAllRooms([[1],[2],[3],[]]))
            