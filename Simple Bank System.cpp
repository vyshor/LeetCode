class Bank {
public:
    vector<long long> balances;
    int n;

    Bank(vector<long long>& balance) {
        balances = std::move(balance);
        n = balances.size();
    }

    bool transfer(int account1, int account2, long long money) {
        account1--;
        account2--;
        if (account1 < 0 || account1 >= n) return false;
        if (account2 < 0 || account2 >= n) return false;

        if (balances[account1] >= money) {
            balances[account1] -= money;
            balances[account2] += money;
        } else {
            return false;
        }
        return true;
    }

    bool deposit(int account, long long money) {
        account--;
        if (account < 0 || account >= n) return false;
        balances[account] += money;
        return true;
    }

    bool withdraw(int account, long long money) {
        account--;
        if (account < 0 || account >= n) return false;
        if (balances[account] >= money) {
            balances[account] -= money;
        } else {
            return false;
        }
        return true;
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
