# http://cs101.openjudge.cn/2025sp_routine/04015

import re

pattern = re.compile(r"^[^@\.](?:[^@]*?[^@\.])?@[^@\.][^@]*?\.[^@]*?[^@\.]$")

while True:
    try:
        email = input()
    except:
        break
    print("YES" if pattern.match(email) else "NO")
