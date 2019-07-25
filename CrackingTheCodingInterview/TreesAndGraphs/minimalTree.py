from Tree import *

def minimalTreeWrapper(array, start, end):
    if end < start:
        return

    mid = int((start + end) / 2)
    node = BinaryTreeNode(array[mid])
    node.left = minimalTreeWrapper(array, start, mid-1)
    node.right = minimalTreeWrapper(array, mid+1, end)
    return node

def minimalTree(array):
    if not len(array):
        return None

    return minimalTreeWrapper(array, 0, len(array)-1)
    
tree = minimalTree([1,2,3,4,5,6])
bu = BinaryTreeUtils()
bu.inorder_traversal(tree)