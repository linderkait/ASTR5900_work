import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['font.size'] = 14

#Problem 1
#Part a
#define a two body code to be animated
def twobody(frame):
    #A circular orbit is assumed.

    #get state of system
    x = state['x']
    y = state['y']
    vx = state['vx']
    vy = state['vy']

    #define radius
    r = np.sqrt(x**2 + y**2)

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
    vy += 0.5 * ay * delt

    #redefine the state of the system
    state['x'] = x
    state['y'] = y
    state['vx'] = vx
    state['vy'] = vy

    #define the path of the satellite
    path_x.append(x)
    path_y.append(y)

    #update plot
    line.set_data(path_x, path_y)
    point.set_data([x], [y])
    return line, point

def euler(frame):
    #A circular orbit is assumed.

    #get state of system
    x = state['x']
    y = state['y']
    vx = state['vx']
    vy = state['vy']

    #define radius
    r = np.sqrt(x**2 + y**2)

    #calculate acceleration
    a_tot = -G * M / r ** 2    #gravitational acceleration due to central object
    ax = a_tot * (x / r)    #acceleration in the x direction
    ay = a_tot * (y / r)    #acceleration in the y direction

    #use eulers method to find position and velocity
    x += delt * vx
    y += delt * vy
    
    vx += delt * ax
    vy += delt * ay


        #redefine the state of the system
    state['x'] = x
    state['y'] = y
    state['vx'] = vx
    state['vy'] = vy
    
    #define the path of the satellite
    path_x.append(x)
    path_y.append(y)

    #update plot
    line.set_data(path_x, path_y)
    point.set_data([x], [y])
    return line, point

#define initial values
x0 = 1
y0 = 0
r0 = np.sqrt(x0**2 + y0**2)

G = 4 * np.pi**2
M = 1 

v_tot = np.sqrt(G * M / r0)    #velocity of orbit
vx0 = v_tot * (y0 / r0)    #velocity in the x direction
vy0 = v_tot * (x0 / r0)    #velocity in the y directon

t = 3    #total time to run simulation in years
delt = 0.01    #timestep 
n = int(t/delt)    #total number of steps

#define the initial state of the system
state = {'x':x0, 'y':y0, 'vx':vx0, 'vy':vy0}
path_x = [x0]
path_y = [y0]

#setup animation
fig, ax = plt.subplots()
ax.set_xlim(-1.5*r0, 1.5*r0)
ax.set_ylim(-1.5*r0, 1.5*r0)
ax.set_aspect('equal')
ax.grid(True)
line, = ax.plot([], [], lw = 1)
point, = ax.plot([], [], 'o', ms = 10)

#animate twobody
two_ani = FuncAnimation(fig, twobody, frames = n, blit=False)

#save animation
two_ani.save('p1_twobody.mp4', writer = 'ffmpeg', fps=30, dpi=100)

#define initial values
x0 = 1
y0 = 0
r0 = np.sqrt(x0**2 + y0**2)

G = 4 * np.pi**2
M = 1 

v_tot = np.sqrt(G * M / r0)    #velocity of orbit
vx0 = v_tot * (y0 / r0)    #velocity in the x direction
vy0 = v_tot * (x0 / r0)    #velocity in the y directon

t = 9   #total time to run simulation in years
delt = 0.01    #timestep 
n = int(t/delt)    #total number of steps

#define the initial state of the system
state = {'x':x0, 'y':y0, 'vx':vx0, 'vy':vy0}
path_x = [x0]
path_y = [y0]

#setup animation
fig, ax = plt.subplots()
ax.set_xlim(-4*r0, 4*r0)
ax.set_ylim(-4*r0, 4*r0)
ax.set_aspect('equal')
ax.grid(True)
line, = ax.plot([], [], lw = 1)
point, = ax.plot([], [], 'o', ms = 10)

#animate euler
eul_ani = FuncAnimation(fig, euler, frames = n, blit=False)

#save animation
eul_ani.save('p1_euler.mp4', writer = 'ffmpeg', fps=30, dpi=100)
