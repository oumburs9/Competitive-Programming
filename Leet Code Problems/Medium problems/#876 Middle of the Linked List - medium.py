# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        hare = tort = head
        
        while( hare and hare.next):
            tort = tort.next
            hare = hare.next.next
        return tort
            
        