class Solution {
public:
    bool isPalindrome(ListNode* head) {

        ListNode* slow = head;
        ListNode* fast = head;

        // Step 1: Find the middle node
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Step 2: Reverse the second half
        ListNode* prev = nullptr;

        while (slow != nullptr) {
            ListNode* next = slow->next;
            slow->next = prev;
            prev = slow;
            slow = next;
        }

        // Step 3: Compare both halves
        ListNode* left = head;
        ListNode* right = prev;

        while (right != nullptr) {
            if (left->val != right->val) {
                return false;
            }
            left = left->next;
            right = right->next;
        }

        return true;
    }
};