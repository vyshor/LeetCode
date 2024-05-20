class StockSpanner {
public:
    int n = 0;
    vector<int> val;
    vector<int> count;

    StockSpanner() {

    }

    int next(int price) {
        int total = 1;
        while (n > 0 && val.back() <= price) {
            total += count.back();
            val.pop_back();
            count.pop_back();
            n--;
        }

        count.push_back(total);
        val.push_back(price);
        n++;
        return total;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */
