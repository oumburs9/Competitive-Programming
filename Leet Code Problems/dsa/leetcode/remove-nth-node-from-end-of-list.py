# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        ptr1, ptr2 = dummy, dummy
        
        # Find the n forward by ptr1
        for _ in range(n+1):
            ptr1 = ptr1.next
        
        #going to the end by ptr1 
        while ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr2.next = ptr2.next.next

        return dummy.next

        

        