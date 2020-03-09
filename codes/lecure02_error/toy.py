#You can print numbers using a format string similar to the printf function in C.

a = 0.1

# print "%20.19f" % a
# 0.1000000000000000056

# This example show the limit of the floating point number representation.
# 1/10 can not be represented precisely because it is not a power of two.
# Even though the console prints a as 0.1 the underlying representation
# is almost 0.1.

a = math.sqrt(2)
# >>> a
# 1.4142135623730951
a ** 2
# 2.0000000000000004
