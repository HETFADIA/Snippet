// https://repl.it/@hetrakeshfadia/UnfoldedFlickeringGlitch#main.cpp
#pragma GCC optimize("O2")
#include <bits/stdc++.h>
using namespace std;
#define het                           \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define lld long long int
#define p(x) cout << x << "\n";
#define endl "\n"
#define all(x) x.begin(), x.end()
#define dll(x) x.begin(), x.end(), greater<lld>()
#define p(x) cout << x << "\n";
#define p2(x, y) cout << x << " " << y << "\n";
#define p3(x, y, z) cout << x << " " << y << " " << z << "\n";
#define p4(x, y, z, a) cout << x << " " << y << " " << z << " " << a << endl;
#define p5(x, y, z, a, b) cout << x << " " << y << " " << z << " " << a << " " << b << endl;
#define ps(x) cout << x << " ";
#define ps2(x, y) cout << x << " " << y << " ";
#define ps3(x, y, z) cout << x << " " << y << " " << z << " ";
#define ps4(x, y, z, a) cout << x << " " << y << " " << z << " " << a << " ";
#define ps5(x, y, z, a, b) cout << x << " " << y << " " << z << " " << a << " " << b << " ";
#define pns(x) cout << x;
#define vect(x, n) vector<lld> x(n, 0);
#define matrix(x, n, m) vector<vector<lld>> x(n, vector<lld>(m, 0));
#define gcd(a, b) __gcd(a, b)
#define lcm(a, b) (a * b) / gcd(a, b)
#define lb lower_bound
#define ub upper_bound
#define pb(x) push_back(x);
#define pf(x) push_front(x);
#define mkp(x, y) make_pair(x, y)
#define f(i,a,b) for(lld i=(a);i<(b);i++)
#define fr(i,a,b) for(lld i=(b);i>a;i--)
#define inf 999999
void print(vector<lld> &v);
lld pow(lld x, lld y);
lld pow(lld x, lld y, lld p);
void swap(lld &x, lld &y);
const lld mod = 1e9 + 7;
lld bintodec(lld n);
string dectobin(lld n);
void addedge(unordered_map<lld, set<lld>> &adj, lld u, lld v);
void dfs(unordered_map<lld, set<lld>> &adj, unordered_map<lld, lld> visited, lld v);
void bfs(unordered_map<lld, set<lld>> &adj, unordered_map<lld, lld> visited, lld v);
struct cmpfunc
{
    bool operator()(const long &a, const long &b) const
    {
        return a > b;
    }
};
void se()
{
}
int main()
{
    het;
    lld t;
    cin >> t;

    while (t--)
    {
        se();
    }
}
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
    // p("");
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
void swap(lld &x, lld &y)
{
    lld temp = x;
    x = y;
    y = temp;
}
