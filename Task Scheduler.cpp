class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        int maxx = tasks.size();
        unordered_map<char, int> counter;
        for (char& task : tasks) {
            if (counter.contains(task)) {
                counter.at(task)++;
            } else {
                counter.insert(make_pair(task, 1));
            }
        }

        vector<int> q;
        q.reserve(counter.size());
        for (auto& p: counter) {
            q.push_back(p.second);
        }
        make_heap(q.begin(), q.end());
        pop_heap(q.begin(), q.end());
        int first_count = q.at(counter.size()-1);
        q.pop_back();
        int first_max = n*(first_count-1)+first_count;
        maxx = max(maxx, first_max);
        while (q.size() > 0 && q.at(0) == first_count) {
            pop_heap(q.begin(), q.end());
            q.pop_back();
            first_max++;
            maxx = max(maxx, first_max);
        }

        return maxx;
    }
};
