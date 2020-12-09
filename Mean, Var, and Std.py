import numpy as np
np.set_printoptions(legacy='1.13')
N,M = map(int,input().split())


a = np.array([input().split() for _ in range(N)],float)

print(np.mean(a,axis=1))
print(np.var(a,axis=0))
print(np.std(a,axis=None))





