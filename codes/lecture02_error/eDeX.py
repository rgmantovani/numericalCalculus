import math

def eDeX(x, es, maxit):
    iter = 1
    sol  = 1
    ea = 100
    while True:
        sol_old = sol
        sol = sol + (pow(x, iter) / math.factorial(iter))
        iter = iter + 1
        if(sol == 0):
            ea = abs((sol - sol_old)/sol) * 100
        if(ea <= es or iter >= maxit):
            break
    return sol, ea, iter

# testes

# teste = eDeX(x = 1, es = 1e-6, maxit = 100)
# math.exp(1)
# 2.718281828459045

# >>> eDeX(x = 2, es = 1e-6, maxit = 100)
# (7.389056098930649, 100, 100)
# >>> math.exp(2)
# 7.38905609893065
