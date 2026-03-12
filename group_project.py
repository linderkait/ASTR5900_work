import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.special import comb

#define binomial probability
def binomial(n, h, theta):
    return comb(n,h) * (theta**h) * ((1-theta)**(n-h))

#liklihood function
def L(data, ntrials, theta):
    nh = (r <= 1).sum()
    return binomial(ntrials, nh, theta)

#prior/beta function
def prior(a, b, theta):
    return (gamma(a+b)/(gamma(a)*gamma(b))) * (theta ** (a-1)) * ((1-theta)**(b-1))

theta = np.linspace(0, 1, 100)

#test several datasets
for i in [5, 50, 500]:
    x = np.random.rand(i)
    y = np.random.rand(i)

    r = np.sqrt(x**2 + y**2)


    prob = L(r, i, theta) * prior(2, 2, theta)

    #print the value of pi/4 and plot the distribution
    print(theta[np.argmax(prob)])
    plt.plot(theta, prob)
    plt.xlabel('$\pi$/4')
    plt.ylabel('Probability')
    plt.title("number of points: "+str(i))
    plt.show()
