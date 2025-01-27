# http://cs101.openjudge.cn/practice/22161/

import heapq
from typing import Dict


class Node:
    def __init__(self, weight, min_char, left=None, right=None):
        self.weight = weight
        self.min_char = min_char
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.weight != other.weight:
            return self.weight < other.weight
        return self.min_char < other.min_char


def construct_huffman_tree(dic):
    heapq.heapify(dic)
    while len(dic) > 1:
        l = heapq.heappop(dic)
        r = heapq.heappop(dic)
        heapq.heappush(
            dic, Node(l.weight + r.weight, min(l.min_char, r.min_char), l, r)
        )
    return dic[0]


def traverse(root: Node, prefix: str, constructed: Dict):
    if not root.left and not root.right:
        constructed[root.min_char] = prefix
        return
    traverse(root.left, prefix + "0", constructed)
    traverse(root.right, prefix + "1", constructed)


def construct_huffman_dic(root):
    dic = dict()
    traverse(root, "", dic)
    return dic


def encode(data: str, dic: Dict):
    result = ""
    for ch in data:
        result += dic[ch]
    return result


def decode(data: str, root: Node):
    pos = 0
    dl = len(data)
    result = ""
    cur = root
    while pos < dl:
        while cur.left and cur.right:
            cur = cur.left if data[pos] == "0" else cur.right
            pos += 1
        result += cur.min_char
        cur = root
    return result


dic_size = int(input())
dic = []
for _ in range(dic_size):
    item = input().split()
    dic.append(Node(int(item[1]), item[0]))

huffman_tree = construct_huffman_tree(dic)
huffman_dic = construct_huffman_dic(huffman_tree)

while True:
    try:
        data = input()
    except:
        break
    if data.isdigit():
        print(decode(data, huffman_tree))
    else:
        print(encode(data, huffman_dic))
