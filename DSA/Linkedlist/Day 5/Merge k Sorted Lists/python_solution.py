import heapq


class Solution:
    def mergeKLists(self, lists):
        min_heap = []

        # Step 1: push all head nodes into heap
        for node in lists:
            if node:
                heapq.heappush(min_heap, (node.val, node))

        dummy = ListNode(0)
        tail = dummy

        # Step 2: process heap
        while min_heap:
            _, node = heapq.heappop(min_heap)

            tail.next = node
            tail = tail.next

            # push next node from same list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, node.next))

        return dummy.next