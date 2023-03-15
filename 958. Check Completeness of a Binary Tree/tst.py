class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# In-order traversal (left, root, right)
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

# Pre-order traversal (root, left, right)
def pre_order_traversal(node):
    if node is not None:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

# Post-order traversal (left, right, root)
def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')

# Level-order traversal (Breadth-First Search)
def level_order_traversal(root):
    if root is None:
        return

    queue = [root]
    while queue:
        current_node = queue.pop(0)
        print(current_node.value, end=' ')

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

# Create the nodes
node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)

# Connect the nodes
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6

# Iterate through all nodes using different traversal methods
print("In-order traversal:")
in_order_traversal(node1)
print("\nPre-order traversal:")
pre_order_traversal(node1)
print("\nPost-order traversal:")
post_order_traversal(node1)
print("\nLevel-order traversal:")
level_order_traversal(node1)

print(None and False)