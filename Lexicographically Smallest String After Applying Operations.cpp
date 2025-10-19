class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        int n = s.size();
        vector<string> q;
        unordered_set<string> seen;
        string minn(n, '9');
        q.push_back(std::move(s));

        while (q.size() > 0) {
            string s2 = std::move(q.back());
            q.pop_back();
            if (seen.contains(s2)) continue;

            seen.insert(s2);
            minn = min(minn, s2);

            string s3 = s2.substr(b) + s2.substr(0, b);
            if (!seen.contains(s3)) q.push_back(std::move(s3));

            for (int i = 1; i < n; i += 2) {
                s2[i] = ((s2[i]-48+a) % 10) + 48;
            }
            if (!seen.contains(s2)) q.push_back(std::move(s2));
        }
        return minn;
    }
};
