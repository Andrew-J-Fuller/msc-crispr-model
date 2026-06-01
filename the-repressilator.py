# -*- coding: utf-8 -*-

# References
### A Synthetic Oscillatory Network of Transcriptional Regulators
#### https://www.nature.com/articles/35002125
### Vincent Stevenson's 'How to solve coupled ODEs in Python'
#### https://youtu.be/MXUMJMrX2Gw

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

## this is literally the time span, it's a list
t_span = (0,20)
periods = np.linspace(0,20,100)

def repressilator(x,t):
    
    #from the paper: "LacI inhibits expression of tetR, which 
    #in turn inhibits transcription of cI, which in turn inhibits expression of LacI
    
    # the alphas (the amount of protein in saturating amounts of repressor = a0, and in complete absence a + a0)
    
    al = 216
    a0l = 0.216
    at = 216
    a0t = 0.216
    ac = 216
    a0c = 0.216
    
    # the betas (b = rate of protein decay : rate of mRNA decay)
    
    bl = 0.2
    bt = 0.2
    bc = 0.2
    
    # Hill coefficient
    
    n = 2
    
    # ode assignments
    
    ### m is the mRNA for a given repressor
    ### a0 is the amount of protein (p) present in a cell when the repressor is saturated
    ### a + a0 is the amount of protein (p) present in a cell with absolutly no repressor
    
  
    mlaci = x[0]
    mtetR = x[1]
    mci = x[2]
    
    placi = x[3]
    ptetR = x[4]
    pci = x[5]
    
    '''all the major aspects which affect mRNA are represented in the ODE, and wonderfully illustrates the central dogma of biology'''
    
    dmldt = -mlaci + (al/(1+pci**n)) + a0l
    dmtdt = -mtetR + (at/(1+placi**n)) + a0t
    dmcdt = -mci + (ac/(1+ptetR**n)) + a0c
    
    '''again the ODE is oddly satisfying: the change in protein is the inverse of protein 
    amount minus the amount of mRNA eventually being translated to protein, then adjusted for
    the ratio of decay of both the protein and the mRNA'''
    
    dpldt = -bl*(placi-mlaci)
    dptdt = -bt*(ptetR-mtetR)
    dpcdt = -bc*(pci-mci)
    
    return [dmldt,dmtdt,dmcdt,dpldt,dptdt,dpcdt]

# initial conditions]

x0 = [0,100,200,0,0,0]
t = np.linspace(0,200,10000)

# let'er rip!

x = odeint(repressilator, x0, t)

mL = x[:,0]
mT = x[:,1]
mC = x[:,2]
pL = x[:,3]
pT = x[:,4]
pC = x[:,5]

plt.plot(t,mL)
plt.plot(t,mT)
plt.plot(t,mC)
plt.plot(t,pL)
plt.plot(t,pT)
plt.plot(t,pC)
#plt.ylim(0,500)
plt.show()
