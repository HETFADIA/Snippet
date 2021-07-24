class Trie:
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)
        self.searching_method=[self.dfs,self.dfs_iterative,self.bfs]
    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def __delitem__(self, word):
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_end_"]
    def prefix(self,word,search_index=2):
        """print all the possible words starting with preifx word(parameter of prefix)"""
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return ""
            current_dict = current_dict[letter]
        self.searching_method[search_index](current_dict,word)
    def dfs(self,current_dict,prefix_word):
        """dfs to print words through prefix_word"""
        for j in current_dict:
            if j=='_end_':
                print(prefix_word)
            else:
                self.dfs(current_dict[j],prefix_word+j)
    def dfs_iterative(self,current_dict,prefix_word):
        """dfs to print words through prefix_word"""
        stack=[]
        words_queue = [prefix_word]
        stack.append(current_dict)
        while stack:
            current_dict=stack.pop()
            prefix_word=words_queue.pop()
            for j in current_dict:
                if j=='_end_':
                    print(prefix_word)
                else:
                    stack.append(current_dict[j])
                    words_queue.append(prefix_word+j)


    def bfs(self,current_dict,prefix_word):
        """bfs to print words through prefix_word"""
        q=deque()
        words_queue = deque()
        q.append(current_dict)
        words_queue.append(prefix_word)
        while len(q):
            current_dict=q.popleft()
            prefix_word=words_queue.popleft()
            for j in current_dict:
                if j=='_end_':
                    print(prefix_word)
                else:
                    q.append(current_dict[j])
                    words_queue.append(prefix_word+j)
    def count_prefix(self,word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return 0
            current_dict = current_dict[letter]
        return self.bfs_count(current_dict, word)
    def bfs_count(self,current_dict,prefix_word):
        """bfs to count all words starting through prefix_word"""
        q=deque()
        q.append(current_dict)
        counter=0
        while len(q):
            current_dict=q.popleft()
            for j in current_dict:
                if j=='_end_':
                    counter+=1
                else:
                    q.append(current_dict[j])
        return counter
    def regex_search(self,word):
        """searches if word is present in trie word may contain regex ."""
        current_dict=self.root
        return self.dfs_search(current_dict,word,0)
    def dfs_search(self,current_dict,word,indexa):
        if type(current_dict)==bool:
            return 0
        if indexa==len(word):
            return "_end_" in current_dict
        if word[indexa]=='.':
            for i in current_dict:
                if self.dfs_search(current_dict[i],word,indexa+1):
                    return 1
            return 0
        else:
            if word[indexa] in current_dict:
                return self.dfs_search(current_dict[word[indexa]],word,indexa+1)
    def max_xor(self,a,bits=32):
        current_dict=self.root
        ans=[]
        for indexa in range(bits):
            if a[indexa] == '0':
                current_bit = '1'
            else:
                current_bit = '0'
            if current_bit in current_dict:
                current_dict=current_dict[current_bit]
                ans.append(current_bit)
            else:
                current_dict=current_dict[a[indexa]]
                ans.append(a[indexa])
        return ''.join(ans)
    def bit_binary(self,a):
        return '{:032b}'.format(a)
    def get_max_xor_array(self,arr):
        arrbits = [self.bit_binary(i) for i in arr]
        n = len(arr)
        for i in arrbits:
            self.add(i)
        maxans = 0
        for i in range(n):
            string = self.max_xor(arrbits[i])
            num = int(string, 2)
            maxans = max(maxans, num ^ arr[i])
        return maxans
