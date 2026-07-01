class ListNode {
    int val;
    ListNode next;
    ListNode(int val) {
        this.val = val;
    }
}

class Solution {

    // Separate reverse function
    public ListNode reverse(ListNode head, int count) {
        ListNode prev = null;
        ListNode curr = head;

        while (count > 0 && curr != null) {
            ListNode nxt = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nxt;
            count--;
        }

        return prev;
    }

    public ListNode reverseEvenLengthGroups(ListNode head) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prevGroupEnd = dummy;
        ListNode curr = head;
        int groupSize = 1;

        while (curr != null) {

            // Step 1: count nodes in group
            ListNode temp = curr;
            int count = 0;

            while (temp != null && count < groupSize) {
                temp = temp.next;
                count++;
            }

            // Step 2: reverse if even size
            if (count % 2 == 0) {

                ListNode reversedHead = reverse(curr, count);

                prevGroupEnd.next = reversedHead;

                ListNode tail = curr;

                curr = temp;

                tail.next = curr;

                prevGroupEnd = tail;

            } else {

                for (int i = 0; i < count; i++) {
                    prevGroupEnd = curr;
                    curr = curr.next;
                }
            }

            groupSize++;
        }

        return dummy.next;
    }
}