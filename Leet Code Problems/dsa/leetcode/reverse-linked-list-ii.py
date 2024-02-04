# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        prev , cur ,count = None,head ,1

        while cur is not None and count < left:
            prev = cur
            cur = cur.next
            count += 1

        last_node_of_first_part = prev
        last_node_of_sub_list_part = cur
        
        
        while cur  and count <= right:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            count +=1

        if last_node_of_first_part is not None:
            last_node_of_first_part.next = prev
        else:
            head = prev

        last_node_of_sub_list_part.next = cur
        return head
       

