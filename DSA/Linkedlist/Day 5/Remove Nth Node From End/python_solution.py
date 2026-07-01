class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        
        # Moving the fast pointer to n steps
        for i in range(n+1):
            fast = fast.next

        # Finding the n th node
        while(fast!=None):  
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return dummy.next