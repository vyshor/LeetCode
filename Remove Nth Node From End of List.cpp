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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dummyHead = ListNode(0, head);
        int m = 1;
        auto pt = head;
        while (pt->next) {
            pt = pt->next;
            m++;
        }

        m -= n;
        pt = &dummyHead;
        while (m > 0) {
            pt = pt->next;
            m -= 1;
        }
        pt->next = pt->next->next;

        return dummyHead.next;
    }
};
