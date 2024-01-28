# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

    
    
        stack = []
        
        fast = head
        slow = head
        
        # find the middle (slow) and push to stack
        while fast and fast.next:
            stack.append(slow.val)
            
            fast = fast.next.next
            slow = slow.next
        if fast != None:
            slow = slow.next
        # print(stack)
            # stack.append(slow.next.val)

        
        while slow and stack:
            if stack.pop() == slow.val:
                slow = slow.next
            else:
                return False
        return True
            
            
            
        
        
        