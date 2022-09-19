
class Trie {
public:
    /** Initialize your data structure here. */
    vector<vector<int>> t;
    int N;
    Trie() {
        t = vector<vector<int>> (1, vector<int> (27));
        N = 0;
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        int node = 0;
        word.push_back('{');
        for(auto ch: word){
            if(!t[node][ch - 'a']){
                t[node][ch - 'a'] = ++N;
                t.push_back(vector<int>(27));
            }
            node = t[node][ch - 'a'];
        }
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        int node = 0;
        int i = 0;
        while(i < word.size() && t[node][word[i]-'a']){
            node = t[node][word[i] - 'a'];
            i += 1;
        }
        return i == word.size() && t[node][26] != 0;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string word) {
        int node = 0;
        int i = 0;
        while(i < word.size() && t[node][word[i]-'a']){
            node = t[node][word[i] - 'a'];
            i += 1;
        }
        return i == word.size();
    }
};
