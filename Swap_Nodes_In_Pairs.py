# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next==None:
            return head
        temp = ListNode()
        temp.next = head
        current = temp
        while current.next and current.next.next:
            first = current.next
            second = current.next.next
            current.next = second
            first.next = second.next
            second.next = first
            current = current.next.next
        return temp.next
