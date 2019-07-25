from Tree import BinaryTreeNode
from Tree import BinaryTreeUtils

class BSTUtils:

    minval = float('inf')
    prevval = float('-inf')

    def minDistanceBST(self, root):

        if root == None:
            return None
        
        self.minDistanceBST(root.left)
        
        self.minval = min(self.minval, abs(root.data - self.prevval))
        self.prevval = root.data

        self.minDistanceBST(root.right)

        return self.minval


tree = BinaryTreeNode(17)
tree.left = BinaryTreeNode(10)
tree.right = BinaryTreeNode(25)
tree.left.left = BinaryTreeNode(7)
tree.left.right = BinaryTreeNode(12)
tree.right.left = BinaryTreeNode(19)
tree.right.right = BinaryTreeNode(32)

# BinaryTreeUtils().inorder_traversal(tree)

print(BSTUtils().minDistanceBST(tree))