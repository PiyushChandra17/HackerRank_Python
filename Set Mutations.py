# Enter your code here. Read input from STDIN. Print output to STDOUT
_,A = input(),set(map(int,input().split()))

for _ in range(int(input())):
    eval("A."+input().split()[0]+"(set(map(int,input().split())))")
print(sum(A))


