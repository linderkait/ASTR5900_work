import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import math

#Problem 2
#Part a

#define data to interpolate
p2xdata = np.array([-1, 0, 1, 2, 3, 3.5, 5, 6, 7, 8])
p2ydata = np.array([-3, -1, 1, 3, 3, 1, 4, 2, 1, 1])

#create the interpolation function
def piecewise(x, xdata, ydata):
    # x refers to the array of points on the x axis you want to y data on from the interpolation
    # xdata and ydata refers to the dataset you want interpolated 
    # xdata must be in order from least to greatest
    
    #avoid data outside of xdata range
    y = np.array([])
    for n in range(len(x)):
        if x[n] < xdata[0] or x[n] > xdata[-1]:
            print("requested point outside of data range")
            return
        #find the xdata value index directly below the x value
        else:
            xdiff = x[n] - xdata
            xneg = xdiff[xdiff <= 0]
            i = len(xdata) - len(xneg) - 1

            #find the corresponding y value to the x on the line between the points directly around it
            y = np.append(y, (ydata[i+1]-ydata[i])/(xdata[i+1]-xdata[i]) * (x[n]-xdata[i]) + ydata[i])
    return y

#create test data
x = np.linspace(p2xdata[0], p2xdata[-1], 100)
y = piecewise(x, p2xdata, p2ydata)

#plot the results
plt.scatter(p2xdata, p2ydata, label="data with interpolation")
plt.plot(p2xdata, p2ydata)
plt.scatter(x, y, label="test points", alpha = 0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Piecewise Interpolation")
plt.legend()
plt.show()



#Part b

#Use the scipy code with variables defined in part a to interpolate
csp = sp.interpolate.CubicSpline(p2xdata,p2ydata)
y_csp = csp(x)

#plot the results against eachother
plt.scatter(p2xdata, p2ydata, label="origional data")
plt.scatter(x, y_csp, label="cubic spline", alpha = 0.5)
plt.scatter(x, y, label="piecewise", alpha = 0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Two ways of Interpolation")
plt.legend()
plt.show()



#Problem 3
#create the dataset
def p3eqn(x):
    return np.sin((math.pi/2)*x) + x/2

p3xdata = np.arange(11)
p3ydata = p3eqn(p3xdata)

#part a
#create the interpolation using the two methods
p3x = np.linspace(p3xdata[0], p3xdata[-1], 100)
p3y = piecewise(p3x, p3xdata, p3ydata)

p3csp = sp.interpolate.CubicSpline(p3xdata, p3ydata)
p3y_csp = p3csp(p3x)

#plot the results
plt.scatter(p3x, p3y_csp, label="cubic spline", alpha = 0.5)
plt.scatter(p3x, p3y, label="piecewise", alpha = 0.5)
plt.scatter(p3xdata, p3ydata, label="origional data")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sin Interpolation")
plt.legend()
plt.show()