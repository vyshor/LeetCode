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
    ListNode* doubleIt(ListNode* head) {
        ListNode* dummyHead = new ListNode(0, head);
        ListNode* prev = dummyHead;
        ListNode* ptr = head;
        while (ptr != nullptr) {
            ptr->val *= 2;
            prev->val += ptr->val / 10;
            ptr->val %= 10;
            prev = ptr;
            ptr = ptr->next;
        }
        if (dummyHead->val != 0) {
            return dummyHead;
        }
        return dummyHead->next;
    }
};