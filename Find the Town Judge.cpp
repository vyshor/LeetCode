class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        set<int> people;
        for (int i = 1; i<=n; i++) {
            people.insert(i);
        }

        unordered_map<int, set<int>> trusted;
        for (auto & kvpair: trust) {
            int person = kvpair.at(0);
            int target = kvpair.at(1);

            if (people.find(person) != people.end()) {
                people.erase(person);
            }

            if (trusted.find(target) == trusted.end()) {
                trusted.insert(make_pair(target, set<int>({person})));
            } else {
                trusted.at(target).insert(person);
            }
        }

        if (people.size() > 1 || people.size() == 0) return -1;

        int judge = *people.begin();
        if (judge == 1 && n == 1) return judge;
        if (trusted.find(judge) != trusted.end() && trusted.at(judge).size() == n-1) return judge;
        return -1;
    }
};
