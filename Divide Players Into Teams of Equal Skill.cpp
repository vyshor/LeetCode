class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        int n = skill.size();
        if (n % 2) return -1;

        sort(skill.begin(), skill.end());
        int avg = skill[0] + skill.back();
        int i = 0, j = n-1;
        long long chemistry = 0;
        while (i < j) {
            if (skill[i] + skill[j] != avg) return -1;
            chemistry += skill[i++] * skill[j--];
        }
        return chemistry;
    }
};
