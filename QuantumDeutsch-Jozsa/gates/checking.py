import gates as g
import numpy as np
#import uncertainties import unumpy

one_sqrt2=(1/np.sqrt(2))
#Constant 
#ket_cb = np.kron((1j/np.sqrt(2))*(g.ket_a), g.ket_H-g.ket_V)
ket_c =(one_sqrt2)*np.array([0,0,-1j,1j])
ket_b = (one_sqrt2)*np.array([1,-1,0,0])


"""ket_test= 1.0111*ket_b
print(ket_test)
print(np.round(ket_b,4))
print(np.round(ket_test,4))
print(np.array_equiv(np.around(ket_b,4),np.around(ket_test,4)))"""
def output(ket):
    #error 2 is around a 1.11% rounding error acounted for
    error =4
    if np.array_equiv(np.round(ket,error),np.round(ket_c,error)) or np.array_equiv(np.round(ket,error),np.round(-ket_c,error)):
        return 'constant'
    if np.array_equiv(np.round(ket,error),np.round(ket_b,error)) or np.array_equiv(np.round(ket,error),np.round(-ket_b,error)):
        return 'balance'
    return "Does not fall under constant or balance function"
#print(check(ket_test))