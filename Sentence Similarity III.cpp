class Solution {
public:
    vector<string> split(string& s) {
        stringstream ss(s);
        vector<string> v;
        while (getline(ss, s, ' ')) {
            v.push_back(s);
        }
        return v;
    }

    bool areSentencesSimilar(string sentence1, string sentence2) {
        auto splits1 = split(sentence1), splits2 = split(sentence2);
        if (splits1.size() > splits2.size()) swap(splits1, splits2);
        int n1 = splits1.size(), n2 = splits2.size();
        if (n1 == 1) return (splits2[0] == splits1[0] || splits2[n2-1] == splits1[0]);

        int l1 = 0, r1 = n1 - 1, r2 = n2 - 1;
        while (l1 < n1 && splits1[l1] == splits2[l1]) l1++;
        while (r1 >= l1 && splits1[r1] == splits2[r2]) {
            r1--;
            r2--;
        }
        return r1 <l1;
    }
};
