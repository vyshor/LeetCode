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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        b += 2 - a;
        
        auto pt = list1;
        while (a > 1) {
            pt = pt->next;
            a--;
        }

        auto pt2 = pt;
        while (b > 0) {
            pt2 = pt2->next;
            b--;
        }

        pt->next = list2;
        while (pt->next) pt = pt->next;
        pt->next = pt2;
        return list1;
    }
};
