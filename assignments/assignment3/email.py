def validate(_email: str):
    at_cnt = 0
    at_index = 0
    for i in range(len(_email)):
        if _email[i] == "@":
            at_cnt += 1
            at_index = i
    if at_cnt != 1:
        return False
    if _email[0] == "@" or _email[-1] == "@" or _email[0] == "." or _email[-1] == ".":
        return False
    if _email[at_index + 1] == "." or _email[at_index - 1] == ".":
        return False
    for i in range(at_index + 2, len(_email)):
        if _email[i] == ".":
            return True
    return False


while True:
    try:
        email = input().strip()
    except:
        break
    if not email:
        break
    print("YES" if validate(email) else "NO")
