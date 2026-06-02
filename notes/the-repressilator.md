# The Repressilator
The Repressilator is a gene network consisting of three sequences which are transcribed/translated into three proteins. Each protein represses the expression of another in this biological game of rock paper scissors, resulting in oscillations in protein and mRNA levels. You can read more about it here: https://www.nature.com/articles/35002125

I chose to model this gene regulated network (GRN) for three reasons: 
### 1. A real taste of synthetic biology. 
In this paper, not only was the system an actual synthetic gene circuit in *E. Coli* but it was also computationally modeled by a simplistic system of ODE's. This would give me a real yet accessible taste of synthetic biology. Knowing the model I've create can successfully simulate a real gene network is truly satisfying!
### 2. Ease of access.
The system is just that: a simple system of 6 (technically 2, repeated thrice) ODE's. I figured this would be relatively simple to implement with my basic python/calculus skills. Thankfully, Vincent Stevenson has a wonderfully concise tutorial on using pyplot, scipy, and numpy in combination to solve systems of ODE's. Without it, hours of reading through documentation would have surely been spent. Link to Vincent's video is here: https://youtu.be/MXUMJMrX2Gw
### 3.  Real modeling. 
ODE systems are, and have been used as, viable methods in computational biology. By completing this project, I've gained a significantly clearer understanding of the computational technicalities involved in modeling biological systems. Without a doubt, this project has taught me more about systems biology and computational modeling than any crash course could. Additionally, I'm guessing I can still expand upon this model, and gain further understanding by adding additional ODE's, or simulating other simple perturbances, like transcriptional stressors, or perhaps a fourth player in the synthetic gene circuit. 

That leaves us with one direction: *Forward!* In the next few commits, I plan on expanding upon the my current model to include hypothetical genes/perturbances, and model their impact on the Repressilator's behavior. Ambitiously, I'd also like to try and describe the new system's steady state, the same way Michael B. Elowitz & Stanislas Leibler do in the Repressilator paper.
