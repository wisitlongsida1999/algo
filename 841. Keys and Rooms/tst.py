# l = [[1,2],[3,4],[5]]


# x = [i for i in rooms[0]]
# for i,j in enumerate(l):
    
#     if i not in x:
        
#         return False
    
#     for k in j:
        
#         x.append(k)
        
    

# print(x)

# return True

# class Solution(object):
#     def canVisitAllRooms(self, rooms):
#         """
#         :type rooms: List[List[int]]
#         :rtype: bool
#         """
#         key = [ x for x in rooms[0]]

#         for i ,j in enumerate(rooms):

#             if i != 0:

#                 if i not in key and len(j) != 0:
        
#                     return False
    
#                 for k in j:
        
#                     key.append(k)

#         return True


l = [1,2]
s = [1]

l = set(l)
s = set(s)

print(l,s)

print( s & l == s)

s.add(2)


print(s)


x = [1]

for i in x:
    
    if i<10:
        
        x.append(i+1)
    
print(x)