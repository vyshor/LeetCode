class Solution {
public:
    vector<vector<int>> connections;
    int endIdx;

    int diff(string& geneA, string& geneB) {
        int count = 0;
        for (int i = 0; i < 8; i++) {
            count += (geneA[i] != geneB[i]);
        }
        return count;
    }

    int minMutation(string startGene, string endGene, vector<string>& bank) {
        if (startGene == endGene) return 0;

        bank.push_back(startGene);

        int n = bank.size();
        connections = vector<vector<int>>(n, vector<int>(n, 8));
        bool canEnd = false;

        for (int i = 0; i < n; i++) {
            if (endGene == bank[i]) {canEnd = true; endIdx=i;}
            for (int j = i+1; j < n; j++) {
                int diff_count = diff(bank[i], bank[j]);
                connections[i][j] = diff_count;
                connections[j][i] = diff_count;
            }
        }

        if (!canEnd) return -1;

        vector<pair<int, int>> q;
        q.emplace_back(0, n-1);
        unordered_set<int> visited;

        while (q.size() > 0) {
            pop_heap(q.begin(), q.end());
            auto [cost, i] = q.back();
            q.pop_back();
            if (visited.contains(i)) continue;

            // cout << "i=" << i << " Cost: " << cost << endl;
            visited.insert(i);

            if (endIdx == i) return -cost;
            for (int j = 0; j < n-1; j++) {
                if (visited.contains(j)) continue;
                if (connections[i][j] == 1) {
                    q.emplace_back(cost-connections[i][j], j);
                    push_heap(q.begin(), q.end());
                }
            }
        }
        return -1;
    }
};
