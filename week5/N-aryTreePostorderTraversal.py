"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.ans = []
        
    def post_order_traverse(self, node):
        # print('node.val: ',node.val)
        if node.children:
            for child in node.children:
                self.post_order_traverse(child)
        #add node to list on the way up after traversing its children (hence postorder)
        self.ans.append(node.val)
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        self.post_order_traverse(root)
        return self.ans


        