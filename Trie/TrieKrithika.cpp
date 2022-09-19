#include <bits/stdc++.h>
using namespace std;

class Trie {
   public:
    int nc;
    vector<bool> hotnode;
    vector<vector<int>> trie;

    Trie(const int MAXN, const int ALPH) {
        trie.assign(MAXN, vector<int>(ALPH, -1));
        hotnode.assign(MAXN, false);
        nc = 0;
    }

    void insert(const string& s) {
        int cur = 0;
        for (int i = 0; i < s.length(); i++) {
            if (trie[cur][s[i] - 'a'] == -1)
                trie[cur][s[i] - 'a'] = ++nc;
            cur = trie[cur][s[i] - 'a'];
        }
        hotnode[cur] = 1;
    }

    bool search(const string& s) {
        int cur = 0;
        for (int i = 0; i < s.length(); i++) {
            if (trie[cur][s[i] - 'a'] == -1)
                return false;
            cur = trie[cur][s[i] - 'a'];
        }
        return hotnode[cur];
    }
};

const int MAXN = 1e5;
const int ALPH = 26;

int32_t main() {
    Trie trie(MAXN, ALPH);
    return 0;
}
