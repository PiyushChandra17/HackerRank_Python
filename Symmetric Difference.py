
_,M = input(),set(map(int,input().split()))
_,N = input(),set(map(int,input().split()))

print(*sorted(list(M.symmetric_difference(N))),sep='\n')
