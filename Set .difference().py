# Enter your code here. Read input from STDIN. Print output to STDOUT
_, A = input(),set(input().split())
_, B = input(),set(input().split())

print(len(A.difference(B)))
