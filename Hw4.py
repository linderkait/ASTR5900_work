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
two_ani = FuncAnimation(fig, twobodyani, frames = n, blit=False)

#save animation
two_ani.save('p2_twobody.mp4', writer = 'ffmpeg', fps=30, dpi=100)

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
    speed = np.array([np.sqrt(vx**2 + vy**2)])    #the total speed of the object

    r = np.sqrt(x**2 + y**2)
    E = np.array([1/2 * speed ** 2 - G * M / r])    #the total specific energy

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
    speed = np.array([np.sqrt(vx**2 + vy**2)])    #the total speed of the system

    r = np.sqrt(x**2 + y**2)

    E = np.array([1/2 * speed ** 2 - G * M / r])    #the total specific energy

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

#plot the functions
plt.plot(t_arr, v_two, label='twobody')
plt.plot(t_arr, v_eul, label='euler')
plt.xlabel("time (yr)")
plt.ylabel('speed (AU/yr)')
plt.legend()
plt.show()

plt.plot(t_arr, E_two, label='twobody')
plt.plot(t_arr, E_eul, label='euler')
plt.xlabel("time (yr)")
plt.ylabel('Energy (AU^2/yr^2)')
plt.legend()
plt.show()

#Problem 2b

#define initial values

v_tot = 0.8 * np.sqrt(G * M / r0)    #velocity of orbit
vx0 = v_tot * (y0 / r0)    #velocity in the x direction
vy0 = v_tot * (x0 / r0)    #velocity in the y directon

t = 4    #total time to run simulation in years
delt = 0.01    #timestep 
t_arr = np.arange(0, 4.01, 0.01)

v_twob, E_twob = twobody(x0, y0, vx0, vy0, t, delt)
v_eulb, E_eulb = euler(x0, y0, vx0, vy0, t, delt)

#plot the functions
plt.plot(t_arr, E_twob, label='twobody')
plt.xlabel("time (yr)")
plt.ylabel('Energy (AU^2/yr^2)')
plt.legend()
plt.show()

plt.plot(t_arr, E_eulb, label='euler')
plt.xlabel("time (yr)")
plt.ylabel('Energy (AU^2/yr^2)')
plt.legend()
plt.show()



#Problem 3
def twobodyanijup(frame):
    #A circular orbit is assumed

    #get state of system
    x = state['x']
    y = state['y']
    vx = state['vx']
    vy = state['vy']
    xj = state['xj']    #j indicates values for jupyter
    yj = state['yj']
    vxj = state['vxj']
    vyj = state['vyj']
    t_current = state['t_current'] 
    v_current = state['v_current']

    #define radius
    r = np.sqrt(x**2 + y**2)
    rj = np.sqrt(xj**2 + yj**2)
    rjs = np.sqrt((xj-x)**2 + (yj-y)**2)    #js indicates jupyer in relation to the spacecraft

    #calculate acceleration
    aj_tot = -G * M / rj ** 2 
    axj = aj_tot * (xj / rj)
    ayj = aj_tot * (yj / rj)
    a_tot = -G * M / r ** 2
    ajs_tot =  -G * Mj / rjs ** 2
    ax = a_tot * (x / r) + ajs_tot * ((x-xj) / rjs)
    ay = a_tot * (y / r) + ajs_tot * ((y-yj) / rjs)


    #Calculate the velocity half step
    vx += 0.5 * ax * delt
    vy += 0.5 * ay * delt
    vxj += 0.5 * axj * delt
    vyj += 0.5 * ayj * delt

    #calculate the position full step
    x += vx * delt
    y += vy * delt
    xj += vxj * delt
    yj += vyj * delt

    #recalculate values
    r = np.sqrt(x**2 + y**2) 
    rj = np.sqrt(xj**2 + yj**2)
    rjs = np.sqrt((xj-x)**2 + (yj-y)**2)

    aj_tot = -G * M / rj ** 2 
    axj = aj_tot * (xj / rj)
    ayj = aj_tot * (yj / rj)
    a_tot = -G * M / r ** 2
    ajs_tot =  -G * Mj / rjs ** 2
    ax = a_tot * (x / r) + ajs_tot * ((x-xj) / rjs)
    ay = a_tot * (y / r) + ajs_tot * ((y-yj) / rjs)


    #calculate the velocity full step
    vx += 0.5 * ax * delt
    vy += 0.5 * ay * delt
    vxj += 0.5 * axj * delt
    vyj += 0.5 * ayj * delt

    #add time and velocity information
    t_current += delt * 12    #time in months
    v_current = np.sqrt(vx**2 + vy**2) * 4.743    #velocity in km/s

    #redefine the state of the system
    state['x'] = x
    state['y'] = y
    state['vx'] = vx
    state['vy'] = vy
    state['xj'] = xj
    state['yj'] = yj
    state['vxj'] = vxj
    state['vyj'] = vyj
    state['t_current'] = t_current
    state['t_current'] = t_current

    #define the path of the satellite
    path_x.append(x)
    path_y.append(y)

    #update plot
    title.set_text(f'Time: {t_current:.2g} months, Velocity: {v_current:.3g} km/s')
    line.set_data(path_x, path_y)
    point.set_data([x], [y])
    jupiter.set_data([xj], [yj])
    return line, point, jupiter, title

#define initial values
x0 = 1
y0 = 0
r0 = np.sqrt(x0**2 + y0**2)

#determine initial position for jupyter
rj0 = 5.2
xj0 = rj0 * np.cos(np.deg2rad(97.5))
yj0 = rj0 * np.sin(np.deg2rad(97.5))

G = 4 * np.pi**2
M = 1 
Mj = .001

v_tot = np.sqrt(G * M / r0) + 11.2/4.743  #add earths escape velocity to total probe velocity    
vx0 = v_tot * (y0 / r0)    
vy0 = v_tot * (x0 / r0)    
vj_tot = np.sqrt(G * M / rj0)    
vxj0 = -vj_tot * (yj0 / rj0)    
vyj0 = vj_tot * (xj0 / rj0)    

t = 3   #total time to run simulation in years
delt = 0.01    #timestep 
n = int(t/delt)    #total number of steps
t0 = 0

#define the initial state of the system
state = {'x':x0, 'y':y0, 'vx':vx0, 'vy':vy0, 'xj':xj0, 'yj':yj0, 'vxj':vxj0, 'vyj':vyj0, 't_current':t0, 'v_current':4.743}
path_x = [x0]
path_y = [y0]

#setup animation
fig, ax = plt.subplots()
ax.set_xlim(-6*r0, 6*r0)
ax.set_ylim(-6*r0, 6*r0)
ax.set_aspect('equal')
ax.grid(True)
title = ax.set_title(f'Time: {0} months, Velocity: {4.743} km/s')
line, = ax.plot([], [], lw = 1)
point, = ax.plot([], [], 'o', ms = 10, label = 'Voyager 2')
jupiter, = ax.plot([], [], 'o', ms = 10, label = 'Jupiter')
ax.legend()

#animate twobody
two_ani = FuncAnimation(fig, twobodyanijup, frames = n, blit=False)

#save animation
two_ani.save('p3_twobody.mp4', writer = 'ffmpeg', fps=30, dpi=100)


#part b
def twobodyjup(x, y, vx, vy, xj, yj, vxj, vyj, t, delt):
    #A circular orbit is assumed

    v_current = np.array([np.sqrt(vx**2 + vy**2) * 4.743])
    rjup = np.array([np.sqrt((xj-x)**2 + (yj-y)**2)])    #the distance to jupiter

    n = int(t/delt)

    for i in range(n):
        #define radius
        r = np.sqrt(x**2 + y**2)
        rj = np.sqrt(xj**2 + yj**2)
        rjs = np.sqrt((xj-x)**2 + (yj-y)**2)    #js indicates jupyer in relation to the spacecraft

        #calculate acceleration
        aj_tot = -G * M / rj ** 2 
        axj = aj_tot * (xj / rj)
        ayj = aj_tot * (yj / rj)
        a_tot = -G * M / r ** 2
        ajs_tot =  -G * Mj / rjs ** 2
        ax = a_tot * (x / r) + ajs_tot * ((x-xj) / rjs)
        ay = a_tot * (y / r) + ajs_tot * ((y-yj) / rjs)


        #Calculate the velocity half step
        vx += 0.5 * ax * delt
        vy += 0.5 * ay * delt
        vxj += 0.5 * axj * delt
        vyj += 0.5 * ayj * delt

        #calculate the position full step
        x += vx * delt
        y += vy * delt
        xj += vxj * delt
        yj += vyj * delt

        #recalculate values
        r = np.sqrt(x**2 + y**2) 
        rj = np.sqrt(xj**2 + yj**2)
        rjs = np.sqrt((xj-x)**2 + (yj-y)**2)

        aj_tot = -G * M / rj ** 2 
        axj = aj_tot * (xj / rj)
        ayj = aj_tot * (yj / rj)
        a_tot = -G * M / r ** 2
        ajs_tot =  -G * Mj / rjs ** 2
        ax = a_tot * (x / r) + ajs_tot * ((x-xj) / rjs)
        ay = a_tot * (y / r) + ajs_tot * ((y-yj) / rjs)


        #calculate the velocity full step
        vx += 0.5 * ax * delt
        vy += 0.5 * ay * delt
        vxj += 0.5 * axj * delt
        vyj += 0.5 * ayj * delt

        #add time and velocity information
        v_current = np.append(v_current, np.sqrt(vx**2 + vy**2) * 4.743)    #velocity in km/s
        rjup = np.append(rjup, np.sqrt((xj-x)**2 + (yj-y)**2))
    return v_current, rjup

#define initial values
x0 = 1
y0 = 0
r0 = np.sqrt(x0**2 + y0**2)

rj0 = 5.2
xj0 = rj0 * np.cos(np.deg2rad(97.5))
yj0 = rj0 * np.sin(np.deg2rad(97.5))

G = 4 * np.pi**2
M = 1 
Mj = .001

v_tot = np.sqrt(G * M / r0) + 11.2/4.743 
vx0 = v_tot * (y0 / r0)    
vy0 = v_tot * (x0 / r0)    
vj_tot = np.sqrt(G * M / rj0)    
vxj0 = -vj_tot * (yj0 / rj0)    
vyj0 = vj_tot * (xj0 / rj0)    

t = 3
delt = 0.01

t_arr = np.arange(0, 3.01, 0.01)

#run function
speed, rjup = twobodyjup(x0, y0, vx0, vy0, xj0, yj0, vxj0, vyj0, t, delt)

#plot the speed vs time
plt.plot(t_arr, speed)
plt.xlabel('time (yr)')
plt.ylabel('speed (km/s)')
plt.show()


#find closest distance and time
r_close = np.min(rjup)
t_close = t_arr[np.argmin(rjup)]

print(f'The closest distance to jupiter was {r_close:.3g} AU and it occured at {t_close:.3g} years after launch')