from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def returns_dydt(y,t):
    dydt = -y * t + 13
    return dydt
y0 = 0
# values of time - from 0 to 5.
t = np.linspace(0,5,10)
# solving ODE
y_result = odeint(returns_dydt, y0, t)
plt.plot(t,y_result)
plt.xlabel("Time")
plt.ylabel("Y")
plt.show()
