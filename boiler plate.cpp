#pragma GCC optimize("O2")
#include <bits/stdc++.h>
using namespace std;
using namespace chrono;
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define int long long
#define lld long long
#define p(x) cout << x << endl;
#define p2(x, y) cout << x << " " << y << endl;
#define p3(x, y, z) cout << x << " " << y << " " << z << endl;
#define p4(x, y, z, a) cout << x << " " << y << " " << z << " " << a << endl;
#define p5(x, y, z, a, b) cout << x << " " << y << " " << z << " " << a << " " << b << endl;
#define ps(x) cout << x << " ";
#define ps2(x, y) cout << x << " " << y << " ";
#define ps3(x, y, z) cout << x << " " << y << " " << z << " ";
#define ps4(x, y, z, a) cout << x << " " << y << " " << z << " " << a << " ";
#define ps5(x, y, z, a, b) cout << x << " " << y << " " << z << " " << a << " " << b << " ";
#define pns(x) cout << x;
#define endl "\n"
#define all(x) x.begin(), x.end()
#define dll(x) x.begin(), x.end(), greater<lld>()
#define vect(x, n) vector<lld> x(n, 0);
#define matrix(x, n, m) vector<vector<lld>> x(n, vector<lld>(m, 0));
#define gcd(a, b) __gcd(a, b)
#define lcm(a, b) (a * b) / gcd(a, b)
#define lb lower_bound
#define ub upper_bound
#define pb(x) push_back(x);
#define pf(x) push_front(x);
#define mkp(x, y) make_pair(x, y)
#define f(i, a, b) for (lld i = (a); i < (b); i++)
#define fr(i, a, b) for (lld i = (b); i > a; i--)
#define inf 999999999999999
#define pll pair<lld, lld>
#define ppll pair<pll, lld>
#define ff first
#define ss second
void addedge(unordered_map<lld, set<lld>> &adj, lld u, lld v)
{
    adj[u].insert(v);
    adj[v].insert(u);
}
void dfs(unordered_map<lld, set<lld>> &adj, unordered_map<lld, lld> visited, lld v)
{
    visited[v] = 1;
    p(v);
    for (auto it = adj[v].begin(); it != adj[v].end(); it++)
    {
        if (visited[*it] == 0)
        {
            dfs(adj, visited, *it);
        }
    }
}
void bfs(unordered_map<lld, set<lld>> &adj, unordered_map<lld, lld> visited, lld v)
{
    visited[v] = 1;
    queue<lld> q;
    q.push(v);
    while (q.empty() == 0)
    {
        lld s = q.front();
        // p(s);
        q.pop();

        for (auto it = adj[s].begin(); it != adj[s].end(); it++)
        {
            if (visited[*it] == 0)
            {
                q.push(*it);
                visited[*it] = 1;
            }
        }
    }
}
struct cmpfunc
{
    bool operator()(const long &a, const long &b) const
    {
        return a > b;
    }
};
lld pow(lld x, lld y, lld p)
{
    lld res = 1; // Initialize result

    // Update x if it is more than or
    // equal to p
    x = x % p;

    while (y > 0)
    {
        // If y is odd, multiply x with the result
        if (y & 1)
            res = (res * x) % p;

        // y must be even now
        y = y >> 1; // y = y/2
        x = (x * x) % p;
    }
    return res;
}
lld pow(lld x, lld y)
{
    lld res = 1;
    while (y > 0)
    {
        if (y & 1)
            res = ((res) * (x));
        y = y >> 1;
        x = ((x) * (x));
    }
    return res;
}
lld bintodec(lld n)
{
    lld num = n;
    lld dec_value = 0;

    // Initializing base value to 1, i.e 2^0
    lld base = 1;

    lld temp = num;
    while (temp)
    {
        lld last_digit = temp % 10;
        temp = temp / 10;

        dec_value += last_digit * base;

        base = base * 2;
    }

    return dec_value;
}
string dectobin(lld n)
{

    //finding the binary form of the number and
    //coneverting it to string.
    string s = bitset<64>(n).to_string();

    //Finding the first occurance of "1"
    //to strip off the leading zeroes.
    const auto loc1 = s.find('1');

    if (loc1 != string::npos)
        return s.substr(loc1);

    return "0";
}
void print(vector<lld> &v)
{
    for (lld i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}
void print(vector<string> &v)
{
    for (lld i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}
void print(vector<pll> &v)
{
    for (lld i = 0; i < v.size(); i++)
    {
        cout << v[i].first << " " << v[i].second << " ";
    }
    cout << endl;
}
void prints(vector<int> v)
{
    //prints the vector from 1st index
    for (int i = 1; i != v.size(); i++)
    {
        ps(v[i]);
    }
}
void print(set<pair<int, int>> seta)
{
    //prints the set it is used for debuggging
    set<pair<int, int>>::iterator i;
    for (i = seta.begin(); i != seta.end(); i++)
    {
        ps2(i->first, i->second);
    }
    p("");
}
void print(map<int, int> mapa)
{
    //prints the map it is used for debuggging
    map<int, int>::iterator i;
    for (i = mapa.begin(); i != mapa.end(); i++)
    {
        ps4("{", i->first, i->second, "}");
    }
    p("");
}
void print(set<int> seta)
{
    //prints the set it is used for debuggging
    set<int>::iterator i;
    for (i = seta.begin(); i != seta.end(); i++)
    {
        ps(*i);
    }
    p("");
}
void print(map<pair<int, int>, pair<int, int>> mapa)
{
    //prints the map it is used for debuggging
    map<pair<int, int>, pair<int, int>>::iterator i;
    for (i = mapa.begin(); i != mapa.end(); i++)
    {
        ps4(i->first.first, i->first.second, i->second.first, i->second.second);
    }
}
void print(map<pair<int, int>, int> mapa)
{
    //prints the map it is used for debuggging
    map<pair<int, int>, int>::iterator i;
    for (i = mapa.begin(); i != mapa.end(); i++)
    {
        ps5("{", i->first.first, i->first.second, i->second, "}");
    }
    p("");
}
void print(pair<int, int> tuple)
{
    //prints the tuple it is used for debuggging
    p2(tuple.first, tuple.second);
}
void print(set<lld, greater<lld>> s)
{
    for (auto i = s.begin(); i != s.end(); i++)
    {
        p(*i);
    }
}
int min_index(vector<int> cost)
{
    //returns the index of the min element of cost ie if min(cost)=4 then it returns index(4) in cost vector
    int index = 0;
    int min_cost = 0;
    if (cost.size())
    {
        min_cost = cost[0];
    }
    for (int i = 0; i < cost.size(); i++)
    {
        if (min_cost > cost[i])
        {
            min_cost = cost[i];
            index = i;
        }
    }
    return index;
}
// const lld a3=1000000;
// bool prime[a3 + 1];
// void SieveOfEratosthenes(int n)
// {

//     memset(prime, true, sizeof(prime));

//     for (int p = 2; p * p <= n; p++)
//     {
//         if (prime[p] == true)
//         {

//             for (int i = p * p; i <= n; i += p)
//                 prime[i] = false;
//         }
//     }
// }
void Counter(vector<lld> &v, unordered_map<lld, lld> &um)
{
    for (int i : v)
    {
        um[i] += 1;
    }
}
unordered_map<lld, lld> Counter(vector<lld> &v)
{
    unordered_map<lld, lld> um;
    for (int i : v)
    {
        um[i] += 1;
    }
    return um;
}
unordered_map<char, lld> Counter(string a)
{
    unordered_map<char, lld> um;
    for (char i : a)
    {
        um[i] += 1;
    }
    return um;
}
void get_list(vector<lld> &v)
{
    for (lld i = 0; i < v.size(); i++)
    {
        cin >> v[i];
    }
}
void ignore(lld a)
{
#ifndef ONLINE_JUDGE
    p(a);
#endif
}
void ignore(lld a, lld b)
{
#ifndef ONLINE_JUDGE
    p2(a, b);
#endif
}
void ignore(lld a, lld b, lld c)
{
#ifndef ONLINE_JUDGE
    p3(a, b, c);
#endif
}
void ignore(lld a, lld b, lld c, lld d)
{
#ifndef ONLINE_JUDGE
    p4(a, b, c, d);
#endif
}
void ignore(lld a, lld b, lld c, lld d, lld e)
{
#ifndef ONLINE_JUDGE
    p5(a, b, c, d, e);
#endif
}
lld kth_no_not_divisible_by_n(lld n, lld k)
{
    return k + (k - 1) / (n - 1);
}
lld ceil(lld a, lld n)
{
    if (a % n == 0)
    {
        return a / n;
    }
    return a / n + 1;
}

string nc = "NO";
string ns = "No";
string yc = "YES";
string ys = "Yes";

void fun()
{
}
signed main()
{
    fastio;
    auto start1 = high_resolution_clock::now();

    lld t;
    cin >> t;

    // t = 1;
    while (t--)
    {
        fun();
    }

    auto stop1 = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop1 - start1);
#ifndef ONLINE_JUDGE
    cerr << "Time: " << duration.count() / 1000.0 << endl;
    cout << duration.count() / 1000.0 << endl;
#endif
}
