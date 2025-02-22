class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next


class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def insertCat(self):
        slow, fast = self.head, self.head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        cat = Node(6)
        cat.next = slow.next
        slow.next = cat

    def printLk(self):
        p = self.head
        while p:
            print(p.data, end=" ")
            p = p.next
        print()


lst = list(map(int, input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()
