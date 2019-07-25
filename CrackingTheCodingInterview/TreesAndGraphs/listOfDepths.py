from Tree import BinaryTreeNode

def listOfDepths(treenode, treelists, level=0):
    if treenode is None:
        return

    if len(treelists) == level:
        treelists.append([])
    treelists[level].append(treenode.data)

    listOfDepths(treenode.left, treelists, level+1)
    listOfDepths(treenode.right, treelists, level+1)    
    return treelists


def listOfDepthsBFS(treenode):
    if treenode is None:
        return 

    treelists = list()
    current = list()
    current.append(treenode)
    data = list()
    data.append(treenode.data)

    while len(current):
        treelists.append(data)
        parents = current
        current = list()
        data = list()

        for parent in parents:
            if parent.left:
                current.append(parent.left)
                data.append(parent.left.data)
            if parent.right:
                current.append(parent.right)
                data.append(parent.right.data)

    return treelists

    


tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)

print(listOfDepths(tree, []))
print(listOfDepthsBFS(tree))