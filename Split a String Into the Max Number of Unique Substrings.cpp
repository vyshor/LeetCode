class Solution {
public:
    int maxUniqueSplit(string s) {
        int n = s.size(), count = 0, maxx = 0;
        unordered_set<string> seen;
        string word = "";

        function<void(int)> recur;
        recur = [&recur, &n, &seen, &count, &word, &maxx, &s] (int i) {
            if (i == n) {
                if (!seen.contains(word)) {
                    if (count+1 > maxx) maxx = count+1;
                }
                return;
            }

            word.push_back(s[i]);
            recur(i+1);
            word.pop_back();

            if (word.size() > 0 && !seen.contains(word)) {
                auto prev_word = word;
                seen.insert(word);
                count++;
                word = s[i];

                recur(i+1);

                word = prev_word;
                seen.erase(word);
                count--;
            }
        };
        recur(0);
        return maxx;
    }
};
