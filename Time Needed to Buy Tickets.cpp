class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int total = 0;
        bool pass_k = false;

        for (int i = 0;i < tickets.size(); i++) {
            if (pass_k) total += min(tickets[i], tickets[k]-1);
            else total += min(tickets[i], tickets[k]);

            if (i == k) pass_k = true;
        }
        return total;
    }
};
