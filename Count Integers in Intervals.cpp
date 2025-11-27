struct Node {
    int minn;
    int maxx;
    int mid;

    int maxx_count;
    int count = 0;

    Node* left = nullptr;
    Node* right = nullptr;

    Node(int left_val=1, int right_val=1e9) : minn{left_val}, maxx{right_val}, mid{(left_val+right_val)/2}, maxx_count{right_val-left_val+1} {
        // if (maxx_count > 1) {
        //     if (left_val < mid) left = new Node(left_val, mid-1);
        //     if (right_val > mid) right = new Node(mid+1, right_val);
        // }
    }

    int add(int left_val, int right_val) {
        // cout << left_val << "," << right_val << endl;

        if (maxx_count == count) return maxx_count;
        if (left_val == right_val && maxx_count == 1) {
            count = 1;
            return count;
        }

        if (right_val-left_val+1 == maxx_count) {
            count = maxx_count;
            return count;
        }

        int new_count = 0;
        if (right_val <= mid) {
            if (!left) left = new Node(minn, mid);
            new_count += left->add(left_val, right_val);
            new_count += right ? right->get_count() : 0;
        } else if (left_val >= mid+1) {
            if (!right) right = new Node(mid+1, maxx);
            new_count += right->add(left_val, right_val);
            new_count += left ? left->get_count() : 0;
        } else {
            if (!left) left = new Node(minn, mid);
            if (!right) right = new Node(mid+1, maxx);
            new_count += left->add(left_val, mid);
            new_count += right->add(mid+1, right_val);
        }

        count = new_count;
        return new_count;
    }

    int get_count() {return count;}

    ~Node(){
        delete left;
        delete right;
    }
};


class CountIntervals {
public:
    Node root;

    CountIntervals() {

    }

    void add(int left, int right) {
        root.add(left, right);
    }

    int count() {
        return root.get_count();
    }
};

/**
 * Your CountIntervals object will be instantiated and called as such:
 * CountIntervals* obj = new CountIntervals();
 * obj->add(left,right);
 * int param_2 = obj->count();
 */
