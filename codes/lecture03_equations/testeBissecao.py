#----------------------------------------------------------------
#----------------------------------------------------------------

import numpy as np
from bissecao import bissecao, bissecao2

#----------------------------------------------------------------
#----------------------------------------------------------------


#E 3.2.1. Considere a equação √x = cos(x). Use o método da bisseção
# com intervalo inicial [a, b] = [0, 1] e x(1) = (a + b)/2 para
# calcular a aproximação da solução desta equação.

def f1(x):
  return(np.sqrt(x) - np.cos(x))

print("\n--------------------------------------")
print("Ex01: f(x) = sqrt(x) - cos(x)")
m1 = bissecao(f = f1, a = 0, b = 1, es = 1e-6, maxit = 100)
print("\n[*] Solução =",  m1[0], "iters =", m1[1])


m2 = bissecao2(f = f1, a = 0, b = 1, es = 1e-6, maxit = 100)
print("\n[*] Solução =",  m2[0], "iters =", m2[1])

#----------------------------------------------------------------
#----------------------------------------------------------------

# E 3.2.3. O polinômio p(x) = −4+8x−5x2+x3 tem raízes x1 = 1 e x2 = x3 = 2
# no intervalo [1/2, 3].

# a) Se o método da bisseção for usando com o intervalo inicial [1/2, 3],
# para qual raiz as iterações convergem?

def f2(x):
    value = -4 + (8 * x) - 5 * pow(x, 2) + pow(x, 3)
    return(value)

print("\n--------------------------------------")
print("Ex02: f(x) = -4 + 8x - 5x^2 + x^3")

m1 = bissecao(f = f2, a = 1/2, b = 3, es = 1e-6, maxit = 1000)
print("\n[*] Solução =",  m1[0], "iters =", m1[1])

m2 = bissecao2(f = f2, a = 1/2, b = 3, es = 1e-6, maxit = 1000)
print("\n[*] Solução =",  m2[0], "iters =", m2[1])


# b) É possível usar o método da bisseção para a raiz x = 2?
#  Justifique sua resposta.


#----------------------------------------------------------------
#----------------------------------------------------------------

# Exercicio: usando o método da bisseção, resolva a equação
#  x^2 + ln(x) = 0, com es = 0.01
# raiz = intersecao dos graficos
print("\n--------------------------------------")
print("\nEx03: f(x) =  x^2 + ln(x)")

def f3(x): 
    return(pow(x, 2) + np.log(x))


m1 = bissecao(f = f3, a = 0.1, b = 1, es = 1e-2, maxit = 100)
print("\n[*] Solução =",  m1[0], "iters =", m1[1])

m2 = bissecao2(f = f3, a = 0.1, b = 1, es = 1e-2, maxit = 100)
print("\n[*] Solução =",  m1[0], "iters =", m1[1])

#----------------------------------------------------------------
#----------------------------------------------------------------
