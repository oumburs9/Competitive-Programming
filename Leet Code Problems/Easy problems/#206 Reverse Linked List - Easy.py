# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

s = Solution()
ls2_1 = ListNode(1)
ls2_2 = ListNode(2)
ls2_3 = ListNode(5)

ls2_1.next = ls2_2
ls2_2.next = ls2_3

res = s.reverseList(ls2_1)
while(res!=None):
    print(res.val)
    res = res.next