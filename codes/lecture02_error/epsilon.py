import numpy as np

#np.finfo().eps = The smallest representable positive number such that 1.0 + eps != 1.0.
# Type of eps is an appropriate floating point type.

print(np.finfo(float).eps)
print(np.finfo(np.float32).eps)
print(np.finfo(np.float64).eps)
