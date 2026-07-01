class ListNode {
public:
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:

    // Separate reverse function
    ListNode* reverse(ListNode* head, int count) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (count > 0 && curr != nullptr) {
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
            count--;
        }

        return prev;
    }

    ListNode* reverseEvenLengthGroups(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        ListNode* prev_group_end = dummy;
        ListNode* curr = head;
        int group_size = 1;

        while (curr != nullptr) {

            // Step 1: count nodes in group
            ListNode* temp = curr;
            int count = 0;

            while (temp != nullptr && count < group_size) {
                temp = temp->next;
                count++;
            }

            // Step 2: reverse if even size
            if (count % 2 == 0) {

                ListNode* reversed_head = reverse(curr, count);

                prev_group_end->next = reversed_head;

                ListNode* tail = curr;

                curr = temp;

                tail->next = curr;

                prev_group_end = tail;

            } else {

                for (int i = 0; i < count; i++) {
                    prev_group_end = curr;
                    curr = curr->next;
                }
            }

            group_size++;
        }

        return dummy->next;
    }
};