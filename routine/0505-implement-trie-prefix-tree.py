# https://leetcode.cn/problems/implement-trie-prefix-tree/description/


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.end = False
        self.child = dict()


class Trie:

    def __init__(self):
        self.root = Node(None)

    def insert(self, word: str) -> None:
        p = self.root
        for ch in word:
            if ch not in p.child:
                p.child[ch] = Node(ch)
            p = p.child[ch]
        p.end = True

    def search(self, word: str) -> bool:
        p = self.root
        for ch in word:
            if ch not in p.child:
                return False
            p = p.child[ch]
        return p.end

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for ch in prefix:
            if ch not in p.child:
                return False
            p = p.child[ch]
        return True
