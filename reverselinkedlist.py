class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        chead = head
        prev = None
        nxt = None
        while (chead):
            nxt = chead.next
            chead.next = prev
            prev = chead
            chead = nxt
        return prev