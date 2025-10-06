unordered_map<int, int> dp_count = {
    {1, 2},
    {2, 3}
};

class Solution {
public:
    string bstring;
    string pattern;
    int pattern_size = 0;
    int pattern_count = 0;

    int bitcount(long long i) {
        int count = 0;
        while (i > 0) {
            count++;
            i >>= 1;
        }
        return count;
    }

    int recurcount(int total_bits) {
        if (total_bits == 1) return 2;
        if (total_bits == 2) return 3;
        int count = 3;
        for (int i = total_bits; i >= 3; i--) {
            count += (1 << ((i-1) / 2));
        }
        return count;

        // if (dp_count.contains(total_bits)) return dp_count[total_bits];

        // int n = total_bits-2; // first and last bit is always 1
        // int count = (1 << ((n+1) / 2)) + recurcount(total_bits-1);
        // dp_count[total_bits] = count;

        // return count;
    }

    int countBinaryPalindromes(long long n) {
        if (n < 2) return n+1;
        if (n == 2) return 2;

        int total_bits = bitcount(n);
        int count = recurcount(total_bits-1);
        int half_bits = (total_bits+1)/2;
        bitset<64> brep(n);
        string front = brep.to_string().substr(64-total_bits, half_bits);
        string back = brep.to_string().substr(64-half_bits);

        for (int i = 1; i < half_bits; i++) {
            if (front[i] == '1') count += (1 << (half_bits - i - 1));
        }

        reverse(front.begin(), front.end());
        count += front <= back;

        return count;
    }
};
