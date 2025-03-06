from collections import deque
class TreeNode:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None
    
    def inorderTraversal(self,root):
        if not root:
            return
        self.inorderTraversal(root.left)
        print(root.val,end = ' ')
        self.inorderTraversal(root.right)
    def preorderTraversal(self,root):
        if not root:
            return
        print(root.val,end = ' ')
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
    def postorderTraversal(self,root):
        if not root:
            return
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        print(root.val,end = ' ')
    def levelorderTraversal(self,root):
        if not root:
            return
        queue=deque()
        queue.append(root)
        while queue:
            cur=queue.popleft()
            print(cur.val,end=' ')
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    

root=TreeNode(10)
root.left=TreeNode(12)
root.right=TreeNode(5)
root.left.left=TreeNode(3)
root.left.right=TreeNode(8)
root.left.left.left=TreeNode(11)
root.left.right.left=TreeNode(15)
root.right.left=TreeNode(9)
root.right.right=TreeNode(4)
root.right.left.left=TreeNode(1)
root.right.left.right=TreeNode(6)
print("Inorder traversal: ")
root.inorderTraversal(root)
print("\nPreorder traversal: ")
root.preorderTraversal(root)
print("\nPostorder traversal: ")
root.postorderTraversal(root)
print("\nlevelorder traversal: ")
root.levelorderTraversal(root)
 