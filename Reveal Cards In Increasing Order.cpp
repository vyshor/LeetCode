class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        sort(deck.begin(), deck.end());
        int i = n-2;
        deque<int> q;
        q.push_back(deck[n-1]);
        while (i >= 0) {
            q.push_front(q.back());
            q.push_front(deck[i]);
            q.pop_back();
            i--;
        }
        vector<int> ans;
        ans.reserve(n);
        for (int& num: q) {
            ans.push_back(num);
        }
        return ans;
    }
};
