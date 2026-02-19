import numpy as np
import matplotlib.pyplot as plt

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
testeu = euler(p1, 0, 1, 0, 1) 
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
testRK = RK4(p1, 0, 1, 0, 1)
print(f'The value from the RK4 method is {testRK:.10g} and the true value is {true:.10g}')



#Part b
x = np.linspace(-4, 4, 1000)
y = np.tan(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()