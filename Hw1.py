import numpy as np
import matplotlib.pyplot as plt

#Problem 2
#Part a

#define data to interpolate
xdata = np.array([-1, 0, 1, 2, 3, 3.5, 5, 6, 7, 8])
ydata = np.array([-3, -1, 1, 3, 3, 1, 4, 2, 1, 1])

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
x = np.linspace(xdata[0], xdata[-1], 100)
y = piecewise(x, xdata, ydata)

#plot the results
plt.scatter(xdata, ydata, label="data with interpolation")
plt.plot(xdata, ydata)
plt.scatter(x, y, label="test points", alpha = 0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Piecewise Interpolation")
plt.legend()
plt.show()