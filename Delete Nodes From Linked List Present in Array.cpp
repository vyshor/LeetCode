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

    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        unordered_set<int> seen(nums.begin(), nums.end());
        ListNode dummy_head(0, head);

        ListNode* prev = &dummy_head;
        ListNode* ptr = head;
        while (ptr) {
            if (seen.contains(ptr->val)) {
                ptr = ptr->next;
            } else {
                prev->next = ptr;
                prev = ptr;
                ptr = ptr->next;
            }
        }
        prev->next = ptr;
        return dummy_head.next;
    }
};