import numpy as np
import matplotlib.pyplot

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
    i = 0
    while x < xf:
        i += 1
        y += h * f(x, y)
        x += h
    else:
        return y


#test the euler code
test = euler(p1, 0, 1, 0, 5) 
true = np.tan(1)
print(f'The value from the euler method is {test:.3g} and the true value is {true:.3g}')