from collections import deque
class TreeNode:
    def __init__ (self,val):
        self.val=val
        self.left=None
        self.right=None
    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.val,end=' ')
        self.inOrder(root.right)

def levelOrderBuildTree(nums):
    if not nums or nums[0] == 'N':
        return None
    
    n =len(nums)
    root=TreeNode(int(nums[0]))
    queue=deque()
    queue.appendleft(root);
    i=1
    while(queue and i<n):
        cur=queue.pop()
        if(nums[i]!='N'):
            cur.left = TreeNode(int(nums[i]))
            queue.appendleft(cur.left)
        i+=1
        if(i<n and nums[i]!='N'):
            cur.right = TreeNode(int(nums[i]))
            queue.appendleft(cur.right)
        i+=1
    return root


nums=input().split()
root=levelOrderBuildTree(nums)
root.inOrder(root)


