import numpy as np
#identy
I = np.array([[1,0],[0,1]])
""" Here are some of the common quantum gates
"""
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

