class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        int n = tokens.size();
        if (n == 0) return 0;
        sort(tokens.begin(), tokens.end());
        int maxx = 0;
        int score = 0;
        int i = 0;
        int j = n-1;
        while (i < n && power >= tokens.at(i) && i <= j) {
            while (i < n && power >= tokens.at(i) && i <= j) {
                power -= tokens.at(i);
                i += 1;
                score += 1;
            }

            maxx = max(maxx, score);
            if (score > 0 && i <= j) {
                power += tokens.at(j);
                j -= 1;
                score -= 1;
            }
        }
        return maxx;
    }
};
