# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        cur = ListNode(0)
        ans = cur

        while (list1 and list2):
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
                cur = cur.next
            else:
                cur.next = list1
                list1 = list1.next
                cur = cur.next
        while (list1):
            cur.next = list1
            list1 = list1.next
            cur = cur.next
        while (list2):
            cur.next = list2
            list2 = list2.next
            cur = cur.next
        return ans.next

s = Solution()

ls1_1 = ListNode(1)
ls1_2 = ListNode(2)
ls1_3 = ListNode(4)

ls1_1.next = ls1_2
ls1_2.next = ls1_3

ls2_1 = ListNode(1)
ls2_2 = ListNode(2)
ls2_3 = ListNode(5)

ls2_1.next = ls2_2
ls2_2.next = ls2_3

res = s.mergeTwoLists(ls1_1,ls2_1)
while(res!=None):
    print(res.val)
    res = res.next
