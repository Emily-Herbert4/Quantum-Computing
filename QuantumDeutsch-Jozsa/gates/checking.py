import numpy as np
import gates as g
#import uncertainties import unumpy
#rounding up to error decimal places
error =6
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
    if np.array_equiv(np.round(ket,error),np.round(ket_c,error)) or np.array_equiv(np.round(ket,error),np.round(-ket_c,error)):
        return 'constant'
    if np.array_equiv(np.round(ket,error),np.round(ket_b,error)) or np.array_equiv(np.round(ket,error),np.round(-ket_b,error)):
        return 'balance'
    return "Does not fall under constant or balance function"
#print(check(ket_test))

def targets():
    #Opperators used 
    thetas = [0,np.pi/2,np.pi]
    values  =[]
    for i in thetas:
      for j in thetas:
        polarizer = np.kron(g.I,(np.sqrt(2))*g.P(-np.pi/4))
        beamsplitter_one = np.kron(g.BS,g.Z)
        WavePlate = g.W_4(i,j)
        Mirror = np.kron(g.M,-g.Z)
        beamsplitter_two = np.kron(g.BS,g.I)
        input_ket = np.kron(g.ket_0,g.ket_V)
        
        #kets
        ket_0 = np.matmul(polarizer,input_ket)
        ket_1 =np.matmul(beamsplitter_one,ket_0)
        ket_2 =np.matmul(WavePlate,ket_1)
        ket_3 = np.matmul(Mirror,ket_2)
        ket_4 = np.matmul(beamsplitter_two,ket_3)
        values.append(ket_4)
    return values