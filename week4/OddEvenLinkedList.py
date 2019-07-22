# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        new_list = result = ListNode(0)
        evens = odds = head
        evens = evens.next
        
        while odds != None:
            new_list.next = ListNode(odds.val)
            new_list = new_list.next
            odds = odds.next
            if odds != None:
                odds=odds.next
        
        while evens != None:
            new_list.next = ListNode(evens.val)
            new_list = new_list.next
            evens = evens.next
            if evens != None:
                evens=evens.next
                        
        result=result.next
        return result

        


        