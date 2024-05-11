class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int k) {
        int n = quality.size();
        vector<pair<double, int>> ratio;
        for (int i = 0; i < n; i++) {
            ratio.push_back(make_pair(static_cast<double>(wage[i]) / static_cast<double>(quality[i]), quality[i]));
        }
        sort(ratio.begin(), ratio.end());
        double rate = ratio[k-1].first;
        vector<int> q;
        int total = 0;
        for (int i = 0; i < k; i++) {
            q.push_back(ratio[i].second);
            total += ratio[i].second;
        }
        double minn = rate * static_cast<double>(total);
        make_heap(q.begin(), q.end());
        for (int i = k; i < n; i++) {
            rate = ratio[i].first;
            q.push_back(ratio[i].second);
            push_heap(q.begin(), q.end());
            total += ratio[i].second - q.front();
            pop_heap(q.begin(), q.end());
            q.pop_back();
            minn = min(minn, rate * static_cast<double>(total));
        }

        return minn;
    }
};
