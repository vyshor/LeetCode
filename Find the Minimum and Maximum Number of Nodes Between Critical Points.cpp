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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int minn = INT_MAX, maxx = 0;
        int first_idx = -1, prev_idx = -1;
        int i = 1;

        ListNode* ptr = head->next;
        ListNode* prev = head;
        while (ptr->next) {
            bool critical = (prev->val < ptr->val && ptr->val > ptr->next->val) || (prev->val > ptr->val && ptr->val < ptr->next->val);
            if (critical) {
                if (first_idx == -1) first_idx = i;

                if (prev_idx != -1) {
                    minn = min(minn, i-prev_idx);
                    maxx = i-first_idx;
                }
                prev_idx = i;
            }
            prev = ptr;
            ptr = ptr->next;
            i++;
        }

        if (prev_idx == first_idx) return {-1, -1};
        return {minn, maxx};
    }
};
