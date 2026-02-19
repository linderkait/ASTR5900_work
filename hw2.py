import numpy as np

#create the bisection function
def bisection(func, x0, x1, tol):
    #inputs are the function you want the root of (func), the initial guesses (x0 and x1)
    #and the toerance of the relative error (tol)
    #will return the x location of the root followed by how many iterations

    #define interval
    i = 0
    
    #check that x0 and x1 are on opposite sides of the x axis and are not the root
    if func(x0) * func(x1) > 0:
        return print('Code failed. Check your initial guesses.')
    elif func(x0) == 0:
        return x0, i
    elif func(x1) == 0:
        return x1, i
    else:
        if func(x0) > 0:
            xu = x0
            xl = x1
        else: 
            xu = x1
            xl = x0
    print(f'x_lower is: {xl:.3g}, x_upper is: {xu:.3g}')

    #increase the interval, find first guess for root and set up for loop
    i +=1
    xr = (xu + xl)/2
    xold = xr
    print(f'Iteration: {i}, root guess: {xr:.3g}')

    #see if it is above or below the x axis
    if func(xr) > 0:
        xu = xr
    elif func(xr) < 0:
        xl = xr
    elif func(xr) == 0:
        return xr, i
    
    #use second guess to make error
    i += 1
    xr = (xu + xl)/2
    print(f'Iteration: {i}, root guess: {xr:.3g}')

    rel_err = abs((xr-xold)/xr)
    

    #create loop to continue cycle
    while rel_err > tol:
        print(f'Tolerance not met. relative error: {rel_err:.3g}')

        if func(xr) > 0:
            xu = xr
        elif func(xr) < 0:
            xl = xr
        elif func(xr) == 0:
            return xr, i
        
        xold = xr    

        i += 1 
        xr = (xu + xl)/2
        print(f'Iteration: {i}, root guess: {xr:.3g}')

        rel_err = abs((xr-xold)/xr)

    else:
        print(f'Tolerance met! relative error: {rel_err:.3g}')
        return xr, i
    

#define the function to find the roots of
f = lambda x: x**3 - 7 * x**2 + 14 * x - 5

#test the bisection function
root, interval = bisection(f, 1, 0, 1E-8)



#Create a Newton-Raphson function
def NewtRaph(func, deriv, x0, tol):
    #inputs are the function you want the root of (func), the derivative of this function(deriv)
    #the initial guess (x0) and the toerance of the relative error (tol)
    #will return the x location of the root followed by how many iterations

    #define the iterations
    i = 0

    #make sure the root hasn't been reached already
    if func(x0) == 0:
        return x0, i
 
    #calculate delta x
    delx = func(x0)/deriv(x0)

    i += 1
    #calculate a new guess for the root
    xr = x0 - delx
        
    print(f'Iteration: {i}, root guess: {xr:.3g}')
    delx = func(xr)/deriv(xr)

    #calculate error
    rel_err = abs(delx/xr)

    #create the loop to loop over root finding
    while rel_err > tol:
        print(f'Tolerance not met. relative error: {rel_err:.3g}')
        i += 1
        #calculate a new guess for the root
        xr = xr - delx
        
        print(f'Iteration: {i}, root guess: {xr:.3g}')
        delx = func(xr)/deriv(xr)
        
        rel_err = abs(delx/xr)

        #create an out if it gets stuck
        if i > 100:
            print('No root found. Try a new initial guess.')
            return

    else:
        print(f'Tolerance met! relative error: {rel_err:.3g}')
        return xr, i
    

#Define the derivative for the origional function
fprime = lambda x: 3 * x**2 - 14 * x + 14

#test the Newton-Raphson function
NewtRaph(f, fprime, 0, 1E-8)



#Problem 3
#Define keplers equation
def kepler(E):
    #define variables (can be changed)
    return E - ec * np.sin(E) - M

ec = 0.9    #eccentricity
M = 3    #mean anomoly

#find the root
bisection(kepler, -3, 5, 1E-8)