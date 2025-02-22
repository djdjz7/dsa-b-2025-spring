# https://leetcode.cn/problems/lru-cache/description/


class CacheNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.pointers = dict()
        self.head = CacheNode()
        p1 = self.head
        for _ in range(capacity - 1):
            p1.next = CacheNode()
            p1.next.prev = p1
            p1 = p1.next
        self.tail = p1

    def _make_most_recent(self, node: CacheNode):
        if node == self.tail:
            return
        if node == self.head:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.head = node.next
            self.head.prev = None
            self.tail.next = None
            return
        self.tail.next = node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = self.tail
        node.next = None
        self.tail = node

    def get(self, key: int) -> int:
        if key in self.pointers:
            self._make_most_recent(self.pointers[key])
            return self.pointers[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pointers:
            self._make_most_recent(self.pointers[key])
            self.pointers[key].val = value
        else:
            node = CacheNode(key, value)
            head_cache = self.head
            if head_cache.key != None:
                del self.pointers[head_cache.key]
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.head = self.head.next
            self.head.prev = None
            self.tail.next = None
            self.pointers[key] = node


lc = LRUCache(3)
lc.put(1, 1)
lc.get(1)
lc.put(2, 2)
lc.put(1, 2)
