# import the required modules

import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

'''
we are going to solve the second order differential equation of a pendulum whcich is as follows ==>> {d^2theta/dt^2 + (B/m * dtheta/dt) + (g/l * sin(theta)) = 0 }
for solving these higher order differential equations , we will first break them down to 1st order ODEs. Here, this can be done by taking theta = theta1.
thus, ==>> dtheta / dt = dtheta1 / dt = theta2;
           d^2(theta)/dt^2 = d^2theta1/dt^2 = dtheta2/dt ;
thus the second order ODE now becomes ==>>> dtheta2/dt + (B/m * theta2) + (g/l * sin(theta1)) = 0
Hence we can break down the 2nd order ODE in to two first order ODEs =>>>>  dtheta1/dt = theta2
                                                                            dtheta2/dt = -(B/m * theta2) - (g/l * sin(theta1))
Take dtheta/dt = [ dtheta1/dt, dtheta2/dt]
We need to define a function which will return the array of dtheta/dt.
Then we can solve for theta by integrating dtheta/dt staring from theta_0 , between the two time limits.
This is done by using ===>>> odeint(function, theta_0, t, arg())
                             theta_0 is the value of theta at the lower limit of t.
                             t is the array of all the time points at which dtheta/dt will be calculated.
                             arg() is used to input all the left out arguments required for the function to work.
solution =  odeint(function, theta_0, t, arg())
solution is the array of theta[theta1,theta2] ==>>> in this case, theta1 is the displacement from mean position and theta2 is the velocity of the pendulum ball.
'''


def d0_dt(theta, t, b, m, g, l):

    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2
    dtheta2_dt = -(b/m * theta2) - (g/l * math.sin(theta1))
    dtheta_dt = [dtheta1_dt, dtheta2_dt]
    return dtheta_dt


theta_0 = [0, 3]
t = np.linspace(0, 20, 150)
b = 0.02
m = 0.1
g = 9.81
l = 3

solution = odeint(d0_dt, theta_0, t, args=(b, m, g, l))
# print(solution)

plt.plot(t, solution[:, 0], color='r', linestyle='-',
         linewidth=2, label=r'$ \frac{d\theta_1}{dt}$ = $\theta_2$')
plt.plot(t, solution[:, 1], color='b', linestyle='--', linewidth=1.5,
         label=r'$ \frac{d\theta_2}{dt}$ = $-\frac{b}{m}\theta_2 - \frac{g}{l}sin\theta_1 $')
plt.xlabel('time(s)')
plt.ylabel('plot')
plt.grid(True)
plt.title('pendulum plots')
plt.legend(loc='best')
plt.savefig('pendulum plots')
plt.show()


sol_dis = solution[:, 0]
# print(sol_dis)

count = 1
x0 = 0
y0 = 0
l = 3
for i in t:

    for s in sol_dis:
        pos_x = x0 + l*math.sin(math.radians(180) + s)
        pos_y = y0 + l*math.cos(math.radians(180) + s)

        filename = '%05d.png' % count
        count = count + 1
        plt.figure()
        plt.plot([-0.25, 0.25], [0, 0], linewidth=15)
        plt.plot(x0, y0, marker='*', markersize=10)
        plt.plot([x0, pos_x], [y0, pos_y], linestyle='--')
        plt.plot(pos_x, pos_y, 'o', markersize=25)
        plt.xlim([-4, 4])
        plt.ylim([-5, 1])
        plt.grid(True)
        plt.title('pendulum motion with damping')
        plt.savefig(filename)
