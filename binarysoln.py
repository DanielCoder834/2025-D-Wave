from dimod import ConstrainedQuadraticModel, Integer
from dwave.system import LeapHybridCQMSampler
import resources

# Define problem size (example: 3 facilities, 3 locations)
n = 3

# Define integer assignment variables
x = [[Integer(f"x_{i}_{j}", lower_bound=0, upper_bound=1) for j in range(n)] for i in range(n)]

# Create CQM model
cqm = ConstrainedQuadraticModel()

# Add assignment constraints: each facility is assigned to exactly one location
for i in range(n):
    cqm.add_constraint(sum(x[i][j] for j in range(n)) == 1, label=f"facility_{i}")

# Add location constraints: each location gets exactly one facility
for j in range(n):
    cqm.add_constraint(sum(x[i][j] for i in range(n)) == 1, label=f"location_{j}")

# Define an example quadratic cost function
distances = resources.distances  # Example distances
flows = resources.flows    # Example flows

# Quadratic objective function
objective = sum(distances[i][j] * flows[k][l] * x[i][k] * x[j][l] 
                for i in range(n) for j in range(n) for k in range(n) for l in range(n))

cqm.set_objective(objective)

# Solve using D-Wave's hybrid CQM solver
sampler = LeapHybridCQMSampler()
result = sampler.sample_cqm(cqm)

# Extract and print best solution
best_solution = result.first.sample
print(best_solution)
