class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> counter;
        for (char& c: s) {
            if (!counter.contains(c)) counter.insert(make_pair(c, 1));
            else counter.at(c)++;
        }

        std::stringstream ans;
        for (char& c: order) {
            if (counter.contains(c))  {
                string n(counter.at(c), c);
                ans << n;
            }
            counter.erase(c);
        }

        for (auto& p: counter) {
            string n(p.second, p.first);
            ans << n;
        }

        return ans.str();
    }
};
