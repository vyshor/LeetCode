class KthLargest {
private:
    vector<int> q_;
    int k_;
public:
    KthLargest(int k, vector<int>& nums) {
        k_ = k;
        q_ = nums;
        for (int i = 0; i < nums.size(); i++) {
            q_[i] *= -1;
        }

        make_heap(q_.begin(), q_.end());

        while (q_.size() > k_) {
            pop_heap(q_.begin(), q_.end());
            q_.pop_back();
        }
    }

    int add(int val) {
        q_.push_back(-val);
        push_heap(q_.begin(), q_.end());
        if (q_.size() > k_) {
            pop_heap(q_.begin(), q_.end());
            q_.pop_back();
        }
        return -q_.front();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
