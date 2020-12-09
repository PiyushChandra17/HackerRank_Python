import re

n = int(input())
for _ in range(n):
    m = re.findall(r'[\s|\S](#[0-9a-fA-F]{3,6})',input())

    if m:
        print(*m,sep='\n')
