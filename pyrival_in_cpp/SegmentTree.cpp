template <typename Node>
class SegmentTree
{
    public:
    Node self_default;
    Node (*func)(Node, Node);
    int self_len;
    int self_size;
    vector<int> selfdata;
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
        for (int i = self_size - 1; i >= 0; --i)
        {
            selfdata[i] = func(selfdata[i + 1], selfdata[2 * i + 1]);
        }
    }
};
int func(int a, int b)
{
    return max(a, b);
}
