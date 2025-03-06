from collections import deque
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,root,val):
        if not root:
            root = Node(val)
            return root
        if val<root.val:
            root.left=self.insert(root.left,val)
        else:
            root.right=self.insert(root.right,val)
        return root
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val,end=' ')
        self.inorder(root.right)

nums=[15,8,18,7,11,24,16]
tree=BST()
for num in nums:
    tree.root=tree.insert(tree.root,num)
tree.inorder(tree.root)