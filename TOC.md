## cs201数算（计算机基础2）2025pre每日选做
<mark>https://github.com/GMyhf/2025spring-cs201/blob/main/pre_problem_list_2025spring.md</mark>

Updated 0002 GMT+8 Feb 5 2025.
2025 winter, Complied by Hongfei Yan

题解在：
[2024fall_LeetCode_problems.md](https://github.com/GMyhf/2024fall-cs101/blob/main/2024fall_LeetCode_problems.md),
[2024spring_dsa_problems.md](https://github.com/GMyhf/2024spring-cs201/blob/main/2024spring_dsa_problems.md),
[sunnywhy_problems.md](https://github.com/GMyhf/2024spring-cs201/blob/main/sunnywhy_problems.md)
<!--
|  |  | -  | - |    |
!-->

| 日期 | 问题编号与名称  | 标签          | 难度 | 链接                                                 |
| ---- | --------------- | ------------- | ---- | ---------------------------------------------------- |
| 0206 | 04123: 马走日 | -  | - | http://cs101.openjudge.cn/practice/04123   |
| 0206 | sy379: 有向图的邻接表 | -  | - | https://sunnywhy.com/sfbj/10/2/379    |
| 0206 | sy378: 无向图的邻接表 | -  | - | https://sunnywhy.com/sfbj/10/2/378   |
| 0205 | 19943: 图的拉普拉斯矩阵 | OOP  | - | http://cs101.openjudge.cn/25dsapre/19943/    |
| 0205 | sy377: 有向图的邻接矩阵 | -  | Easy | https://sunnywhy.com/sfbj/10/2/377    |
| 0205 | sy376: 无向图的邻接矩阵 | -  | Easy | https://sunnywhy.com/sfbj/10/2/376    |
|  |  | -  | - | graph begin   |
| 0204 | 01760: Disk Tree | Trie  | - | http://cs101.openjudge.cn/25dsapre/01760/    |
| 0204 | 124.二叉树中的最大路径和 | dfs  | Tough | https://leetcode.cn/problems/binary-tree-maximum-path-sum/    |
| 0204 | 199.二叉树的右视图 | bfs  | Medium | https://leetcode.cn/problems/binary-tree-right-side-view/    |
| 0203 | 01703: 发现它，抓住它 | disjoint set  | - | http://cs101.openjudge.cn/25dsapre/01703/    |
| 0203 | 01611: The Suspects | disjoint set  | - | http://cs101.openjudge.cn/practice/01611/    |
| 0203 | 01182: 食物链  | disjoint set  | Tough | http://cs101.openjudge.cn/practice/01182    |
| 0202 | 01145: Tree Summing | -  | - | http://cs101.openjudge.cn/25dsapre/01145/    |
| 0202 | 02788: 二叉树（2） | -  | - | http://cs101.openjudge.cn/practice/02788/    |
| 0202 | 02756: 二叉树（1） | -  | - | http://cs101.openjudge.cn/practice/02756/    |
| 0201 | 02524: 宗教信仰 | disjoint set  | - | http://cs101.openjudge.cn/dsapre/02524/   |
| 0201 | 02499: Binary Tree | -  | - | http://cs101.openjudge.cn/25dsapre/02499/    |
| 0201 | 02255: 重建二叉树 | -  | - | http://cs101.openjudge.cn/practice/02255/     |
| 0131 | 27625: AVL树至少有几个结点 | -  | - | http://cs101.openjudge.cn/25dsapre/27625/   |
| 0131 | 05455: 二叉搜索树的层次遍历 | -  | - | http://cs101.openjudge.cn/practice/05455/      |
| 0131 | 22275: 二叉搜索树的遍历 | -  | - | http://cs101.openjudge.cn/practice/22275/      |
| 0130 | 18164: 剪绳子 | -  | - | http://cs101.openjudge.cn/25dsapre/18164/     |
| 0130 | 22161: 哈夫曼编码树 | -  | Tough | http://cs101.openjudge.cn/practice/22161/      |
| 0130 | 晴问9.7: 向下调整构建大顶堆 | -  | - | https://sunnywhy.com/sfbj/9/7      |
| 0129 | 04078: 实现堆结构 | -  | - | http://cs101.openjudge.cn/25dsapre/04078/      |
| 0129 | 25145: 猜二叉树（按层次遍历） | -  | - | http://cs101.openjudge.cn/practice/25145/      |
| 0129 | 24729: 括号嵌套树   | -  | - | http://cs101.openjudge.cn/practice/24729/       |
| 0128 | 01577: Falling Leaves   | -  | - | http://cs101.openjudge.cn/25dsapre/01577/     |
| 0128 | 22158: 根据二叉树前中序序列建树  | - | - | http://cs101.openjudge.cn/practice/22158/   |
| 0128 | 24750: 根据二叉树中后序序列建树  | - | - | http://cs101.openjudge.cn/practice/24750/   |
| 0127 | 02775: 文件结构“图”  | -  | Tough | http://cs101.openjudge.cn/25dsapre/02775/      |
| 0127 | 25140: 根据后序表达式建立队列表达式  | - |  | http://cs101.openjudge.cn/practice/25140/   |
| 0127 | 102.二叉树的层序遍历  | - | Easy | https://leetcode.cn/problems/binary-tree-level-order-traversal/   |
| 0126 | 06646:二叉树的深度   | -  | - | http://cs101.openjudge.cn/25dsapre/06646/     |
| 0126 | 108.将有序数组转换为二叉搜索树  | - | Easy | https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/   |
| 0126 | 100.相同的树  | - | Easy | https://leetcode.cn/problems/same-tree/  |
| 0125 | 08581: 扩展二叉树   | -  | - | http://cs101.openjudge.cn/25dsapre/08581/       |
| 0125 | 543.二叉树的直径  | - | Easy | https://leetcode.cn/problems/diameter-of-binary-tree/    |
| 0125 | 101.对称二叉树  | - | Easy | https://leetcode.cn/problems/symmetric-tree/    |
| 0124 | 27637: 括号嵌套二叉树 | -  | - | http://cs101.openjudge.cn/25dsapre/27637/      |
| 0124 | 226.翻转二叉树  | - | Easy | https://leetcode.cn/problems/invert-binary-tree/    |
| 0124 | 104.二叉树的最大深度  | - | Easy | https://leetcode.cn/problems/maximum-depth-of-binary-tree/    |
| 0123 | 27638: 求二叉树的高度和叶子数目   | - | - | http://cs101.openjudge.cn/25dsapre/27638/       |
| 0123 | 94.二叉树的中序遍历   | - | Easy | https://leetcode.cn/problems/binary-tree-inorder-traversal/       |
|      |                 | -             | - | tree begin       |
| 0123 | 3095.或值至少K的最短子数组I   | 滑动窗口 | - | https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-i/       |
| 0122 | 04137: 最小新整数   | monotonous-stack  | - | http://cs101.openjudge.cn/25dsapre/04137/       |
| 0122 | 27925: 小组队列   | queue  | - | http://cs101.openjudge.cn/practice/27925/       |
| 0122 | 155.最小栈   | 辅助栈 | Medium | https://leetcode.cn/problems/min-stack/       |
| 0121 | 02299: Ultra-QuickSort   | merge sort  | Tough | http://cs101.openjudge.cn/25dsapre/02299/       |
| 0121 | sy322: 跨步迷宫 | bfs    | Medium | https://sunnywhy.com/sfbj/8/2/322    |
| 0121 | sy323: 字符迷宫 | bfs    | Medium | https://sunnywhy.com/sfbj/8/2/323    |
| 0120 | 03151: Pots   | bfs  | - | http://cs101.openjudge.cn/25dsapre/03151/       |
| 0120 | sy320: 迷宫问题 | bfs    | Medium | https://sunnywhy.com/sfbj/8/2/320    |
| 0120 | 05902: 双端队列   | queue  | - | http://cs101.openjudge.cn/practice/05902/       |
| 0119 | 04067: 回文数字   | queue  | - | http://cs101.openjudge.cn/25dsapre/04067/       |
| 0119 | 19.删除链表的倒数第N个结点   | 快慢指针 | Medium | https://leetcode.cn/problems/remove-nth-node-from-end-of-list/       |
| 0119 | 24591:中序表达式转后序表达式   | stack  | 必须会 | http://cs101.openjudge.cn/practice/24591/       |
| 0118 | 02746: 约瑟夫问题   | queue  | - | http://cs101.openjudge.cn/25dsapre/02746/       |
| 0118 | 24588: 后序表达式求值   | stack  | - | http://cs101.openjudge.cn/practice/24588/       |
| 0118 | 20.删除链表元素   | linked-list  | - | http://dsbpython.openjudge.cn/dspythonbook/P0020/       |
| 0117 | 02734: 十进制到八进制   | stack  | - | http://cs101.openjudge.cn/25dsapre/02734/       |
| 0117 | 4.插入链表元素   | linked-list  | - | http://dsbpython.openjudge.cn/2024allhw/004/       |
| 0117 | sy296: 后缀表达式 | stack    | Easy | https://sunnywhy.com/sfbj/7/1/296       |
| 0116 | 03704: 括号匹配问题   | stack  | - | http://cs101.openjudge.cn/25dsapre/03704       |
| 0116 | sy295: 可能的出栈序列 | stack    | Medium | https://sunnywhy.com/sfbj/7/1/295       |
| 0116 | sy294: 合法的出栈序列 | stack    | Easy | https://sunnywhy.com/sfbj/7/1/294       |
| 0115 | 27653:Fraction类  | OOP        | - | http://cs101.openjudge.cn/25dsapre/27653       |
| 0115 | sy293: 栈的操作序列 | stack    | Easy | https://sunnywhy.com/sfbj/7/1/293       |
| 0115 | 118.杨辉三角    | dp            | Easy | https://leetcode.cn/problems/pascals-triangle/       |
| 0114 | 01321: 棋盘问题 | backtracking  | - | http://cs101.openjudge.cn/25dsapre/01321/       |
| 0114 | 234.回文链表   | 快慢指针 | Easy | https://leetcode.cn/problems/palindrome-linked-list/       |
| 0114 | 206.反转链表   | linked-list            | Easy | https://leetcode.cn/problems/reverse-linked-list/       |
| 0113 | 05345: 位查询 | implementation | - | http://cs101.openjudge.cn/25dsapre/05345/ |
| 0113 | 35.搜索插入位置 | binary search | Easy | https://leetcode.cn/problems/search-insert-position/ |
| 0113 | 20.有效的括号   | stack         | Easy | https://leetcode.cn/problems/valid-parentheses/      |
