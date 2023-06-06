# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []  # Initialize a stack to store values from the first half of the linked list

        fast = head  # Fast pointer to move two steps at a time
        slow = head  # Slow pointer to move one step at a time

        # Find the middle node (slow) and push values to the stack
        while fast and fast.next:
            stack.append(slow.val)

            fast = fast.next.next  # Move fast pointer two steps
            slow = slow.next  # Move slow pointer one step

        if fast is not None:
            slow = slow.next  # Adjust slow pointer for odd-length linked list

        # Compare the remaining half of the linked list with the values in the stack
        while slow and stack:
            if stack.pop() == slow.val:
                slow = slow.next
            else:
                return False

        return True




# # Definition for singly-linked list.
# from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:

    
    
#         stack = []
        
#         fast = head
#         slow = head
        
#         # find the middle (slow) and push to stack
#         while fast and fast.next:
#             stack.append(slow.val)
            
#             fast = fast.next.next
#             slow = slow.next
#         if fast != None:
#             slow = slow.next
#         # print(stack)
#             # stack.append(slow.next.val)

        
#         while slow and stack:
#             if stack.pop() == slow.val:
#                 slow = slow.next
#             else:
#                 return False
#         return True

            
            
            
        
        
        