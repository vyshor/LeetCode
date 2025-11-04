class Solution {
public:
    static constexpr int MAXX = 1e5;

    int minSwap(vector<int>& nums1, vector<int>& nums2) {
        int original = 0, switched = 1;
        int n = nums1.size();
        int prev_min = min(nums1[n-1], nums2[n-1]);
        int prev_num1 = nums1[n-1];
        int prev_num2 = nums2[n-1];

        for (int i = n-2; i>= 0; --i) {
            int num1 = nums1[i];
            int num2 = nums2[i];
            int new_original = MAXX;
            int new_switched = MAXX;

            // cout << "i=" << i << " original=" << original << " switched= " << switched << endl;

            if (max(num1, num2) < prev_min) {
                // Switch or don't switch doesnt matter
                new_original = min(original, switched);
                new_switched = 1+min(original, switched);
            } else {
                // Valid case by not switching
                if (num1 < prev_num1 && num2 < prev_num2) {
                    new_original = min(new_original, original);
                    new_switched = min(new_switched, 1+switched);
                } else {
                    // Must switch
                    new_original = min(new_original, switched);
                    new_switched = min(new_switched, 1+original);
                }
            }

            original = new_original;
            switched = new_switched;
            prev_min = min(num1, num2);
            prev_num1 = num1;
            prev_num2 = num2;
        }
        return min(original, switched);
    }
};
