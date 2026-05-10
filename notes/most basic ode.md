*for learning, I've created the most simplistic ODE I can, a growth function using numpy, scipy and matplotlib. I imagine more python majicks will be required for more complex modeling, but for now this note serves as a launching point I may refer back to both serve my memory and to appreciate how simple it can get*

'#' is for comments
```
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
```
this imports numpy, scipy and matplotlib.pyplot for use later

()'s are lists, so t_span is a list of 0 and 20 and t_eval linspace (so its a numberline, with 100 points between 0 and 20)
```
t_span = (0,20)
periods = np.linspace(0,20,100)
```

x0 needs to be in brackets since scipy's solve_ivp needs a 1 dimensional array (isn't that just a list?) in order to evaluate
```
x0 = [10]
r = 0.5
t_final = 20
```

This is the func that solve_ivp needs to evaluate
```
def growth(t, x):
    r = 0.5
    dxdt = r * x
    return dxdt
```

 not sure why we need to explicitly set t_eval? I though it would be implied by the order of the arguments but I suppose no
```
sol = solve_ivp(growth, t_span, x0,  t_eval=periods)
```

This next block sets the plotting. Much like the glorious ggplot we all know and love
```
plt.plot(sol.t, sol.y[0])
plt.xlabel("Time")
plt.ylabel("Cell number?")
plt.show()
```


# This results in:
<img width="815" height="532" alt="image" src="https://github.com/user-attachments/assets/e1bac7da-f3d9-4abd-bdb6-d8a4204019e3" />
