from Tree import *

def getHeight(tree):
    if tree == None:
        return 0

    return 1 + max(getHeight(tree.left), getHeight(tree.right))


def checkBalanced(tree):
    if tree == None:
        return False
    
    lh = getHeight(tree.left)
    if lh == -1:
        return -1

    rh = getHeight(tree.right)
    if rh == -1:
        return -1

    if abs(lh-rh) > 1:
        return -1
    else:
        return 1 + max(lh, rh)


tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)
tree.right.right.right = BinaryTreeNode(8)
tree.right.right.right.right = BinaryTreeNode(9)

print(checkBalanced(tree))

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)

print(checkBalanced(tree))