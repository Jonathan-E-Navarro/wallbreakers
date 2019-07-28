# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.total = 0 
        
    def traverse(self,node,branch):
        # print("node: ",node.val)
        if node.left:
            self.traverse(node.left,"left")
        if node.right:
            self.traverse(node.right,"right")
            
        if not node.left and not node.right and branch == "left":
            # print("found a left leaf")
            self.total+=node.val
        
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.traverse(root,"root")
        return self.total
        