# Assignment #6: 回溯、树、双向链表和哈希表


## 1. 题目

### [LC46: 全排列](https://leetcode.cn/problems/permutations/)

#### 代码

```python
from typing import List

class Solution:
    def helper(self, nums: List[int], used: List[bool], counter, length, now: List[int]) -> List[List[int]]:
        if counter == length: return [now.copy()]
        result = []
        now.append(0)
        for i in range(length):
            if not used[i]:
                used[i] = True
                now[-1] = nums[i]
                result.extend(self.helper(nums, used, counter + 1, length, now))
                used[i] = False
        now.pop()
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        return self.helper(nums, [False] * l, 0, l, [])
```

#### 代码运行截图

![permutations](./permutations.png)

### [LC79: 单词搜索](https://leetcode.cn/problems/word-search/)

#### 代码

```python
from typing import List, Set


class Solution:
    def do_search(
        self,
        board: List[List[str]],
        row,
        col,
        word: str,
        word_len: int,
        pos: int,
        visited: Set,
        i: int,
        j: int,
    ) -> bool:
        if pos == word_len:
            return True
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        for n in range(4):
            x = i + dx[n]
            y = j + dy[n]
            if (
                0 <= x < row
                and 0 <= y < col
                and board[x][y] == word[pos]
                and (x, y) not in visited
            ):
                visited.add((x, y))
                if self.do_search(
                    board, row, col, word, word_len, pos + 1, visited, x, y
                ):
                    return True
                visited.remove((x, y))
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        wl = len(word)
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and self.do_search(
                    board, row, col, word, wl, 1, set([(i, j)]), i, j
                ):
                    return True
        return False
```

#### 代码运行截图

![word search](./word-search.png)

### [LC94: 二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

#### 代码

```python
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        result = []
        while stack:
            top = stack.pop()
            if top == None:
                continue
            if isinstance(top, TreeNode):
                stack.append(top.right)
                stack.append(top.val)
                stack.append(top.left)
            else:
                result.append(top)
        return result
```

#### 代码运行截图

![inorder traversal](./inorder-traversal.png)

### [LC102: 二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

#### 思路

比起用队列实现，我可能更喜欢一层一层用 array。

#### 代码

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        result = []
        this_level = [root]
        while this_level:
            result.append([])
            new_level = []
            for node in this_level:
                result[-1].append(node.val)
                if node.left: new_level.append(node.left)
                if node.right: new_level.append(node.right)
            this_level = new_level
        return result
```

#### 代码运行截图

![level order traversal](./level-order-traversal.png)

### [LC131: 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/)

#### 思路

这题目数据量并不大，不用 dp 也能解决。

#### 代码

```python
from typing import List
from functools import cache

class Solution:
    @cache
    def is_palindrome(self, s: str) -> bool:
        ls = len(s)
        for i in range(ls // 2):
            if s[i] != s[ls - i - 1]: return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        ls = len(s)
        if ls == 0:
            return [[]]
        result = []
        for i in range(ls):
            if self.is_palindrome(s[i:]):
                x = self.partition(s[:i])
                for sig in x:
                    sig.append(s[i:])
                result.extend(x)
        return result
```

#### 代码运行截图

### [LC146: LRU缓存](https://leetcode.cn/problems/lru-cache/)

#### 代码

```python
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
```

#### 代码运行截图

![lru cache](./lru-cache.png)

## 2. 学习总结和收获

这次力扣周赛比较简单，能 AC 三道。第四题的话看上去和煎鸡排比较类似，可惜这种题目一直不是很会，就感觉给出的公式是很自然的，但是没法证明。
