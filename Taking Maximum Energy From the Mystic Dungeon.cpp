class Solution {
public:
    int maximumEnergy(vector<int>& energy, int k) {
        int n = energy.size();
        int maxx = energy[n-1];
        for (int i = n-1; i >=0 ; i--) {
            maxx = max(maxx, energy[i]);
            if (i - k >= 0) {
                energy[i-k] = energy[i-k] + energy[i];
            }
            // cout << "i=" << i << " " << energy[i] << endl;
        }
        return maxx;
    }
};
