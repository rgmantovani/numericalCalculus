# Based on the code by Nick Higham
# https://gist.github.com/higham/6f2ce1cdde0aae83697bca8577d22a6e
# Compares relative error formulations using single precision and compared to double precision

N = 501    # Note: Use 501 instead of 500 to avoid the zero value
d = numpy.finfo(numpy.float32).eps * 1e4
a = 3.0
x = a * numpy.ones(N, dtype=numpy.float32)
y = [x[i] + numpy.multiply((i - numpy.divide(N, 2.0, dtype=numpy.float32)), d, dtype=numpy.float32) for i in range(N)]

# Compute errors and "true" error
relative_error = numpy.empty((2, N), dtype=numpy.float32)
relative_error[0, :] = numpy.abs(x - y) / x
relative_error[1, :] = numpy.abs(1.0 - y / x)
exact = numpy.abs( (numpy.float64(x) - numpy.float64(y)) / numpy.float64(x))

# Compute differences between error calculations
error = numpy.empty((2, N))
for i in range(2):
    error[i, :] = numpy.abs((relative_error[i, :] - exact) / numpy.abs(exact))

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
axes.semilogy(y, error[0, :], '.', markersize=10, label="$|x-y|/|x|$")
axes.semilogy(y, error[1, :], '.', markersize=10, label="$|1-y/x|$")

axes.grid(True)
axes.set_xlabel("y")
axes.set_ylabel("Relative Error")
axes.set_xlim((numpy.min(y), numpy.max(y)))
axes.set_ylim((5e-9, numpy.max(error[1, :])))
axes.set_title("Relative Error Comparison")
axes.legend()
plt.show()
