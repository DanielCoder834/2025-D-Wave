import dimod
import numpy as np
from dwave.system import LeapHybridQMSampler
import resources

cqm = dimod.ConstrainedQuadraticModel()

x = {i: dimod.Integer(f"x_{i}", lower_bound=0, upperbound=18)
     for i in range(n)}

objective = dimod.QuadraticModel()

alpha = 1
beta = 1
gamma = 1
for i in range(19):
    for j in range(19):
        if i != j:
            objective.add_quadratic(x[i], x[j],
                                    resources.flows[i, j] * resources.distances[x[i], x[j]] +
                                    )
