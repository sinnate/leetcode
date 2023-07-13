# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # if no head return head funnny 
        if not head or not head.next : return head
        head_giver = previous_head = ListNode(0)
        previous_head.next = head
        while head and head.next:
            if head.val >= x and head.next.val<x:
                # 0 - > 0 - > 
                temp = head.next.next
                head.next.next = previous_head.next
                previous_head.next = head.next
                head.next = temp
            else :
                head = head.next
            if previous_head.next.val < x :
                previous_head=previous_head.next
        return head_giver.next