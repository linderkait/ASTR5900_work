import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from functools import partial

#Problem 1
#Part a
#define a two body code
def twobody(frame, x, y, vx, vy):
    #x and y are the initial position coordinates, vx and vy are initial velocityis, delt is the time step. 
    #A circular orbit is assumed.

    #define some values
    G = 6.674e-11    #gravitational constant
    M = 1    #mass of the object being orbited
    r = np.sqrt(x**2 + y**2)    #radius of orbit
    delt = 0.05

    #calculate acceleration
    a_tot = -G * M / r ** 2    #gravitational acceleration due to central object
    ax = a_tot * (x / r)    #acceleration in the x direction
    ay = a_tot * (y / r)    #acceleration in the y direction

    #Calculate the velocity half step
    vx += 0.5 * ax * delt
    vy += 0.5 * ay * delt

    #calculate the position full step
    x += vx * delt
    y += vy * delt

    #recalculate values
    r = np.sqrt(x**2 + y**2) 

    a_tot = -G * M / r ** 2
    ax = a_tot * (x / r)
    ay = a_tot * (y / r) 

    #calculate the velocity full step
    vx += 0.5 * ax * delt
    vy += 0.5 * ax * delt

    return x, y, vx, vy

def euler(frame, x, y, vx, vy):
    #x and y are the initial position coordinates, vx and vy are initial velocityis, delt is the time step. 
    #A circular orbit is assumed.

    #define some values
    G = 6.674e-11    #gravitational constant
    M = 1    #mass of the object being orbited
    r = np.sqrt(x**2 + y**2)    #radius of orbit
    delt = 0.05

    #calculate acceleration
    a_tot = -G * M / r ** 2    #gravitational acceleration due to central object
    ax = a_tot * (x / r)    #acceleration in the x direction
    ay = a_tot * (y / r)    #acceleration in the y direction

    #use eulers method to find position and velocity
    vx += delt * ax
    vy += delt * ay

    x += delt * vx
    y += delt * vy
    return x, y, vx, vy





#define initial values
x0 = 1
y0 = 0
r = np.sqrt(x0**2 + y0**2)

G = 6.674e-11
M = 1 

v_tot = np.sqrt(G * M / r)    #velocity of orbit
vx0 = v_tot * (y0 / r)    #velocity in the x direction
vy0 = v_tot * (x0 / r)    #velocity in the y directon

t = 3    #total time to run simulation in years
delt = 0.05    #timestep 
n = t/delt    #total number of steps

#make animation
fig, ax = plt.subplots()

twobody, = ax.plot([], [])

def init():
    twobody.set_data([], [], [], [])
    return twobody


two_ani = FuncAnimation(fig, partial(twobody, x = x0, y = y0, vx = vx0, vy = vy0), save_count = int(t/delt), init_func = init)
two_ani.to_jshtml()
plt.show()