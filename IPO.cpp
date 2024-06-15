class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        int n = profits.size();
        vector<int>q ;
        vector<pair<int, int>> q2;
        for (int i = 0; i < n; i++) {
            if (w >= capital[i]) q.push_back(profits[i]);
            else q2.emplace_back(-capital[i], profits[i]);
        }

        make_heap(q.begin(), q.end());
        make_heap(q2.begin(), q2.end());

        if (q.size() == 0) return w;

        pop_heap(q.begin(), q.end());
        w += q.back();
        q.pop_back();
        k--;

        while (k > 0) {
            while (q2.size() > 0 && -q2[0].first <= w) {
                pop_heap(q2.begin(), q2.end());
                q.push_back(q2.back().second);
                push_heap(q.begin(), q.end());
                q2.pop_back();
            }

            if (q.size() == 0) return w;

            pop_heap(q.begin(), q.end());
            w += q.back();
            q.pop_back();
            k--;
        }
        return w;
    }
};
