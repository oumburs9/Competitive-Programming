# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(None)
        currentVal = ans
        carry = sum1 = 0
        while(l1 or l2):
            sum1 = carry
            if l1:
                sum1 += l1.val
                l1 = l1.next
            if l2:
                sum1 += l2.val
                l2 = l2.next
            carry = int(sum1/10)
            currentVal.next = ListNode(sum1%10)
            currentVal = currentVal.next
        if(carry > 0 ):
            currentVal.next = ListNode(carry)
        return ans.next
