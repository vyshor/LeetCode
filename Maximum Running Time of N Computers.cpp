class Solution {
public:
    long long maxRunTime(int n, vector<int>& batteries) {
        int n2 = batteries.size();
        if (n > n2) return 0;

        unordered_map<long long, int> counter;
        set<long long, std::greater<long long>> seen;
        long long N = n;
        long long total = 0;
        for (long long battery: batteries) {
            ++counter[battery];
            seen.insert(battery);
            total += battery;
        }

        while (N > 0) {
            long long avg = total / N;
            long long largest = *seen.begin();
            if (largest <= avg) return avg;
            total -= largest;
            --N;
            --counter[largest];
            if (counter[largest] == 0) seen.erase(largest);
        }

        return 0;
    }
};