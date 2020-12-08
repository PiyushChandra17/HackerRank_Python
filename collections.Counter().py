import collections

num_of_shoes = int(input())
stocks_shoes_sizes = collections.Counter(map(int,input().split()))

total_revenue = 0

for _ in range(int(input())):
    size,price = map(int,input().split())
    if stocks_shoes_sizes[size]:
        total_revenue += price
        stocks_shoes_sizes[size] -= 1
print(total_revenue)
