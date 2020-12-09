import numpy as np
N,M = map(int,input().split())
a = np.array([input().split() for _ in range(N)],int)

print(np.max(np.min(a,axis=1)))
