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
    vector<ListNode*> splitListToParts(ListNode* head, int k) {
        int n = 0;
        auto ptr = head;
        while (ptr) {
            n++;
            ptr = ptr->next;
        }

        auto m = n / k;
        auto k2 = n % k;
        ptr = head;
        vector<ListNode*> arr;
        while (ptr) {
            arr.push_back(ptr);
            int i = 0;
            while (i < (m - 1 + int(k2 > 0)) && ptr) {
                ptr = ptr->next;
                i++;
            }
            k2--;
            auto nxt = ptr->next;
            ptr->next = nullptr;
            ptr = nxt;
        }

        while (arr.size() < k) {
            arr.push_back(nullptr);
        }
        return arr;
    }
};