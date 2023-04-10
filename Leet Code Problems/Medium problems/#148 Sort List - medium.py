class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        if self.next:
            return f'{self.val} -> {self.next}'
        else:
            return f'{self.val} -> None'

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: empty list or single node list
        if not head or not head.next:
            return head
        
        # Divide the linked list into two halves
        mid = self.get_mid(head)
        left, right = head, mid.next
        mid.next = None
        
        # Recursively sort the two halves
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        # Merge the two sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def get_mid(self, head: ListNode) -> ListNode:
        # Use the two pointers technique to find the midpoint
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node and a pointer to it
        dummy = ListNode()
        cur = dummy
        
        # Compare the values of the nodes in the two lists
        # and append the smaller one to the merged list
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        # Append the remaining nodes of the non-empty list
        cur.next = l1 or l2
        
        # Return the merged list
        return dummy.next
