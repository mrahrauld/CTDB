import numpy as np
M = np.loadtxt('matrix.txt', delimiter=',')
A = M[:,0:-1]
b = M[:,-1]
x=np.linalg.solve(A, b) #solving the linear matrix equation

print('x is: ', x)
if np.array_equal(b,A.dot(x)):
    print('b and A*x are equal')
elif np.allclose(b,A.dot(x)):
    print('b and A*x are almost equal')
else:
    print('The result does not make sense')
