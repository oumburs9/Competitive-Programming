# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(merged, (node.val, i, node))
        # print(merged)
        root = ListNode("dump")
        temp = root
        while merged:
            val, ind, node = heapq.heappop(merged)
            temp.next = ListNode(val)
            temp = temp.next
            
            if node.next:
                heapq.heappush(merged, (node.next.val, ind, node.next))
        
        return root.next