# https://sunnywhy.com/sfbj/7/1/296

tokens = input().split()

result = []

for i in range(len(tokens)):
    if tokens[i] not in "+-*/":
        continue
    if len(result) == 0:
        result.append(tokens[0])
    result.append(tokens[i + 1])
    result.append(tokens[i])

print(" ".join(result))
