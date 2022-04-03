template <typename Node>
class SegmentTree
{
    // vector<int> v = {3, 4, 5};
    // SegmentTree<int> s1(v, 0, func);
    // cout << s1.query(2, 3) << endl;
public:
    Node self_default;
    Node (*func)(Node, Node);
    int self_len;
    int self_size;
    vector<Node> selfdata;
    int bit_lenght(int a)
    {
        int ans = 0;
        while (a)
        {
            ans++;
            a >>= 1;
        }
        return ans;
    }
    SegmentTree(vector<Node> &data, Node _default, Node (*f1)(Node, Node))
    {
        self_default = _default;
        func = f1;
        int self_len = data.size();
        self_size = 1 << bit_lenght(self_len - 1);
        selfdata = vector<Node>(2 * self_size, _default);
        for (int i = self_size; i < self_size + self_len; i++)
        {
            selfdata[i] = data[i - self_size];
        }
        for (int i = self_size - 1; i >= 0; --i)
        {
            selfdata[i] = func(selfdata[2 * i], selfdata[2 * i + 1]);
        }
    }
    void delitem(int idx, int value)
    {
        selfdata[idx] = self_default;
    }
    Node getitem(int idx, int value)
    {
        return selfdata[idx + self_size];
    }
    void setitem(int idx, int value)
    {
        idx += self_size;
        selfdata[idx] = value;
        idx >>= 1;
        while (idx)
        {
            selfdata[idx] = func(selfdata[2 * idx], selfdata[2 * idx + 1]);
            idx >>= 1;
        }
    }
    Node query(int start, int stop)
    {
        // function of [start,stop) just like pyrival
        start += self_size;
        stop += self_size;
        int res_left, res_right;
        res_left = res_right = self_default;
        while (start < stop)
        {
            if (start & 1)
            {
                res_left = func(res_left, selfdata[start]);
                start += 1;
            }
            if (stop & 1)
            {
                stop -= 1;
                res_right = func(selfdata[stop], res_right);
            }
            start >>= 1;
            stop >>= 1;
        }

        return func(res_left, res_right);
    }
    int len()
    {
        return self_len;
    }
    void repr()
    {
        for (int i = 0; i < selfdata.size(); i++)
        {
            cout << selfdata[i] << " ";
        }
        cout << endl;
    }
};
