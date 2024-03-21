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
    ListNode* reverseList(ListNode* head) {
        if (!head || !head->next) return head;

        auto pt1 = head, pt2 = head->next;
        pt1->next = nullptr;

        while (pt2) {
            auto pt3 = pt2->next;
            pt2->next = pt1;
            pt1 = pt2;
            pt2 = pt3;
        }

        return pt1;
    }
};
