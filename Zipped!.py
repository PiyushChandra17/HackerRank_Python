'''n,x = map(int,input().split())

sheet = []

for _ in range(x):
    sheet.append(map(float,input().split()))

for i in zip(*sheet):
    print(sum(i)/len(i))'''

[print(sum(i)/len(i))for i in zip(*[map(float,input().split()) for _ in range(int(input().split()[1]))])]
