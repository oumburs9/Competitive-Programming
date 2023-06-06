# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head):
            return head

        odd = head
        even = odd.next
        evenList = even

        while (even and even.next):
            odd.next = even.next
            odd = odd.next

            evenList.next= odd.next
            even = even.next
        odd.next = evenList
        return head


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
res = s.oddEvenList(n_1)
while (res):
    print(res.val)
    res = res.next
