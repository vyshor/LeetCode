class Solution {
public:
    int compareVersion(string version1, string version2) {
        int v1 = 0, v2 = 0;
        int i1 = 0, i2 = 0;
        stringstream ss1, ss2;
        while (i1 < version1.size() || i2 < version2.size()) {
            while (i1 < version1.size() && version1[i1] != '.') {
                ss1 << version1[i1++];
            }

            while (i2 < version2.size() && version2[i2] != '.') {
                ss2 << version2[i2++];
            }

            if (ss1.str().size() > 0) v1 = stoi(ss1.str());
            if (ss2.str().size() > 0) v2 = stoi(ss2.str());

            if (v1 < v2) return -1;
            if (v2 < v1) return 1;
            i1++;
            i2++;
            v1 = 0;
            v2 = 0;
            ss1.str("");
            ss2.str("");
        }

        return 0;
    }
};
