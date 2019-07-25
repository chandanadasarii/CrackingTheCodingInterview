import sys

class BinaryTreeNode():
    
    left = None
    right = None
    
    def __init__(self, data):
        self.data = data


class BinaryTree():

    def preorder_traversal(self, root):
        if root:
            print(root.data)
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)


    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

        
    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data)


    def non_recursive_preorder_traversal(self, root):
        stack = list()
        while(1):
            while(root):
                print(root.data)
                stack.append(root)
                root = root.left
            if not len(stack):
                return
            root = stack.pop()
            root = root.right


    def non_recursive_inorder_traversal(self, root):
        stack = list()
        while(1):
            while(root):
                stack.append(root)
                root = root.left
            if not len(stack):
                return
            root = stack.pop()
            print(root.data)
            root = root.right


    def non_recursive_postorder_traversal(self, root):
        stack = list()
        while(1):
            while(root):
                stack.append(root)
                root = root.left
            while(root is None and len(stack)):
                root = stack[-1]
                if (root.right is None or root.right == prev):
                    print(root.data)
                    stack.pop()
                    prev = root
                    root = None
                else:
                    root = root.right
            if not len(stack):
                return


    def level_order_traversal(self, root):
        queue = list()
        if root:
            queue.append(root)
            while queue:
                temp = queue.pop(0)
                print(temp.data)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)



    def find_max(self, root):
        max = None
        if root:
            cur_data = root.data
            left = self.find_max(root.left)
            right = self.find_max(root.right)
            if left is not None and right is not None:
                if left > right:
                    max = left
                else:
                    max = right
            if max is None or max < cur_data:
                max = cur_data
        return max

    
    def find_max_using_level_order(self, root):
        queue = list()
        max = None
        if root:
            queue.append(root)
            while queue:
                temp = queue.pop(0)
                if max is None or temp.data > max:
                    max = temp.data
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return max


    def find(self, root, value):
        if root:
            if root.data == value:
                return True
            ret = self.find(root.left, value)
            if not ret:
                return self.find(root.right, value)
            else:
                return ret
        else:
            return False


    def insert(self, root, new_node):
        queue = list()
        if root:
            queue.append(root)
            while queue:
                temp = queue.pop(0)
                if temp.left is None:
                    temp.left = new_node
                    return
                else:
                    queue.append(temp.left)
                if temp.right is None:
                    temp.right = new_node
                    return
                else:
                    queue.append(temp.right)


    def sizeoftree(self, root):
        # size=0
        if root:
            return self.sizeoftree(root.left) + 1 + self.sizeoftree(root.right)
        else:
            return 0


    def heightoftree(self, root):
        if root:
            leftheight = self.heightoftree(root.left)
            rightheight = self.heightoftree(root.right)
            if leftheight > rightheight:
                return leftheight+1
            else:
                return rightheight+1
        else:
            return 0

tree = BinaryTreeNode(1)
tree.left = BinaryTreeNode(2)
tree.right = BinaryTreeNode(3)
tree.left.left = BinaryTreeNode(4)
tree.left.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(6)
tree.right.right = BinaryTreeNode(7)

btree = BinaryTree()

# btree.preorder_traversal(tree)
# btree.non_recursive_preorder_traversal(tree)
# btree.inorder_traversal(tree)
# btree.non_recursive_inorder_traversal(tree)
# btree.postorder_traversal(tree)
# btree.non_recursive_postorder_traversal(tree)
# btree.level_order_traversal(tree)
# print(btree.find_max(tree))
# print(btree.find_max_using_level_order(tree))
# print(btree.find(tree, 4))
# print(btree.find(tree, 9))
# btree.insert(tree, BinaryTreeNode(8))
# btree.level_order_traversal(tree)
# btree.insert(tree, BinaryTreeNode(9))
# btree.level_order_traversal(tree)
# print(btree.sizeoftree(tree))
print(btree.heightoftree(tree))
btree.insert(tree, BinaryTreeNode(8))
print(btree.heightoftree(tree))