# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        curA = headA
        curB = headB

        s1 = 0
        while curA:
            curA = curA.next
            s1 += 1

        s2 = 0
        while curB:
            curB = curB.next
            s2 += 1

        diff = abs(s1 - s2)

        longer, shorter = 0, 0
        if s1 > s2:
            longer = headA
            shorter = headB
        else:
            longer = headB
            shorter = headA
        
        for _ in range(diff):
            longer = longer.next
        
        while longer:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        return None




        