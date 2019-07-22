# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        put all of nodes into one big list, sort it, then place them into 
        a linked list
        '''
        nodes = []
        new_list = current = ListNode(0)
        
        #iterate through linkedlist and append values to a list
        for l1 in lists:
            while l1:
                nodes.append(l1.val)
                l1 = l1.next
        #sort list containing node values
        nodes.sort()
        
        #iterate through sorted node values and create new sorted LinkedList
        for value in nodes:
            current.next = ListNode(value)
            current = current.next
            
        return new_list.next