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
    bool isPalindrome(ListNode* head) {
        auto pt = head;
        vector<int> arr;
        while (pt) {
            arr.push_back(pt->val);
            pt = pt->next;
        }

        int i = 0, j = arr.size()-1;
        while (i < j) {
            if (arr.at(i) != arr.at(j)) return false;
            i++;
            j--;
        }
        return true;
    }
};

