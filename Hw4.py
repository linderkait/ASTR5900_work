import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams['font.size'] = 14

#Problem 1
#Part a
#define a two body code to be animated
def twobodyani(frame):
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

def eulerani(frame):
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

v_tot = 0.8 * np.sqrt(G * M / r0)    #velocity of orbit
vx0 = v_tot * (y0 / r0)    #velocity in the x direction
vy0 = v_tot * (x0 / r0)    #velocity in the y directon

t = 4    #total time to run simulation in years
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
#two_ani = FuncAnimation(fig, twobodyani, frames = n, blit=False)

#save animation
#two_ani.save('p2_twobody.mp4', writer = 'ffmpeg', fps=30, dpi=100)

#define initial values
x0 = 1
y0 = 0
r0 = np.sqrt(x0**2 + y0**2)

G = 4 * np.pi**2
M = 1 

v_tot = 0.8 * np.sqrt(G * M / r0)    #velocity of orbit
vx0 = v_tot * (y0 / r0)    #velocity in the x direction
vy0 = v_tot * (x0 / r0)    #velocity in the y directon

t = 8  #total time to run simulation in years
delt = 0.001    #timestep 
n = int(t/delt)    #total number of steps

#define the initial state of the system
state = {'x':x0, 'y':y0, 'vx':vx0, 'vy':vy0}
path_x = [x0]
path_y = [y0]

#setup animation
fig, ax = plt.subplots()
ax.set_xlim(-2*r0, 2.5*r0)
ax.set_ylim(-2*r0, 2*r0)
ax.set_aspect('equal')
ax.grid(True)
line, = ax.plot([], [], lw = 1)
point, = ax.plot([], [], 'o', ms = 10)

#animate euler
eul_ani = FuncAnimation(fig, eulerani, frames = n, blit=False)

#save animation
eul_ani.save('p2_euler.mp4', writer = 'ffmpeg', fps=300, dpi=100)



#Part b and c
def twobody(x, y, vx, vy, t, delt):
    #where x and y are the initial positions and vx and vy are initial velocities. t is the
    #total time to integrate over and delt is the step size
    speed = np.array([np.sqrt(vx**2 + vy**2)])

    r = np.sqrt(x**2 + y**2)
    E = np.array([1/2 * speed ** 2 - G * M / r])

    n = int(t/delt)

    for i in range(n):
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

        vtot = np.sqrt(vx**2 + vy**2)
        #calculate speed and energy
        speed = np.append(speed, vtot)
        E = np.append(E, 1/2 * vtot ** 2 - G * M / r)
    return speed, E

def euler(x, y, vx, vy, t, delt):
    #where x and y are the initial positions and vx and vy are initial velocities. t is the
    #total time to integrate over and delt is the step size
    speed = np.array([np.sqrt(vx**2 + vy**2)])

    r = np.sqrt(x**2 + y**2)

    E = np.array([1/2 * speed ** 2 - G * M / r])

    n = int(t/delt)

    for i in range(n):
        #calculate acceleration
        a_tot = -G * M / r ** 2    #gravitational acceleration due to central object
        ax = a_tot * (x / r)    #acceleration in the x direction
        ay = a_tot * (y / r)    #acceleration in the y direction

        #use eulers method to find position and velocity
        x += delt * vx
        y += delt * vy
    
        vx += delt * ax
        vy += delt * ay
        vtot = np.sqrt(vx**2 + vy**2)

        #calculate speed and energy
        speed = np.append(speed, vtot)
        E = np.append(E, 1/2 * vtot ** 2 - G * M / r)

        #recalculate radius
        r = np.sqrt(x**2 + y**2)
    return speed, E

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

v_two, E_two = twobody(x0, y0, vx0, vy0, t, delt)
v_eul, E_eul = euler(x0, y0, vx0, vy0, t, delt)
t_arr = np.arange(0, 3.01, 0.01)

#plt.plot(t_arr, v_two, label='twobody')
#plt.plot(t_arr, v_eul, label='euler')
#plt.xlabel("time (yr)")
#plt.ylabel('speed (AU/yr)')
#plt.legend()
#plt.show()

#plt.plot(t_arr, E_two, label='twobody')
#plt.plot(t_arr, E_eul, label='euler')
#plt.xlabel("time (yr)")
#plt.ylabel('Energy (AU^2/yr^2)')
#plt.legend()
#plt.show()

#Problem 2b

#define initial values

v_tot = 0.8 * np.sqrt(G * M / r0)    #velocity of orbit
vx0 = v_tot * (y0 / r0)    #velocity in the x direction
vy0 = v_tot * (x0 / r0)    #velocity in the y directon

t = 4    #total time to run simulation in years
delt = 0.01    #timestep 

v_twob, E_twob = twobody(x0, y0, vx0, vy0, t, delt)
v_eulb, E_eulb = euler(x0, y0, vx0, vy0, t, delt)

#plt.plot(t_arr, E_twob, label='twobody')
#plt.xlabel("time (yr)")
#plt.ylabel('Energy (AU^2/yr^2)')
#plt.legend()
#plt.show()

#plt.plot(t_arr, E_eulb, label='euler')
#plt.xlabel("time (yr)")
#plt.ylabel('Energy (AU^2/yr^2)')
#plt.legend()
#plt.show()
