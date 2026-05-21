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
    
    # the alphas
    
    al = 1
    a0l = 1
    at = 1
    a0t = 1
    ac = 1
    a0c = 1
    
    # the betas
    
    bl = 1
    bt = 1
    bc = 1
    
    # ode assignments
    
    mlaci = x[0]
    mtetR = x[1]
    mci = x[2]
    
    placi = x[3]
    ptetR = x[4]
    pci = x[5]
    
    #=======================================================================
    # PICK UP HERE #
    #=======================================================================
    
    
    
    
### m is the mRNA for a given repressor
### a0 is the amount of protein (p) present in a cell when the repressor is saturated
### a + a0 is the amount of protein (p) present in a cell with absolutly no repressor

'''the elegance here is appreciated due to the simplicity: all the major aspects which affect mRNA
are represented in the ODE, and wonderfully illustrates the central dogma of biology'''

def mlacl(m,t,p,a0,a):
    dmdt = -m + (a/(1+p)) + a0
    return dmdt

def mtetR(m,t,p,n,a0,a):
    dmdt = -m + (a/(1+p**n)) + a0
    return dmdt

def mcl(m,t,p,a0,a):
    dmdt = -m + (a/(1+p)) + a0
    return dmdt

'''again the ODE is oddly satisfying: the change in protein is the inverse of protein 
amount minus the amount of mRNA eventually being translated to protein, then adjusted for
the ratio of decay of both the protein and the mRNA'''

def placl(p,t,m,b):
    dpdt = -b*(p-m)
    return dpdt

def ptetR(p,t,m,b):
    dpdt = -b*(p-m)
    return dpdt

def pcl(p,t,m,b):
    dpdt = -b*(p-m)
    return dpdt



plt.plot()
plt.xlabel("Time")
plt.ylabel("Cell number?")
plt.show()
