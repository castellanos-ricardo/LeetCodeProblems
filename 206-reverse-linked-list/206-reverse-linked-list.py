# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        behind = None
        current = head
        
        while current:
            next = current.next
            current.next = behind
            behind = current
            current = next
        
        
        return behind
            
            
        
        