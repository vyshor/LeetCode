class Solution {
public:
    vector<int64_t> diff;
    int N;
    int R;

    int checkValidPower(int64_t power, int excess) {
        int m = 2*R+2;
        vector<int64_t> q(m, 0);

        int64_t carry = 0;
        for (int i = 0; i < N; i++) {
            carry += q[i % m] + diff[i];
            q[i % m] = 0;
            if (carry < power) {
                // cout << "i=" << i << " carry=" << carry << " Power=" << power << " excess=" << excess << endl;
                int64_t used = power - carry;
                excess -= used;
                if (excess < 0) return 0;
                q[(i+m-1) % m] -= used;
                carry += used;
            }
        }
        return excess >= 0;
    }

    long long maxPower(vector<int>& stations, int r, int k) {
        N = stations.size();
        R = r;

        // Construct diff array
        diff = vector<int64_t> (N+1, 0);
        int minn_pow = stations[0];
        int64_t summ = 0;
        for (int i = 0; i < N; i++) {
            int pow = stations[i];
            diff[max(i-r, 0)] += pow;
            diff[min(i+r+1, N)] -= pow;
            minn_pow = min(minn_pow, pow);
            summ += pow;
        }

        // cout << "Diff:";
        // for (int i = 0; i < N; i++) {
        //     cout << diff[i] << " ";
        // }
        // cout << endl;

        int64_t maxx = summ+k+1, minn = minn_pow;
        // Binary search
        int64_t maxx_valid = minn;
        while (minn <= maxx) {
            // cout << "Minn=" << minn << " Maxx=" << maxx << endl;
            int64_t mid = (minn+maxx)/2;
            if (checkValidPower(mid, k)) {
                maxx_valid = max(maxx_valid, mid);
                minn = mid+1;
            } else {
                if (minn == maxx) break;
                maxx = mid;
            }
        }
        return maxx_valid;
    }
};
