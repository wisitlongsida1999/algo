# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
    
#     def __init__(self):
        
#         self.temp=0

#         self.temp_l= []

#         self.temp2 = 0
    
#     def isCompleteTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         print(root.val)
#         self.temp_l.append(root.val)
#         if root.left == None and root.right == None:
#             return True

#         if root.left == None and root.right != None:
            
#             return False

#         if root.left != None and root.right == None:
#             self.temp+=1
#             self.temp2 = root.left.val
#             return True
        
       
#         return self.isCompleteTree(root.left) and self.isCompleteTree(root.right) and self.temp<2 and self.temp2 not in self.temp_l


# class Solution(object):
#     def isCompleteTree(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         empty_right = False
        
#         queue = [root]
#         while queue:
#             curNode = queue.pop(0)

#             if curNode.left == None and curNode.right == None:
#                 continue

#             if empty_right:
#                 return False

#             if curNode.left:
#                 queue.append(curNode.left)
#             else:
#                 return False
            
#             if curNode.right:
#                 queue.append(curNode.right)

#             else:
#                 empty_right = True

#         return True


#CR. singhabhinash
import collections
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        is_null_in_between_nodes = False
        while queue:
            total_nodes_in_level = len(queue)
            for i in range(total_nodes_in_level):
                curr_node = queue.popleft()
                if curr_node is None:
                    is_null_in_between_nodes = True
                else:
                    if is_null_in_between_nodes:
                        return False
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
        return True