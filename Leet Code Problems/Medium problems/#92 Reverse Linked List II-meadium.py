# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        currentPos = 1
        currentNode = head
        start = head

        while currentPos < left:
            start = currentNode
            currentNode = currentNode.next
            currentPos += 1

        newList = None
        tail = currentNode

        while currentPos >= left and currentPos <= right:
            nextNode = currentNode.next
            currentNode.next = newList
            newList = currentNode
            currentNode = nextNode
            currentPos += 1

        start.next = newList
        tail.next = currentNode

        if left > 1:
            return head
        else:
            return newList

