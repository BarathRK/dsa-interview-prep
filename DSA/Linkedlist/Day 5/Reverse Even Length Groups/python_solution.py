class Solution:

    #  Separate reverse function
    def reverse(self, head: ListNode, count: int) -> ListNode:
        prev = None
        curr = head

        while count > 0 and curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count -= 1

        return prev


    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev_group_end = dummy
        curr = head
        group_size = 1

        while curr:

            # Step 1: count actual nodes in this group
            temp = curr
            count = 0

            while temp and count < group_size:
                temp = temp.next
                count += 1

            # Step 2: reverse only if even length
            if count % 2 == 0:
                reversed_head = self.reverse(curr, count)

                # connect previous group to reversed head
                prev_group_end.next = reversed_head

                # curr becomes tail after reversal
                tail = curr

                # move curr forward
                curr = temp

                # connect tail to next group
                tail.next = curr

                prev_group_end = tail

            else:
                # skip normally
                for _ in range(count):
                    prev_group_end = curr
                    curr = curr.next

            group_size += 1

        return dummy.next