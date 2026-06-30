class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while(fast!=None and fast.next!=None):
            slow = slow.next
            if(fast.next == None):
                return slow
            fast = fast.next.next
        return slow