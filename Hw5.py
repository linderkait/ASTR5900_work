import numpy as np
import matplotlib.pyplot as plt
import scipy
import time

#Problem 1
#Part b
#define the functions
def DFT(f, N, xi, xf):
    #the function takes a function f(x), the number of steps to use N and the range to be integrated xi to xf and outputs the 
    #Fourier transform F(k)
    x = np.linspace(xi, xf, int(N))
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
N = np.array([10, 20, 50])
T1 = DFT(f, N[0], xi, xf)
k1 = 2 * np.pi * np.arange(N[0]) / L

T2 = DFT(f, N[1], xi, xf)
k2 = 2 * np.pi * np.arange(N[1]) / L

T3 = DFT(f, N[2], xi, xf)
k3 = 2 * np.pi * np.arange(N[2]) / L

#calculate the analytical result
ftrue = lambda k: np.exp((-100j * k - k ** 2) / 200) * np.sqrt(np.pi / 50)

Ttrue = ftrue(k3)

#plot the transforms
plt.plot(k1, np.abs(T1), label = f'N = {N[0]}')
plt.plot(k2, np.abs(T2), label = f'N = {N[1]}')
plt.plot(k3, np.abs(T3), label = f'N = {N[2]}')
plt.plot(k3, np.abs(Ttrue), label = 'analytical result')
plt.title("Fourier Transform")
plt.ylabel('F(k)')
plt.xlabel('k')
plt.legend()
plt.show()

#inverse the results
iT1 = iDFT(T1, N[0])
x1 = np.linspace(xi, xf, N[0])

iT2 = iDFT(T2, N[1])
x2 = np.linspace(xi, xf, N[1])

iT3 = iDFT(T3, N[2])
x3 = np.linspace(xi, xf, N[2])

#calculate the analytical result

iTtrue = f(x3)

#Plot the inverses
plt.plot(x1, iT1, label = f'N = {N[0]}')
plt.plot(x2, iT2, label = f'N = {N[1]}')
plt.plot(x3, iT3, label = f'N = {N[2]}')
plt.plot(x3, iTtrue, label = 'Origional Function')
plt.title("Inverse Fourier Transform")
plt.ylabel('f(x)')
plt.xlabel('x')
plt.legend()
plt.show()



#Part c
#plot the two functions
test = scipy.fft.fft(f(x2))

plt.plot (k2, np.abs(test), label = 'scipy code')
plt.plot(k2, np.abs(T2), label = 'My code', lw = 0.8)
plt.ylabel('F(k)')
plt.xlabel('k')
plt.legend()
plt.show()

#time the two codes
#start with FFT
t_FFT = np.array([])
j_FFT = np.arange(3, 21)
N_FFT = 2 ** j_FFT

for i in N_FFT:
    x = np.linspace(0, 1, i)
    t_tot = np.array([])
    for j in range(100):
        start = time.perf_counter()
        fft = scipy.fft.fft(f(x))
        end = time.perf_counter()
        t = end - start
        t_tot = np.append(t_tot, t)
    t_FFT = np.append(t_FFT, np.average(t_tot))

#Now DFT
t_DFT = np.array([])
j_DFT = np.arange(3, 11)
N_DFT = 2 ** j_DFT

for i in N_DFT:
    x = np.linspace(0, 1, i)
    t_tot = np.array([])
    for j in range(100):
        start = time.perf_counter()
        dft = DFT(f, i, 0, 1)
        end = time.perf_counter()
        t = end - start
        t_tot = np.append(t_tot, t)
    t_DFT = np.append(t_DFT, np.average(t_tot))

plt.loglog(N_FFT, t_FFT, label = "FFT")
plt.loglog(N_DFT, t_DFT, label = "DFT")
plt.ylabel('t')
plt.xlabel('N')
plt.legend()
plt.show()


#Problem 2
#calculate the DFT of the initial distribution
alpha = 0.005
delt = 0.001
T = 5
N = int(T/delt)

heati = DFT(f, N, 0, 1)

#integrate with scipy runge-kutta code
k_all = 2 * np.pi * np.arange(N)
dudt = lambda t, u:-alpha * k ** 2 * u

heat_kt = np.array([])
for i in np.arange(N):
    k = k_all[i]
    u = heati[i]
    heattrans = scipy.integrate.RK45(dudt, t0 = 0, y0 = u, t_bound = T, step_size = delt)
    heat_kt = np.concatenate(heat_kt, heattrans)
#Inverse transform
heatf = iDFT(heattrans.y, N)

#plot the results
x = np.linspace(0, 1, N)

plt.pcolormesh(x, heattrans.t, np.abs(heatf))
plt.xlabel('Position')
plt.ylabel('time')
plt.colorbar(label = 'heat')
plt.show()