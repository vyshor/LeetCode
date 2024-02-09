class Solution {
public:
    string frequencySort(string s) {
        unordered_map<int, uint16_t> umap;
        for (char & c: s) {
            if (umap.find(c) == umap.end()) {
                umap.insert(make_pair(c, 1));
            } else {
                umap.at(c)++;
            }
        }

        vector<pair<uint16_t, int>> arr;
        arr.reserve(umap.size());
        for (auto & it: umap) {
            arr.push_back(it);
        }

        sort( arr.begin(), arr.end(), []( const auto& lhs, const auto& rhs )
        {
            return lhs.second > rhs.second;
        });

        stringstream ss;
        for (auto & kvpair: arr) {
            ss << string(kvpair.second, kvpair.first);
        }

        return ss.str();
    }
};
