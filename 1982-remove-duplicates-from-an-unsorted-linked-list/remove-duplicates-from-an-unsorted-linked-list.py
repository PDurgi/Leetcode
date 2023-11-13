# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        counts={}
        current=head
        while current:
            if current.val in counts:
                counts[current.val]=counts[current.val]+1
                
            else:
                counts[current.val]=1
            current=current.next
            
        temp=head
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        while temp :
            if counts[temp.val] >1:
                temp=temp.next
                prev.next=temp
                
            else:   
                prev=prev.next
                temp=temp.next
        return dummy.next