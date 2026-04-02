import numpy as np
import matplotlib.pyplot as plt

#Problem 1
#Part b
#define the functions
def DFT(f, N, xi, xf):
    #the function takes a function f(x), the number of steps to use N and the range to be integrated xi to xf and outputs the 
    #Fourier transform F(k)
    x = np.linspace(xi, xf, N)
    n = np.arange(N)
    m = np.arange(N)
    transform = 0
    for i in n:
        transform += f(x[i]) * np.exp(- 2j * np.pi * i * m/ N)
    return transform

def iDFT(F, N):
    #the function takes the output from my DFT code a Fourier transform array F and  the number of steps N and outputs
    #inverse Fourier transform f(x)
    n = np.arange(N)
    m = np.arange(N)
    invtransform = 0
    for i in m:
        invtransform += 1 / N * F[i] * np.exp(2j * np.pi * n * i / N)
    return invtransform

#define the function to transform
f = lambda x: np.exp(-50 * (x - 0.5) ** 2)

#calculate the transform for several different n values
xi = 0
xf = 1
L = xf - xi
N = np.array([5, 10, 20])
T1 = DFT(f, N[0], xi, xf)
k1 = 2 * np.pi * np.arange(N[0]) / L

T2 = DFT(f, N[1], xi, xf)
k2 = 2 * np.pi * np.arange(N[1]) / L

T3 = DFT(f, N[2], xi, xf)
k3 = 2 * np.pi * np.arange(N[2]) / L

#calculate the analytical result
ftrue = lambda k: np.exp((-100j * k + k ** 2) / 200) * np.sqrt(np.pi / 50)

Ttrue = ftrue(k3)

#plot the transforms
plt.plot(k1, T1, label = f'N = {N[0]}')
plt.plot(k2, T2, label = f'N = {N[1]}')
plt.plot(k3, T3, label = f'N = {N[2]}')
plt.plot(k3, Ttrue, label = 'analytical result')
plt.show()

#inverse the results
iT1 = iDFT(T1, N[0])
x1 = np.linspace(xi, xf, N[0])

iT2 = iDFT(T2, N[1])
x2 = np.linspace(xi, xf, N[1])

iT3 = iDFT(T3, N[2])
x3 = np.linspace(xi, xf, N[2])

#calculate the analytical result
iFtrue = lambda x: np.exp(-50 * (x - 0.5) ** 2)

iTtrue = iFtrue(x3)