import numpy as np


A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])

alpha = 6
# q12 - not possible


# q13 - perform a - c.T
#print(A - C.T)


# q14
#print(C.T + 3 * D)

# q15
#print(B.dot(A))

# q16 - not possible

#  q17
#print(B.dot(B.dot(B.dot(B))))

print(B.dot(C))

