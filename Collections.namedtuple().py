from collections import namedtuple
n,student = int(input()),namedtuple('student',input())

print('{:.2f}'.format(sum([int(student(*input().split()).MARKS)for _ in range(n)])/n))
