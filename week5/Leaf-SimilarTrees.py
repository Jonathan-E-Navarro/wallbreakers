# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def traverse(self,node,sequence):
        # print("node: ",node.val)
        if node.left:
            self.traverse(node.left,sequence)
        if node.right:
            self.traverse(node.right,sequence)
        elif not node.left and not node.right:
            # print("adding leaf")
            sequence.append(node.val)
            
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        sequence1 = []
        self.traverse(root1,sequence1)
        print(sequence1)
        sequence2 = []
        self.traverse(root2,sequence2)
        print(sequence2)
        
        return sequence1 == sequence2