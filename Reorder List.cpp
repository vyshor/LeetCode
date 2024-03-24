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
    void reorderList(ListNode* head) {
        if (!head->next) return;

        auto slow = head;
        auto fast = head->next;
        while (fast->next) {
            fast = fast->next;
            slow = slow->next;

            if (!fast->next) break;
            fast = fast->next;
        }

        auto pt = slow->next;

        slow->next = nullptr;

        auto n = pt->next;
        pt->next = nullptr;
        while (n) {
            auto n2 = n->next;
            n->next = pt;
            pt = n;
            n = n2;
        }

        auto pt1 = head;
        auto pt2 = pt;
        while (pt1 && pt2) {
            auto pt3 = pt2->next;
            pt2->next = pt1->next;
            pt1->next = pt2;
            pt1 = pt1->next->next;
            pt2 = pt3;
        }
    }
};
