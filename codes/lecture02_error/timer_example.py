import timeit
import numpy as np


def forloop1(N):
	a1 = 0
	for i in range(N):
		a1 += float(i)*float(i)
	return a1

def forloop2(N):
	a2 = [0]*N
	for i in range(N):
		a2[i] = float(i)**2
	return sum(a2)

# Uses list comprehension
def listcomp(N):
	a3 = [float(i)**2 for i in range(N)]
	return sum(a3)

def numpymethod(N):
	a4 = np.sum(np.arange(0, N)**2, dtype='d')
	return a4


N = 10000000

print("Method 1 =", forloop1(N))
print("Method 2 =", forloop2(N))
print("Method 3 =", listcomp(N))
print("Method 4 =", numpymethod(N))

# print("Method 1 runs for", timeit.timeit('[func(N) for func in (forloop1,)]', globals=globals(), number=1), "seconds")
# print("Method 2 runs for", timeit.timeit('[func(N) for func in (forloop2,)]', globals=globals(), number=1), "seconds")
# print("Method 3 runs for", timeit.timeit('[func(N) for func in (listcomp,)]', globals=globals(), number=1), "seconds")
# print("Method 4 runs for", timeit.timeit('[func(N) for func in (numpymethod,)]', globals=globals(), number=1), "seconds")

#print(timeit.timeit('[func(N) for func in (forloop1,)]', globals=globals(), number=1))
