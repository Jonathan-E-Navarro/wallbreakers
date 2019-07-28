# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_depth = 0 
        self.max_value = 0 
    def traverse(self,node,depth,branch):
        # print("node: ",node.val,"depth: ",depth)
        if node.left:
            self.traverse(node.left,depth+1,"left")
        if node.right:
            self.traverse(node.right,depth+1,"right")
        
        else:
            #we have a leaf 
            # print(branch," leaf found"," node: ",node.val)
            if branch == "left" and depth > self.max_depth:
                # print("max is a left")
                self.max_depth = depth
                self.max_value = node.val
            elif branch == "right" and depth > self.max_depth:
                # print("max is a right")
                self.max_depth = depth
                self.max_value = node.val
            elif branch == "root" and not node.left and not node.right:
                self.max_value = node.val
        
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.traverse(root,0,"root")
        # print(self.max_value)
        return self.max_value
        