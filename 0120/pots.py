# http://cs101.openjudge.cn/practice/03151/

from collections import deque

A, B, C = map(int, input().split())
pending = deque()
visited = [[False for _ in range(B + 1)] for _ in range(A + 1)]
visited[0][0] = True
visited[A][0] = True
visited[0][B] = True

pending.append({"actions": ["FILL(1)"], "status": (A, 0)})
pending.append({"actions": ["FILL(2)"], "status": (0, B)})

while pending:
    current = pending.popleft()
    (a, b) = current["status"]
    if a == C or b == C:
        print(len(current["actions"]))
        print("\n".join(current["actions"]))
        exit(0)
    # FILL(1)
    if not visited[A][b]:
        visited[A][b] = True
        new_actions = current["actions"].copy()
        new_actions.append("FILL(1)")
        pending.append({"actions": new_actions, "status": (A, b)})
    # FILL(2)
    if not visited[a][B]:
        visited[a][B] = True
        new_actions = current["actions"].copy()
        new_actions.append("FILL(2)")
        pending.append({"actions": new_actions, "status": (a, B)})
    # DROP(1)
    if not visited[0][b]:
        visited[0][b] = True
        new_actions = current["actions"].copy()
        new_actions.append("DROP(1)")
        pending.append({"actions": new_actions, "status": (0, b)})
    # DROP(2)
    if not visited[a][0]:
        visited[a][0] = True
        new_actions = current["actions"].copy()
        new_actions.append("DROP(2)")
        pending.append({"actions": new_actions, "status": (a, 0)})
    # POUR(1,2)
    b_vacant = B - b
    new_status: tuple
    if b_vacant > a:
        new_status = (0, b + a)
    else:
        new_status = (a - b_vacant, B)
    if not visited[new_status[0]][new_status[1]]:
        visited[new_status[0]][new_status[1]] = True
        new_actions = current["actions"].copy()
        new_actions.append("POUR(1,2)")
        pending.append({"actions": new_actions, "status": new_status})
    # POUR(2,1)
    a_vacant = A - a
    new_status: tuple
    if a_vacant > b:
        new_status = (a + b, 0)
    else:
        new_status = (A, b - a_vacant)
    if not visited[new_status[0]][new_status[1]]:
        visited[new_status[0]][new_status[1]] = True
        new_actions = current["actions"].copy()
        new_actions.append("POUR(2,1)")
        pending.append({"actions": new_actions, "status": new_status})

print("impossible")
