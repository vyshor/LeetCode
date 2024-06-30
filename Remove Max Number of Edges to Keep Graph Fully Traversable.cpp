class Solution {
public:
    int find(int x, vector<int>& parents) {
        if (parents[x] != x) {
            int main_parent = find(parents[x], parents);
            parents[x] = main_parent;
            return main_parent;
        }
        return x;
    }

    int union_(int x, int y, vector<int>& parents) {
        int parent_x = find(x, parents), parent_y = find(y, parents);
        if (parent_x == parent_y) return 1;
        parents[parent_y] = parent_x;
        return 0;
    }

    int maxNumEdgesToRemove(int n, vector<vector<int>>& edges) {
        vector<int> parents(n);
        for (int i = 0; i < n; i++) {
            parents[i] = i;
        }

        int count = 0;
        int islands = n;
        for (auto edge: edges) {
            int t = edge[0], u = edge[1], v = edge[2];
            if (t == 3) {
                int inc = union_(u-1, v-1, parents);
                count += inc;
                islands += inc-1;
            }
        }

        vector<int> parents_2 = parents;
        int islands2 = islands;

        for (auto edge: edges) {
            int t = edge[0], u = edge[1], v = edge[2];
            if (t == 1) {
                int inc = union_(u-1, v-1, parents);
                count += inc;
                islands += inc-1;
            } else if (t == 2) {
                int inc = union_(u-1, v-1, parents_2);
                count += inc;
                islands2 += inc-1;
            }
        }

        if (islands2 != 1 || islands != 1) return -1;

        return count;
    }
};
