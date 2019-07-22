# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
[1,2,3,4,5,6,7,8]

'''

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 0:
            return head
        ans = temp = ListNode(0)
        count = 0
        stack = []
        while head!=None:
            while count < k and head!= None:
                # print("appending node: ",head.val)
                stack.append(head)
                count+=1
                head=head.next
                # print(stack)
            
            if count == k:
                while len(stack)!=0:
                    temp.next = ListNode(stack.pop().val)
                    # print("popping off: ",temp.next)
                    temp=temp.next
                print(ans)
            
            count = 0
            # head=head.next
        for node in stack:
            temp.next = ListNode(node.val)
            temp=temp.next
        # print("done!")
        return ans.next


