class Solution {
public:
    string hash(vector<string> v) {
        stringstream ss;
        for (string& s: v) {
            ss << s << "-";
        }
        return ss.str();
    }
    vector<vector<string>> partition(string s) {
        int j = 0;
        vector<string> substring;
        for (char& c: s) {
            string new_s(1, c);
            substring.push_back(new_s);
        }

        vector<vector<string>> arr{
            substring,
        };

        unordered_set<string> seen;
        function<void(vector<string>)> explore;
        explore = [&arr, &seen, this] (vector<string> arr2) -> void {
            int n = arr2.size();
            for (int i = 0; i < n-1; i++) {
                if (arr2[i] == arr2[i+1]) {
                    vector<string> arr3(arr2.begin(), arr2.begin()+i);
                    arr3.push_back(arr2[i] + arr2[i+1]);
                    arr3.insert(arr3.end(), arr2.begin()+i+2, arr2.end());
                    string key = hash(arr3);
                    if (!seen.contains(key)) {
                        seen.insert(key);
                        arr.push_back(move(arr3));
                    }
                }
            }

            for (int i = 0; i < n-2; i++) {
                if (arr2[i] == arr2[i+2]) {
                    vector<string> arr3(arr2.begin(), arr2.begin()+i);
                    arr3.push_back(arr2[i] + arr2[i+1] + arr2[i+2]);
                    arr3.insert(arr3.end(), arr2.begin()+i+3, arr2.end());
                    string key = hash(arr3);
                    if (!seen.contains(key)) {
                        seen.insert(key);
                        arr.push_back(move(arr3));
                    }
                }
            }
        };

        while (j < arr.size()) {
            explore(arr[j++]);
        }
        return arr;
    }
};
