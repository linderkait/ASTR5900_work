import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.special import comb
plt.rcParams['font.size'] = 14

#Problem 2:
#define the function
def bayes(prior, data, likelihood, trials, theta):
    #prior is the prior function inputting theta, the data is an array of data(1 means specific event you are tracking
    #probability of 0 means other events), the likelihood function takes inputs of trials as the total number of events and h 
    #as the number of specific event that is being tracked. Trials is the number of data points you would like to use in your 
    #function. Theta is the probability of your specific event occuring. Outputs the posterior probability distribution function.
    h = sum(data[:trials])
    posterior = prior(theta, a, b) * likelihood(trials, h, theta)
    return posterior

#Part 2a:
#define the liklihood function
def binomial(n, h, theta):
    return comb(n, h) * (theta ** h) * ((1 - theta) ** (n - h))

#define the prior/beta function
def prior(theta, a, b):
    return (gamma(a + b) / (gamma(a) * gamma(b))) * (theta ** (a - 1)) * ((1 - theta) ** (b - 1))

#determine theta
theta = np.linspace(0, 1, 100)

#import data
data = np.loadtxt('data.txt', dtype=int)

#run and plot the function
a = 2
b = 5
prob1 = bayes(prior, data, binomial, 500, theta)

plt.plot(theta, prob1)
plt.xlabel(r'$\theta$')
plt.ylabel('Probability')
plt.show()






#test several datasets
#for i in [5, 50, 500]:
    #x = np.random.rand(i)
    #y = np.random.rand(i)

    #r = np.sqrt(x**2 + y**2)


    #prob = L(r, i, theta) * prior(2, 2, theta)

    #print the value of pi/4 and plot the distribution
    #print(theta[np.argmax(prob)])
    #plt.plot(theta, prob)
    #plt.xlabel('$\pi$/4')
    #plt.ylabel('Probability')
    #plt.title("number of points: "+str(i))
    #plt.show()
