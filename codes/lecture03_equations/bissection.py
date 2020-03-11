#######################################
#######################################

from __future__ import division

#######################################
#######################################

# Parametros de entrada: 

# f     = função objeito
# a     = extremo esquerdo do intervalo [a, b]
# b     = extremo direito  do intervalo [a, b]
# es    = tolerância para o erro absoluto ( critério de parada)
# maxit = número máximo de iterações


# Saida:

# p     = aproximação de uma raiz x∗ de f, 
#          satisfazendo |p−x∗| < TOL ou f(p) = 0.
# its   = numero de iteracoes necessárias 

def bissecao(f, a, b, es, maxit):  
    
    its = 1  
    fa = f(a)  
    
    while (its <= maxit):  
        
        # iteracao da bissecao  
        p = a + (b-a)/2  
        fp = f(p)  
        
        # condicao de parada  
        if ((fp == 0) or ((b-a)/2 < es)):  
            return p, its  
        
        # bissecta o intervalo  
        its = its + 1  
        
        if (fa * fp > 0):  
            a = p  
            fa = fp  
        else:  
            b = p

#######################################
# Casos de teste
#######################################

#E 3.2.1. Considere a equação √x = cos(x). Use o método da bisseção 
# com intervalo inicial [a, b] = [0, 1] e x(1) = (a + b)/2 para 
# calcular a aproximação x(4) da solução desta equação.


# E 3.2.3. O polinômio p(x) = −4+8x−5x2+x3 tem raízes x1 = 1 e x2 = x3 = 2 
# no intervalo [1/2, 3].
            
# a) Se o método da bisseção for usando com o intervalo inicial [1/2, 3], 
# para qual raiz as iterações convergem?

def fx(x):
    value = -4 + (8 * x) - 5 * pow(x, 2) + pow(x, 3)
    return(value)
    
[sol, its] = bissecao(f = fx, a = 1/2, b = 3, es = 1e-6, maxit = 1000)
print(sol, its) #1.0000001192092896 22

# b) É possível usar o método da bisseção para a raiz x = 2? 
#  Justifique sua resposta.

[sol, its] = bissecao(f = fx, a = 1.2, b = 2.9, es = 1e-6, maxit = 1000)
print(sol, its) # não acha!

#######################################
#######################################
