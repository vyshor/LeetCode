struct Node {
    int idx;
    int total_cost;
    vector<Node*> connect;

    Node(int i): idx(i) {}

    int64_t find(int fro, int target) {
        if (idx == target) return (int64_t(1) << idx);

        for (auto node: connect) {
            if (node->idx == fro) continue;

            int64_t find_cost = node->find(idx, target);
            if (find_cost > 0) return (find_cost | (int64_t(1) << idx));
        }
        return 0;
    }

    pair<int, int> minCost(int fro) {
        int halve = total_cost >> 1, nohalve = total_cost;
        for (auto node: connect) {
            if (node->idx == fro) continue;

            auto [h, nh] = node->minCost(idx);
            nohalve += min(h, nh);
            halve += nh;
        }
        return {halve, nohalve};
    }
};

class Solution {
public:
    unordered_map<int, Node*> nodes;

    int minimumTotalPrice(int n, vector<vector<int>>& edges, vector<int>& price, vector<vector<int>>& trips) {
        for (int i = 0; i < n; i++) {
            nodes[i] = new Node(i);
        }
        for (auto edge: edges) {
            auto fro = nodes[edge[0]], target = nodes[edge[1]];
            fro->connect.push_back(target);
            target->connect.push_back(fro);
        }

        vector<int> node_count(n, 0);
        for (auto trip: trips) {
            int start = trip[0], end = trip[1];
            int64_t bit_mask = nodes[start]->find(-1, end);
            int i = 0;
            while (bit_mask > 0) {
                node_count[i] += (bit_mask & 1);
                bit_mask >>= 1;
                i++;
            }
        }

        for (int i = 0; i < n; i++) {
            nodes[i]->total_cost = node_count[i] * price[i];
        }

        auto [halve, nohalve] = nodes[0]->minCost(-1);
        return min(halve, nohalve);
    }
};
