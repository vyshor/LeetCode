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
    ListNode* removeNodes(ListNode* head) {
        vector<ListNode*> stack;
        ListNode* ptr = head;

        while (ptr != nullptr) {
            while (stack.size() > 0 && stack.back()->val < ptr->val) {
                stack.pop_back();
            }

            stack.push_back(move(ptr));
            ptr = ptr->next;
        }

        for (int i = 0; i < stack.size()-1; i++) {
            stack[i]->next = stack[i+1];
        }
        return stack[0];
    }
};
