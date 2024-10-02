class CustomStack {
public:
    int n;
    vector<int> arr;

    CustomStack(int maxSize) {
        n = maxSize;
    }

    void push(int x) {
        if (arr.size() < n) arr.push_back(x);
    }

    int pop() {
        if (arr.size() > 0) {
            auto val = arr.back();
            arr.pop_back();
            return val;
        }
        return -1;
    }

    void increment(int k, int val) {
        for (int i = 0; i < min(k, (int) arr.size()); i++) {
            arr[i] += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
