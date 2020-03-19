#----------------------------------------------------------------
#----------------------------------------------------------------

import numpy as np
from aproximacoesSucessivas import aproximacoesSucessivas

#----------------------------------------------------------------
#----------------------------------------------------------------
# Exemplo 3.2 - pgs 99 - 100 - Livro da Selma Arenales
#----------------------------------------------------------------

# funcao original
# fx = cos(x) - x
# es = 0.01
      
def fx(x):
  return(np.cos(x) - x)
      
# Obtendo phi
#cos(x) - x = 0
#x = cos(x)
#phi(c) = cos(x)  
    
def phi(x):
  return(np.cos(x))

m = aproximacoesSucessivas(xo = 0.7, phi = phi, es = 0.01, maxit = 100)

print("\n[*] Solução =",  m[0], "iters =", m[1], "erro =", m[2]) 
 
#----------------------------------------------------------------
#----------------------------------------------------------------
