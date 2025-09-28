class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int k;
        int count = 0;
        for (int i = 0; i < n-2; i++) {
            if (nums[i] == 0) continue;
            k = i+2;
            for (int j = i+1;j < n-1; j++) {
                while (k < n && nums[k] < nums[i] + nums[j]) {
                    k++;
                }
                count += k - j - 1;
                // cout << "j: " << j << " k: " << k << " count: " << count << endl;
            }
        }
        return count;
    }
};

class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int total_count = nums.size();
        vector<int> uni_num;
        unordered_map<int, int> counter;
        for (int num: nums) {
            if (num == 0) continue;
            counter[num]++;
            if (counter[num] == 1) uni_num.push_back(num);
        }

        sort(uni_num.begin(), uni_num.end());
        int n = uni_num.size();
        int summ = 0;
        vector<pair<int, int>> arr;
        arr.resize(n);

        for (int i = n-1; i >= 0; i--) {
            int num = uni_num[i];
            summ += counter[num];
            arr[i].first = num;
            arr[i].second = summ;

            // cout << num << ": " << summ << endl;
        }

        int triplets = 0;
        for (int i = 0; i < n; i++) {
            int num = uni_num[i];
            int count = counter[num];
            if (count > 2) {
                triplets += (count * (count - 1) * (count - 2)) / 6;
            }
        }

        // cout << "Count same triplets: " << triplets << endl;

        for (int i = 0; i < n; i++) {
            int num = uni_num[i];
            int count = counter[num];
            if (count > 1) {
                pair<int, int> v = {num + num, 0};
                auto ptr = upper_bound(arr.begin(), arr.end(), v);
                if (ptr != arr.end()) {
                    triplets += count * (count-1) * (arr[i].second - count - ptr->second) / 2;
                } else {
                    triplets += count * (count-1) * (arr[i].second - count) / 2;
                }
            }
        }
        // cout << "Include 2 num same triplets: " << triplets << endl;

        for (int i = 0; i < n-1; i++) {
            for (int j = i+1; j < n; j++) {
                int first = arr[i].first;
                int second = arr[j].first;
                if (counter[second] > 1) {
                    triplets += counter[first] * (counter[second] * (counter[second]-1)) / 2;
                }
            }
        }

        for (int i = 0; i < n-2; i++) {
            for (int j = i+1; j < n-1; j++) {
                int first = arr[i].first;
                int second = arr[j].first;
                pair<int, int> v = {first + second, 0};
                auto ptr = upper_bound(arr.begin(), arr.end(), v);

                int inc;
                if (ptr != arr.end()) {
                    inc = counter[first] * counter[second] * (arr[j].second - counter[second] - ptr->second);
                } else {
                    inc = counter[first] * counter[second] * (arr[j].second - counter[second]);
                }
                triplets += inc;
                // cout << "First: " << first << " Second: " << second << " Pos:" << ptr - arr.begin() << " Inc: " << inc << endl;
            }
        }

        // cout << "Include all diff triplets: " << triplets << endl;
        return triplets;
    }
};
