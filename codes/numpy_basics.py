a = arange(15).reshape(3, 5)
a

type(a)

a.shape

(rows, cols) = a.shape
rows
cols

a.ndim
#2
a.size
# 15

a[2, 3]

a[2][3]

a[-1]
# array([10, 11, 12, 13, 14])

# >>> a[-2]
# array([5, 6, 7, 8, 9])
# >>> a[-2:]
# array([[ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])
# >>> a[2:]
# array([[10, 11, 12, 13, 14]])
# >>> a[:-3]
# array([], shape=(0, 5), dtype=int64)
# >>> a[:]
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])
# >>> a[1, ...]
# array([5, 6, 7, 8, 9])
# >>> a[:, 0]
# array([ 0,  5, 10])
# A numpy array can be created from a regular Python list or tuple using the array function. The type of the array elements depends on that of the elements in the sequences.
#
# >>> a = array([[1, 2], [2, 3]])
# >>> a
# array([[1, 2],
#        [2, 3]])
# >>> a = array(((4, 5), (6, 7)))
# >>> a
# array([[4, 5],
#        [6, 7]])
# >>> a.dtype
# dtype('int64')
# >>>>>> b = array([(1.2, 1.3), (1.4, 1.5)])
# >>> b
# array([[ 1.2,  1.3],
#        [ 1.4,  1.5]])
# >>> b.dtype
# dtype('float64')
# Numpy includes functions that create arrays with default values. The eye() function creates a identity matrix and the identity() performs a similar function. The copy function clones an array object includes the data it contains.
#
# >>> zeros((2, 3))
# array([[ 0.,  0.,  0.],
#        [ 0.,  0.,  0.]])
# >>> ones((3, 4))
# array([[ 1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.],
#        [ 1.,  1.,  1.,  1.]])
# >>> empty((2, 3))
# array([[  2.68156159e+154,   2.68156159e+154,   2.68156242e+154],
#        [  2.68156159e+154,   2.68156159e+154,   2.68156159e+154]])
# >>> eye(3, 3)
# array([[ 1.,  0.,  0.],
#        [ 0.,  1.,  0.],
#        [ 0.,  0.,  1.]])
# >>> identity(3, float)
# array([[ 1.,  0.,  0.],
#        [ 0.,  1.,  0.],
#        [ 0.,  0.,  1.]])
# Arithmetic operations on numpy arrays are element-wise operations. The product * operator does a element-wise multiplication. The dot function performs matrix multiplications.
#
# >>> a
# array([[1, 2],
#        [3, 4]])
# >>> b = a.copy()
# >>> b
# array([[1, 2],
#        [3, 4]])
# >>> a*b
# array([[ 1,  4],
#        [ 9, 16]])
# >>> dot(a, b)
# array([[ 7, 10],
#        [15, 22]])
# Numpy also includes a number of basic linear algebra functions.
#
# >>> from numpy.linalg import *
# >>> a = array([[1.0, 2.0], [3.0, 4.0]])
# >>> a
# array([[ 1.,  2.],
#        [ 3.,  4.]])
# >>> a.transpose()
# array([[ 1.,  3.],
#        [ 2.,  4.]])
# >>> inv(a)
# array([[-2. ,  1. ],
#        [ 1.5, -0.5]])
# >>> y = array([[5.], [7.]])
# >>> solve(a, y)
# array([[-3.],
#        [ 4.]])
