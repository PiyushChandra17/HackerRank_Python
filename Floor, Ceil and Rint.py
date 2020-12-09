import numpy as np
N = input().split()
np.set_printoptions(sign=' ')
A = np.array(N,dtype=float)

print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))
