class Solution {
public:
    ListNode *detectCycle(ListNode *head) {

        ListNode *slow = head;
        ListNode *fast = head;

        // Step 1: Detect if a cycle exists
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;

            if (slow == fast) {
                break;
            }
        }

        // No cycle found
        if (fast == nullptr || fast->next == nullptr) {
            return nullptr;
        }

        // Step 2: Find the starting node of the cycle
        slow = head;

        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }

        return slow;
    }
};