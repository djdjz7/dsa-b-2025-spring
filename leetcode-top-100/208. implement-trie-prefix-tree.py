# https://leetcode.cn/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-100-liked


class TrieNode:
    def __init__(
        self,
    ):
        self.children = dict()
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        p = self.root
        for ch in word:
            if ch in p.children:
                p = p.children[ch]
            else:
                p.children[ch] = TrieNode()
                p = p.children[ch]
        p.is_end = True

    def search(self, word: str) -> bool:
        p = self.root
        for ch in word:
            if ch not in p.children:
                return False
            p = p.children[ch]
        return p.is_end

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for ch in prefix:
            if ch not in p.children:
                return False
            p = p.children[ch]
        return True
