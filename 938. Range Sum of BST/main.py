# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#approach 1 >>> iterate treenode then check if value meeting the criteria
class Solution(object):
    def rangeSumBST(self, root, low, high):
        queue = [root]
        ans = 0
        
        while queue:
            l = queue.pop(0)

            if l.left != None:
                queue.append(l.left)
            if l.right!= None:
                queue.append(l.right)

            if low<= l.val <= high:
                ans+=l.val

        return ans
    
    
#approach 2 >>> just recursive !
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        return self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R) + (root.val if L <= root.val <= R else 0)