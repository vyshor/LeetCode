struct Trie {
    int val = -1;
    Trie* child[2];

    Trie() {
        child[0] = nullptr;
        child[1] = nullptr;
    };

    void add(int num, int i) {
        int bit = (num & (1 << i)) >> i;

        if (i == 0) {
            val = num;
            return;
        }

        if (!child[bit]) child[bit] = new Trie();
        child[bit]->add(num, i-1);
    }

    int find(int num, int i) {
        int inverse = ((num & (1 << i)) >> i) ^ 1;

        if (i == 0) {
            return val;
        }

        if (child[inverse]) {
            int valid_num = child[inverse]->find(num, i-1);
            if (valid_num != -1) return valid_num;
        }

        int same_bit = inverse ^ 1;
        if (child[same_bit]) {
            int valid_num = child[same_bit]->find(num, i-1);
            if (valid_num != -1) return valid_num;
        }

        return -1;
    }
};

class Solution {
public:
    Trie root = Trie();

    int max_bit(int i) {
        int count = 0;
        while (i > 0) {
            count++;
            i >>= 1;
        }
        return count;
    };

    int findMaximumXOR(vector<int>& nums) {
        int maxx = *max_element(nums.begin(), nums.end());
        int total_bits = max_bit(maxx);
        for (int num: nums) {
            root.add(num, total_bits);
        }

        maxx = 0;
        for (int num: nums) {
            int other_num = root.find(num, total_bits);
            maxx = max(maxx, num ^ other_num);
        }
        return maxx;
    }
};
