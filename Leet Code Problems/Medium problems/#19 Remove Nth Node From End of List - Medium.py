# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        first = head
        second = head

        for i in range(1,n+2):
            first = first.next
        
        while(first):
            first = first.next
            second = second.next
        second.next = second.next.next

        return ans.next


# node creation
n_1 = ListNode(1)
n_2 = ListNode(2)
n_3 = ListNode(3)
n_4 = ListNode(4)

#  node connection

n_1.next = n_2
n_2.next = n_3
n_3.next = n_4
s = Solution()
res = s.removeNthFromEnd(n_1,2)
while (res):
    print(res.val)
    res = res.next

