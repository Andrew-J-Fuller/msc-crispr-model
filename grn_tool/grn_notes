# A Gene Regulated Network Tool
Writing each gene a complex and individually tailored ODE which describes a large network of interactions is impractical. Therefore I'll need to create a system/tool to create larger more complex networks through abstraction, while maintaining a level of specificity needed for acurate genetic modeling.

## Goals
- works with odeint to solve for a graph of gene/protein concentrations
- avoids hardcoding each gene's interactions
- able to model a dozen genes (or more!)
- allow for multiple interaction types (not just repression)

## First thoughts
I'm modeling the concentrations of mRNA and protein in a large netowrk. Therefore, the output will always be a conentration (number). 

So to abstract what that concentration is for every gene/protein, I can say

	concentration = activation - deactivation - decay...(etc)
  
This way, I can relate the output to a number of interactions. I'll define each interaction...*once* and each gene will be assigned a combination of interactions/targets. The mathematical ODE will then be generated automatically.

This method might lack specificity however. I may wish to model gene X and gene Y as both activators of gene Z, but with differing strengths. Then, I would have to define "activate" and potentially "super activate" or some alternative. I'm hoping I can rely on gene specific constants (perhaps assigned with each gene's interactions/targets) as a solution at first. But I imagine I'll want to use different ODE's for similar behaviors later. 
