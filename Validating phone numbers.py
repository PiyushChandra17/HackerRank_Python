import re

N = int(input())
for i in range(N):
    if re.search(r'^[789]\d{9}$',input()):
        print('YES')
    else:
        print('NO')
