from dwave.system import LeapHybridNLSampler
from dwave.optimization.model import Model
import numpy as np
import resources

# Step 1: Define the flow rate and distance matrices
# Example for 4 rooms and 4 locations
distance_matrix = resources.distances  # Example flow rate between rooms

flow_matrix = resources.flows # Example distance between locations

# Step 2: Initialize the model
model = Model()

# Step 3: Define constants
cost_per_day = 10  # Example constant cost per day
cost = model.constant(cost_per_day)
distances = model.constant(distance_matrix)
flows = model.constant(flow_matrix)

# Step 4: Add decision variables (rooms assigned to locations)
num_rooms = len(flow_matrix)
route = model.list(num_rooms)  # The route represents the permutation of rooms

# Step 5: Define the nonlinear objective
# Minimize the cost, considering the flow rate and distance between rooms
# Cost function: sum(cost * distances[route[i], route[j]] * flows[i, j])
# where route[i] is the room placed at location i, and route[j] is the room placed at location j.
ixs = model.constant(list(range(num_rooms)))
jxs = model.constant(list(range(num_rooms)))
alpha = model.constant(0.1)
beta = model.constant(0.1)
gamma = model.constant(0.1)

model.minimize(
    ((alpha * flows[ixs, jxs] * flows[ixs, jxs] + beta * distances[route[ixs], route[jxs]]) * (distances[route[ixs], route[jxs]] * flows[ixs, jxs]).sum()).sum()
)

sampler = LeapHybridNLSampler()
results = sampler.sample(model, time_limit=30, label="Optimal Room Assignment Problem")

# Step 6: Solve the model using D-Wave's sampler
sampler = LeapHybridNLSampler()

# Create the EmbeddingComposite to find an embedding onto the hardware
results = sampler.sample(model, label="hi")

results = sampler.sample(model, label="bye")

route, = model.iter_decisions()
print(route.state(0))
