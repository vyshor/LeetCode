/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (!head || !head->next) return false;
        auto slow = head;
        auto fast = head->next;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;

            if (!fast) return false;

            fast = fast->next;
            if (!fast) return false;
        }
        return true;
    }
};
