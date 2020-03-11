def erroVerdadeiro(val, x):
	Et = val - x
	return(Et)

def erroRelativo(val, Et):
	et = (Et/val) * 100
	return(et)

# ponte -> val = 10000, x = 9999
E_ponte = erroVerdadeiro(val = 10000, x = 9999)
e_ponte = erroRelativo(val = 10000, Et = E_ponte)
print("E_t = ", E_ponte, ", et = ", e_ponte, "%")

# rebite -> val = 10, x = 9
E_rebite = erroVerdadeiro(val = 10, x = 9)
e_rebite = erroRelativo(val = 10, Et = E_rebite)
print("E_t = ", E_rebite, ", et = ", e_rebite, "%")
