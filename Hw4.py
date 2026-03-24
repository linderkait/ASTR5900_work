import numpy as np
import matplotlib.pyplot as plt

#Problem 1
#Part a
#define a two body code
def twobody(M, r0, V0, t, n):
    #M is the mass of the primary interacting object, r0 is the initial position and t is how long the simulation should be run
    #A circular orbit is assumed.
    delt = t/n
    a = 
    Vhalf = V0 + .5 * a * delt
    x =  x + Vhalf * delt
    anew = 
    V = Vhalf + 0.5 * anew * delt