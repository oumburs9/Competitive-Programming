# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()

        def Merge(dummy, list1, list2):
            # if both is null
            if not list1 and not list2:
                return
            # if list1 is null
            if  not list1 and list2 :
                return list2
            # if list2 is null
            if not list2  and list1 :
                return list1
            
            # if value of list1 is smaller
            if list1.val <= list2.val:
                dummy = list1
                dummy.next = Merge(dummy, list1.next, list2)
                
            # if value of list1 is smaller
            if list1.val > list2.val:
                dummy = list2
                dummy.next = Merge(dummy, list1, list2.next)

            return dummy

        return Merge(dummy, list1, list2)
