class Solution {
public:
    int key(int book, int j) {
        return j << 10 | book;
    }

    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        int n = books.size();
        map<int, int> dp;
        function<int(int, int, int)> place;
        place = [&place, &n, &dp, &shelfWidth, &books, this] (int book, int j, int h) {
            int k = key(book, j);
            if (dp.count(k)) return dp[k];

            if (book == n) return h;

            int thic = books[book][0], height = books[book][1];
            int cost = INT_MAX;
            if (j + thic <= shelfWidth) cost = place(book+1, j+thic, max(height, h));

            if (j != 0) cost = min(cost, h + place(book, 0, 0));

            dp[k] = cost;
            return cost;
        };

        return place(0, 0, 0);
    }
};
