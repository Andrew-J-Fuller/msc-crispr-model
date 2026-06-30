import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import pandas as pd
import json


# about this network:
# Gene names = strings
# alphas, betas and naughts are numbers
# targets are a list of dictionaries with the key being the target and the pair being a list of interactions (repress, activate, etc.)

network = pd.read_csv("gene list.csv") 

# defining the gene as a class, this will include both the protein and the mRNA.
class gene:
    def __init__(self, name):
        self.name = name
        self.targets = []
        self.alpha = None
        self.beta = None
        self.naught = None
        self.mRNA = None
        self.protein = None

genlst = [] # the list of genes(classes) in the network

# the genes (classes) are now assigned their attributes from the csv
for index, row in network.iterrows():
    g = gene(row["gene name"])
    g.alpha = row["alpha"]
    g.beta = row["beta"]
    g.naught = row["naught"]
    g.targets = json.loads(row["targets"]) # a list of dictionaires where the key is the target of the gene, and the value is the type of effect it has on the target
    genlst.append(g)

# defining the repression regulation
# returns a number
def scrip_repress(target, gene, hill):
    change = (target.alpha/(1+gene.protein**hill)+target.naught)
    return change

# creates a list of regulators for a defined gene
def regulators(gene):
    regs = [] # a list of genes(class) which interact with gene
    for g in genlst:
        for d in g.targets:
            if gene.name in d:
                regs.append(g)
    return regs

# defining mRNA dynamics (doesn't work on its own because init conds haven't been set yet)
# returns a number
def transcription(gene):
    change = -gene.mRNA
    for reg in regulators(gene): #this loops the list of genes
        for d in reg.targets: #this loops the list of dictionaries in the gene.target
            if "rep" in d.values():
                change += scrip_repress(gene, reg, 2)
                break
    return change

# definging protein dynamics...returns a number
def translation(gene):
    change = -gene.beta*(gene.protein - gene.mRNA)
    return change

# repressilator func that gets added to odeint
def repressilator(x,t):

    ### assings initial conditions
    rna = x[:len(genlst)] #cuts the init conds in half
    prot = x[len(genlst):] #^^^^^^^
    for gen, mRNA, protein in zip(genlst, rna, prot):
        gen.mRNA = mRNA
        gen.protein = protein
    ### assings initial conditions

    ### assings the ode changes according to the transcription and translation
    changes = []
    for gen in genlst:
        changes.append(transcription(gen))
    for gen in genlst:
        changes.append(translation(gen))
    return changes

# adding initial conditions
x0 = [0,100,200,0,0,0]
t = np.linspace(0,200,10000)

# plotting the repressilator using odeint
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
