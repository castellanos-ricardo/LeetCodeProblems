# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        current = head
        behind = dummy
        
        while(current):
            nxt = current.next
            if(current.val == val):
                behind.next = nxt
            else:
                behind = current
            current = nxt
        
        return dummy.next