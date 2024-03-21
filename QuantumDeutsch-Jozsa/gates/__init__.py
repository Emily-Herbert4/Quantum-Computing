import numpy as np
#identy
I = np.array([[1,0],[0,1]])

#Kets
ket_0 = np.array([1,0])
ket_1 = np.array([0,1])

""" Here are some of the common quantum gates"""
#Pauli gates
M = np.array([[0,1],[1,0]])
Y = np.array([[0, -1j],[1j,0]])
Z = np.array([[1,0],[0,-1]])
#Hadamard
H = (1/np.sqrt(2))*np.array([[1,1],[1,-1]])
#phase gate S (sqrt Z)
S = np.array([[1,0],[0,1j]])
#Square root of X,square root of NOT
V = (0.5)*np.array([[1+1j,1-1j],[1-1j,1+1j]])
#CNOT
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
#Anticontrolled-NOT,anticontrolled-X,zero control,control-on-0-NOT,reversible exclusive NOR
XNOR= np.array([[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]])
#Controlled-Z,controlled sign flip,controlled phase flip
CZ = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]])
#Double-controlled NOT
DCNOT = np.array([[1,0,0,0],[0,0,1,0],[0,0,0,1],[0,1,0,0]])
#Swap
SWAP = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
#Imagary Swap
SWAP = np.array([[1,0,0,0],[0,0,1j,0],[0,1j,0,0],[0,0,0,1]])

"""Gates created for the Senior Project Setup Spring 2024"""
BS = (1/np.sqrt(2))*np.array([[1,-1j],[-1j,1]])

#Polairazor opperator
def P(theta):
    ket_theta= np.array([np.cos(theta),np.sin(theta)])
    return np.outer(ket_theta,ket_theta)


def M_theta(theta):
    sin = np.sin(theta)
    cos = np.cos(theta)
    if (sin<10**-10):
        sin = 0
    if (cos<10**-10):
        cos = 0
    P = np.array([[cos, -sin],[sin, cos]])
    return P

def W_4 (theta_0,theta_1):
    w_0 =np.sin(2*theta_0)
    w_1 =np.sin(2*theta_1)
    #This accounts for rounding errors
    if (w_0<10**-15):
        w_0 = 0
    if (w_1<10**-15):
        w_1 = 0
    w = np.array([[w_0, np.cos(2*theta_0),0,0],
                  [np.cos(2*theta_0),-w_0,0,0],
                  [0,0,w_1, np.cos(2*theta_1)],
                  [0,0,np.cos(2*theta_1),-w_1]])
    return w

#trying the matrix guess and returning results for every possible waveplate combonation
def WavePlate_guess(guess):
    angle = [0,np.pi/2,np.pi]
    M_tests = np.array[8]
    for theta_0 in angle:
        for theta_1 in angle:
            M_tests.append(guess.dot(W_4(theta_0,theta_1)))
    return M_tests

