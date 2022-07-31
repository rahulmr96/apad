class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):  ####Reversing a linked list
        prev,cur=None,head

        while cur:
            nxt=cur.next
            cur.next=prev   ###Changing the address
            prev=cur        
            cur=cur.next   ###So you can iterate through it
        return prev

