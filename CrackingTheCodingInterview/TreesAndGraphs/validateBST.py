from Tree import BinaryTreeNode

def validateBST(tree):
    if not tree:
        return True

    if tree.left and tree.left.data  > tree.data:
            return False
    
    if tree.right and tree.right.data <= tree.data:
            return False    

    if not validateBST(tree.left) or not validateBST(tree.right):
        return False

    return True


tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)

print(validateBST(tree))

tree = BinaryTreeNode(4)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(6)
tree.left.left = BinaryTreeNode(1)
tree.left.right = BinaryTreeNode(3)
tree.right.left = BinaryTreeNode(5)
tree.right.right = BinaryTreeNode(7)

print(validateBST(tree))