# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we have to rearrange the links of odd and even pointers
        if head is None:
            return
        odd=head
        even=head.next
        evenhead=head.next
        # if even reaches null, it means that we reached end of list
        while(even is not None and even.next is not None):
            odd.next=odd.next.next
            odd=odd.next
            even.next=even.next.next
            even=even.next
        odd.next=evenhead
        return head
        

        

        