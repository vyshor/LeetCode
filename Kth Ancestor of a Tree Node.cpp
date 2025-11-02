class TreeAncestor {
public:
    int M;
    int N;
    vector<vector<int>> up;

    TreeAncestor(int n, vector<int>& parent) {
        N = n+1;
        int n2 = N;
        M = 1;
        while (n2 != 0) {
            M++;
            n2 >>= 1;
        }

        parent.push_back(N-1);
        parent[0] = N-1;
        up = vector<vector<int>>(N, vector<int>(M, -1));
        for (int i = 0; i < N; i++) {
            up[i][0] = parent[i];
        }

        for (int j = 1; j < M; j++) {
            for (int i = 0; i < N; i++) {
                up[i][j] = up[up[i][j-1]][j-1];
            }
        }
    }

    int getKthAncestor(int node, int k) {
        for (int i = 0; i < M; i++) {
            if (k & (1 << i)) {
                node = up[node][i];
            }
        }

        if (node == N-1) return -1;
        return node;
    }
};

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor* obj = new TreeAncestor(n, parent);
 * int param_1 = obj->getKthAncestor(node,k);
 */
