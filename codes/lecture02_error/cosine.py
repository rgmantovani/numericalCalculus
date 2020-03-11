#######################################
#######################################

import math
import numpy as np

#######################################
#######################################

# x: em graus
# es: é o erro de parada
# maxit: número de iterações

def cosseno(x, es, maxit):
    
    iter = 0
    ea   = 100
    
    cosx = 0
    
    # convertendo x para radianos (rads)
    rads = x * (np.pi / 180)
    
    while True:
        
        sol_old = cosx 
   
        # somatório (série)
        cosx = cosx + ((pow(-1, iter) * pow(rads, 2 * iter)) / math.factorial(2 * iter))
   
        iter = iter + 1
 
        # atualização do erro
        if(cosx  != 0):
            ea = abs((cosx  - sol_old)/cosx ) * 100
        
        # critério de parada
        if(ea <= es or iter >= maxit):
            break
        
    return cosx , ea, iter

#######################################
# *** Casos de teste
#######################################
    
# cosseno(x = 0, es = 1e-10, maxit = 100)
# (1.0, 0.0, 2)

# cosseno(x = 90, es = 1e-10, maxit = 100)
# (4.2539467343847764e-17, 1.6863642882192947e-11, 17)

# cosseno(x = 180, es = 1e-10, maxit = 100)
# (-1.0000000000000004, 2.0872192862952935e-12, 14)

# cosseno(x = 270, es = 1e-10, maxit = 100)
# (1.303366028307835e-15, 1.2710227710284156e-12, 25)

# cosseno(x = 360, es = 1e-10, maxit = 100)
# (0.9999999999999942, 1.458833054357464e-11, 19)

#######################################