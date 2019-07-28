# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.diameter = 0
    def traverse(self,node):
        #base case we have reached a leaf, begin ascension 
        if not node:
            return 0
        
        # print("node: ",node.val)
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        #path is depth of left children + right children
        #or path from left leaf to right leaf
        path = left+right
        #set diameter to longest path seen so far 
        self.diameter = max(self.diameter, path)
        #return depth of longer branch + 1 to update depth count of recursive call 
        return max(left,right)+1
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.traverse(root)
        # print(self.diameter)
        return self.diameter