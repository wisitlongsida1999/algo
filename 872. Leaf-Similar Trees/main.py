# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Approach >>> Create function for recursive and get all leafnode store to temp list then compare each others.
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        self.lsTemp = []

        self.recursToGetLeafNode(root1)

        lsRoot1 = self.lsTemp

        self.lsTemp = []

        self.recursToGetLeafNode(root2)

        lsRoot2 = self.lsTemp

        return lsRoot1 == lsRoot2


    def recursToGetLeafNode(self,root):

        if root.left != None:
            self.recursToGetLeafNode(root.left)
        if root.right != None:
            self.recursToGetLeafNode(root.right)
        
        if root.left == None and root.right == None:

            self.lsTemp.append(root.val)