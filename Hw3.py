import numpy as np
import matplotlib.pyplot as plt

#adjust global plot font size
plt.rcParams['font.size'] = 14

#Problem 1

#define the function to use in this part
def p1(x, y):
    return y**2 + 1

#create code for the euler method
def euler(f, xi, xf, yi, n):
    #f is the function to integrate, xi and xf are the end points of integration, yi is the
    #initial y value and n is the number of steps.
    
    #define h (step size), initial x value, y value and iteration
    h = (xf - xi) / n
    x = xi
    y = yi

    #create the loop to do the intergration
    while x < xf:
        y += h * f(x, y)
        x += h
    else:
        return y


#test the euler code
testeu = euler(p1, 0, 1, 0, 5) 
true = np.tan(1)
print(f'The value from the euler method is {testeu:.10g} and the true value is {true:.10g}')



def RK4(f, xi, xf, yi, n):
    #f is the function to integrate, xi and xf are the end points of integration, yi is the
    #initial y value and n is the number of steps.
    
    #define h (step size), initial x value, y value and iteration
    h = (xf - xi) / n
    x = xi
    y = yi

    #create the loop to do the integration
    while x < xf:
        k1 = f(x, y)
        k2 = f(x + h/2, y + (h / 2) * k1)
        k3 = f(x + h/2, y + (h / 2) * k2)
        k4 = f(x + h, y + h * k3)

        y += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
    else:
        return y
    


#test the RK code
testRK = RK4(p1, 0, 1, 0, 5)
print(f'The value from the RK4 method is {testRK:.10g} and the true value is {true:.10g}')



#Part b
x = np.linspace(-4, 4, 1000)
y = np.tan(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()



#Part d
#define a range of step sizes over a few magnitudes
narr = np.logspace(0, 3, 50)
harr = 1/narr

#define the highest resolution case
Eufinal = euler(p1, 0, 1, 0, narr[-1]) 
RKfinal = RK4(p1, 0, 1, 0, narr[-1])

#calculate the predicted y with each step size
Eudiff = np.array([])
RKdiff = np.array([])

for i in narr:
    Eu = euler(p1, 0, 1, 0, i) 
    RK = RK4(p1, 0, 1, 0, i)

    Eudiff = np.append(Eudiff, Eufinal - Eu)
    RKdiff = np.append(RKdiff, RKfinal - RK)

#plot the results
plt.loglog(harr, abs(Eudiff), label = 'Euler')
plt.loglog(harr, abs(RKdiff), label = 'Runge-Kutta')
plt.xlabel('log(step size)')
plt.ylabel('log(|highest res - predicted|)')
plt.legend()
plt.show()


#Part e
#find the difference between the two highest resolution cases and compare
print(f'The difference between the two highest resolution cases for Euler is: {abs(Eudiff[-2]):.5g}')
print(f'The difference between the two highest resolution cases for RK4 is: {abs(RKdiff[-2]):.5g}')
print(f'The difference between the highest resolution and true values for Euler is: {abs(Eufinal - true):.5g}')
print(f'The difference between the highest resolution and true values for RK4 is: {abs(RKfinal - true):.5g}')



#Problem 2

#define the equation
def p2(v, y):
    #define constants using protons for mass
    m = 1.67262192e-27
    k = 1.380649e-23
    T = 10000
    f = ((m / (2 * np.pi * k * T)) ** (3 / 2)) * (4 * np.pi * v ** 2) * np.exp(-((m * v ** 2) / (2 * k * T)))
    return f

#Part a
#define velocity array and probability density array
v = np.linspace(0, 4e4, 100)
f = p2(v, 0)

#plot the distribution
plt.plot(v, f)
plt.xlabel('v(m/s)')
plt.ylabel('f(v)')
plt.show()



#part b
#calculate the minimum velocity
delE = 10.2    #energy in eV
E = 10.2 * 1.6022e-19    #energy in J
m = 1.6726e-27    #mass of a proton
vmin = np.sqrt(2 * E / m)    #minimum velocity

print(f'The minumum velocity of a proton to acheive an energy of {E:.3g} J is {vmin:.3g} m/s')

#integrate from the minimum speed to infinity
frac = RK4(p2, vmin, 1e10, 0, 1000)
print(f'The fraction of atoms able to excite electrons out of the ground state is {frac:.3g}')