# To speed up Python's performance, usually for array operations,
# most of the code provided here use NumPy, a Python's scientific
#computing package. However, for comparison, code without NumPy
#are also presented. To see the costs of running code with
#different styles of coding/implementation, we compare three
#different ways of calculating the sum of x^2 with x  going from 0 to N−1
 # and time the execution for each method using the timeit module.

import timeit
import numpy as np

def forloopmethod(N):
    a1 = [0]*N
    for i in range(N):
        a1[i] = float(i)**2
    return sum(a1)

def listcompmethod(N):
    a2 = [float(i)**2 for i in range(N)]
    return sum(a2)

def numpymethod(N):
    a3 = np.sum(np.arange(0, N)**2, dtype='d')
    return a3

# and when N = 10000000, using the timeit module to time each
# method execution:

print(timeit.timeit('[func(N) for func in (forloopmethod,)]',
globals=globals(), number=1))

print(timeit.timeit('[func(N) for func in (listcompmethod,)]',
globals=globals(), number=1))

print(timeit.timeit('[func(N) for func in (numpymethod,)]',
globals=globals(), number=1))

# we obtain that the first method with conventional for loop takes
# the longest time to run, about 3.4 seconds, the second method
# with list comprehension runs for about 3.2 seconds, and the
# method with NumPy runs the fastest, about 0.1 seconds.
# An example code to measure execution time is available here.
