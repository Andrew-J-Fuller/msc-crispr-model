
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt



# ()'s are lists, so t_span is a list of 0 and 20 and t_eval linspace (so its a numberline, with 100 points between 0 and 20)

t_span = (0,20)
periods = np.linspace(0,20,100)

# x0 needs to be in brackets since scipy's solve_ivp needs a 1 dimensional array (isn't that just a list?) in order to evaluate

x0 = [10]
r = 0.5
t_final = 20


# This is the func that solve_ivp needs to evaluate

def growth(t, x):
    r = 0.5
    dxdt = r * x
    return dxdt

# not sure why we need to explicitly set t_eval? I though it would be implied by the order of the arguments but I suppose no

sol = solve_ivp(growth, t_span, x0,  t_eval=periods)


# This next block sets the plotting. Much like the glorious ggplot we all know and love

plt.plot(sol.t, sol.y[0])
plt.xlabel("Time")
plt.ylabel("Cell number?")
plt.show()
