# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def traverse(self,node,node_list):
        # print("node: ",node.val)
        node_list.append(node.val)
        if node.left:
            self.traverse(node.left,node_list)
        else:
            node_list.append(None)
        if node.right:
            self.traverse(node.right,node_list)
        else:
            node_list.append(None)
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p and q or p and not q:
            return False
        
        nl1 = []
        self.traverse(p,nl1)
        # print("nl1: ",nl1)
        nl2 = []
        self.traverse(q,nl2)
        # print("nl2: ",nl2)
        return nl1 == nl2
        