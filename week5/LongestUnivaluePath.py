# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.uni_path = 0
        
    def traverse(self,node):
        '''
        same idea as diameter of a binary tree
        only we check the nodes values on the way back up 
        if they dont match, then we don't add depth to the current nodes path
        '''
        if not node:
            # print("leaf node found")
            return 0 
        # print("node: ",node.val)
        left_branch = self.traverse(node.left)
        right_branch = self.traverse(node.right)
        
        #if our left child existed, check whetehr it matches this current nodes value 
        #else we do not count the right child's depth for this path 
        left_depth = left_branch+1 if node.left and node.val == node.left.val else 0 

        #if our right child existed, check whetehr it matches this current nodes value 
        #else we do not count the right child's depth for this path 
        right_depth = right_branch+1 if node.right and node.val == node.right.val else 0 
                
        #longest possible path is from deepest valid left child to deepest valid right child 
        path = left_depth+right_depth
        self.uni_path = max(self.uni_path,path)
        #as we recurse up, we only care about the path of the longest child to add to new path 
        return max(left_depth,right_depth)
        
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.traverse(root)
        # print(self.uni_path)
        return self.uni_path