# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hare = head
        turtle = head
        while hare and turtle and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if turtle == hare:
                return True
        return False


s = Solution()
ls2_1 = ListNode(1)
ls2_2 = ListNode(2)
ls2_3 = ListNode(6)
ls2_4 = ListNode(7)
ls2_5 = ListNode(9)



ls2_1.next = ls2_2
ls2_2.next = ls2_3
ls2_3.next = ls2_4

ls2_4.next = ls2_2

# ls2_4.next = ls2_5


res = s.hasCycle(ls2_1)
print(res)
# while(res!=None):
#     print(res.val)
#     res = res.next

