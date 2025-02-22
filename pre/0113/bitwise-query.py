# http://cs101.openjudge.cn/25dsapre/05345/

steps = int(input().split()[1])
nums = list(map(int, input().split()))

for i in range(steps):
    inp = input().split()
    cmd = inp[0]
    num = int(inp[1])
    if cmd == "C":
        nums = list(map(lambda x: x + num, nums))
    else:
        result = 0
        for x in nums:
            if x >> num & 1:
                result += 1
        print(result)
