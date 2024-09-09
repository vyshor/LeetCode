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
    vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
        vector<vector<int>> matrix;
        for (int i = 0; i < m; i++) {
            matrix.emplace_back(n, -1);
        }

        int i = 0, j = -1;
        vector<pair<int, int>> dirs = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0}
        };

        int direct = 0;
        auto ptr = head;
        auto [delta_x, delta_y] = dirs[direct];
        while (ptr) {
            if ((i+delta_x < 0) || (i+delta_x >= m) || (j+delta_y < 0) || (j +delta_y >= n) || (matrix[i+delta_x][j+delta_y] != -1)) {
                direct++;
                direct %= 4;

                delta_x = dirs[direct].first;
                delta_y = dirs[direct].second;
            }

            i += delta_x;
            j += delta_y;
            // cout << i << " " << j << endl;
            matrix[i][j] = ptr->val;
            ptr = ptr->next;
        }
        return matrix;
    }
};
