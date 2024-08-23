class Solution {
public:
    string fractionAddition(string expression) {
        int n = expression.size(), i = 0;
        stringstream numerator, denominator;
        vector<int> num, den;
        int look_num = 1, pos = 1;
        while (i < n) {
            char c = expression[i];
            if (c == '+' || c == '-') {
                if (!numerator.str().empty()) {
                    num.push_back(stoi(numerator.str()) * pos);
                    stringstream().swap(numerator);
                } else {
                    num.push_back(0);
                }

                if (!denominator.str().empty()) {
                    den.push_back(stoi(denominator.str()));
                    stringstream().swap(denominator);
                } else {
                    den.push_back(1);
                }

                if (c == '-') pos = -1;
                else pos = 1;
                look_num = 1;

            } else if (c == '/') {
                look_num = 0;
            } else if (look_num) {
                numerator << c;
            } else {
                denominator << c;
            }
            i++;
        }

        num.push_back(stoi(numerator.str()) * pos);
        den.push_back(stoi(denominator.str()));
        n = num.size();
        int product = 1;
        for (int d: den) {
            if (product % d == 0) continue;
            product *= d;
        }

        int summ = 0;
        for (int j = 0; j < n; j++) {
            summ += num[j] * (product / den[j]);
        }

        int sign = 1;
        if (summ < 0) {
            sign = -1;
            summ *= -1;
        }

        // cout << summ << '\n';
        // cout << product << '\n';

        while (summ % 2 == 0 && product % 2 == 0) {
            summ /= 2;
            product /= 2;
        }

        int j = 3;
        while (j <= summ && j <= product && summ > 1 && product > 1) {
            if (summ % j == 0 && product % j == 0) {
                summ /= j;
                product /= j;
            } else {
                j += 2;
            }
        }
        return to_string(summ * sign) + "/" + to_string(product);
    }
};
