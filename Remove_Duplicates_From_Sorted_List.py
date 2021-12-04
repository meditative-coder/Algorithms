# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if (head==None or head.next == None):
            return head
        while(temp!=None and temp.next):
            while(temp.next and temp.val == temp.next.val):
                to_del = temp.next
                temp.next = temp.next.next
                del to_del
            temp = temp.next
        return head
