class Solution {
public:
    int findIntegers(int n) {
        int count = 0;
        int n2 = n;
        while (n2 != 0) {
            n2 >>= 1;
            count++;
        }

        int i=1, j=0, k=0, m=0;
        for (int n2 = count; n2 >= 0; n2--) {
            int bit = (n >> n2) & 1;
            int i2=(i+j)*(bit==0), j2=i*bit, k2=k+m+bit*(i+j), m2=k;
            i = i2;
            j = j2;
            k = k2;
            m = m2;
        }
        return i+j+k+m;
    }
};
