# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        #make use of dummy/sentinel node
        dummy=ListNode()
        current=dummy
        carry=0
        while(l1 is not None or l2 is not None):
            sum_val=carry
            if l1:
                sum_val=sum_val+l1.val
                l1=l1.next
            if l2:
                sum_val=sum_val+l2.val
                l2=l2.next
            carry=sum_val//10
            new_node=ListNode(sum_val%10)
            current.next=new_node
            current=current.next
        
        if carry:
            new_node=ListNode(carry)
            current.next=new_node
        return dummy.next
            


 
