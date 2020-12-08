import re

N = int(input())
for _ in range(N):
    try:
        print(bool(re.compile(input())))
    except re.error:
        print('False')
