The SymPy library for Python allows us to manipulate variables symbolically (as symbols). The following code snippets demonstrates some basic functionality of SymPy.

>>> from sympy import Symbol
>>> x = Symbol('x');
>>> x+2*x+3*x
6*x
>>> y=x+2*x+3*x
>>> y
6*x
>>> y.subs(x, 2)
12
>>> from sympy import diff
>>> diff(y, x)
6
>>> from sympy import sin, cos
>>> diff(sin(x), x)
cos(x)
>>> diff(cos(x), x)
-sin(x)
>>> y = 4 - 1/x
>>> y.diff()
x**(-2)
>>> y.diff().subs(x, 0.5)
4.00000000000000
>>> from sympy import series
>>> sin(x).series(x, 0)
x - x**3/6 + x**5/120 + O(x**6)
>>> sin(x).series(x, 0, 10)
x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 + O(x**10)
