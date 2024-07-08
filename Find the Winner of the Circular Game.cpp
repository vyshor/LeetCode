class Node {
    public:
    Node(int val, Node* next) : val(val), next(next) {}

    int val;
    Node* next;
};

class Solution {
public:
    int findTheWinner(int n, int k) {
        auto head = new Node(1, nullptr);
        auto ptr = head;
        for (int i = 2; i < n+1; i++) {
            ptr->next = new Node(i, nullptr);
            ptr = ptr->next;
        }
        ptr->next = head;

        auto prev = ptr;
        ptr = head;
        int count = k-1;
        while (prev != ptr) {
            if (count == 0) {
                prev->next = ptr->next;
                ptr = ptr->next;
                count = k-1;
            } else {
                prev = ptr;
                ptr = ptr->next;
                count--;
            }
        }
        return ptr->val;
    }
};
