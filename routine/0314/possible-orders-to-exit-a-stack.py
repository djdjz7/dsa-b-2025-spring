# https://sunnywhy.com/sfbj/7/1/295

n = int(input())

def enum(pending, stack, ans_seg):
    if pending > n and not stack:
        print(*ans_seg)
        return
    if pending > n:
        ans_seg.append(stack.pop())
        enum(pending, stack, ans_seg)
        return
    if stack:
        _stack = stack.copy()
        _ans_seg = ans_seg.copy()
        _ans_seg.append(_stack.pop())
        enum(pending, _stack, _ans_seg)
    stack.append(pending)
    enum(pending + 1, stack, ans_seg)

enum(1, [], [])
