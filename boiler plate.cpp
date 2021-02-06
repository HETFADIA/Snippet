#pragma GCC optimize("O2")
#include <bits/stdc++.h>
using namespace std;
#define fastio                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define lld long long
#define lld long long
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
#define inf 999999
#define pll pair<lld, lld>
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
void print(vector<lld> &v)
{
    for (lld i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
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
string nc = "NO";
string ns = "No";
string yc = "YES";
string ys = "Yes";
void fun()
{
    lld n;
    cin >> n;
    string a;
    string b;
    cin >> a;
    cin >> b;
    unordered_map<char, lld> um = Counter(a + b);
    for (auto i : um)
    {
        if (i.second % 2 != 0)
        {
            p(-1);
            return;
        }
    }
    vector<lld> ab;
    vector<lld> ba;
    for (lld i = 0; i < n; i++)
    {
        if (a[i] == b[i])
        {
            continue;
        }
        else if (a[i] == 'a' && b[i] == 'b')
        {
            ab.pb(i);
        }
        else
        {
            ba.pb(i);
        }
    }
    lld count = 0;
    vector<pll> answer;
    while (ab.size() > 1)
    {
        lld siza = ab.size();
        pll tuple = {ab[siza - 1], ab[siza - 2]};
        answer.pb(tuple);
        ab.pop_back();
        ab.pop_back();
    }
    while (ba.size() > 1)
    {
        lld siza = ba.size();
        pll tuple = {ba[siza - 1], ba[siza - 2]};
        answer.pb(tuple);
        ba.pop_back();
        ba.pop_back();
    }
    if (ab.size() == 0 && ba.size() == 0)
    {
        p(answer.size());
        for (lld i = 0; i < answer.size(); i++)
        {
            p2(answer[i].first + 1, 1 + answer[i].second);
        }
    }
    else
    {
        pll tuple = {ab[0], ab[0]};
        answer.pb(tuple);
        tuple = {ab[0], ba[0]};
        answer.pb(tuple);
        p(answer.size());
        for (lld i = 0; i < answer.size(); i++)
        {
            p2(answer[i].first + 1, 1 + answer[i].second);
        }
    }
}
int main()
{
    fastio;
    lld t;
    cin >> t;
    // t=1;
    while (t--)
    {
        fun();
    }
}
