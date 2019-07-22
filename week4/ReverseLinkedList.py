# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return 

        new_head = ListNode(head.val)
        head=head.next
        
        while head != None:
            copy = ListNode(head.val)
            copy.next = new_head
            new_head = copy  
            head=head.next
                    
        return new_head

            