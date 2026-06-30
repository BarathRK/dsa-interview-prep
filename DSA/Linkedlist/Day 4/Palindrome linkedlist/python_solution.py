
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head

        # Finding the middle node of the linkedlist
        while(fast!=None and fast.next!=None):
            slow = slow.next
            if(fast.next == None):
                break
            fast = fast.next.next
        
        # Reversing the half
        prev = None
        while(slow!=None):
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        left = head
        right = prev

        #Checking the palindrome condition
        while(right!=None):
            if left.val!=right.val:
                return False
            left = left.next
            right = right.next
        
        return True