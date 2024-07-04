/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        auto ptr = head->next;
        auto new_ptr = head;
        int summ = 0;
        while (ptr) {
            while (ptr->val) {
                summ += ptr->val;
                ptr = ptr->next;
            }

            new_ptr->val = summ;
            summ = 0;
            ptr = ptr->next;
            if (ptr) {
                new_ptr = new_ptr->next;
            } else {
                new_ptr->next = nullptr;
            }
        }
        return head;
    }
};
