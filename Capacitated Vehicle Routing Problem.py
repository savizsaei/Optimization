#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: saviz
"""

# Capacitated Vehicle Routing Problem

import math
import random
import numpy as np

numCustomers = 30
maxNumVehicles = 5
vehicleCapacity = 30
demandMin = 2
demandMax = 5

random.seed(0)

depot = 0
customers = [*range(1, numCustomers + 1)]
locations = [depot] + customers
connections = [(i, j) for i in locations for j in locations if i != j]
vehicles = [*range(1, maxNumVehicles + 1)]

# create random depot and customer locations in the Euclidian plane (1000x1000)
points = [(random.randint(0, 999), random.randint(0, 999)) for i in locations]
# dictionary of Euclidean distance between each pair of points (interpreted as travel costs)
costs = {
    (i, j): math.ceil(
        math.sqrt(sum((points[i][k] - points[j][k]) ** 2 for k in range(2)))
    )
    for i in locations
    for j in locations
    if i != j
}

# create random demands in range [demandMin,demandMax]
demands = {i: random.randint(demandMin, demandMax) for i in locations}
demands[0] = 0  # depot has no demand

### MODEL CONFIGURATION
vehicleIndexedRoutes = 0  # 0: no vehicle index, 1: vehicle-indexed route variables


import gurobipy as gp
from gurobipy import GRB

def numVehiclesNeededForCustomers(customers):
    sumDemand = 0
    for i in customers:
        sumDemand += demands[i]
    return math.ceil(sumDemand / vehicleCapacity)

# create model for Capacitated Vehicle Routing Problem instance
model = gp.Model("CVRP")

# binary variables x(i,j): is 1 if some vehicle is going from node i to node j, 0 otherwise
x = model.addVars(connections, vtype=GRB.BINARY, name="x")

# objective function: minimize sum of connection costs
model.setObjective(x.prod(costs), GRB.MINIMIZE)

# all customers have exactly one incoming and one outgoing connection
model.addConstrs((x.sum("*", j) == 1 for j in customers), name="incoming")
model.addConstrs((x.sum(i, "*") == 1 for i in customers), name="outgoing")

# vehicle limits
model.addConstr(x.sum(0, "*") <= maxNumVehicles, name="maxNumVehicles")
model.addConstr(
    x.sum(0, "*") >= numVehiclesNeededForCustomers(customers),
    name="minNumVehicles",
)

if vehicleIndexedRoutes == 1:
    # binary variables v(i,j,k): is 1 if vehicle k is going from node i to node j, 0 otherwise
    v = model.addVars(connections, vehicles, vtype=GRB.BINARY, name="v")

    # relation to vehicle-independent route variables
    model.addConstrs((v.sum(i, j, "*") == x[i,j] for (i,j) in connections), name="linking")

     # all customers have exactly one incoming and flow conservation has to hold for each vehicle
    model.addConstrs((v.sum("*", j, k) == v.sum(j, "*", k) for j in customers for k in vehicles), name="flowConservation")
    
    
    
model.params.Threads = 4
model.optimize()

usedConnections = [(i, j) for (i, j) in x.keys() if x[i, j].X > 0.5]

# create a dict for the next customer based on the current one 
# (note that the depot in general has multiple outgoing connections)
nextCustomer = {}
for (i, j) in usedConnections:
    if i == 0:
        if 0 not in nextCustomer.keys():
            nextCustomer[0] = []
        nextCustomer[0].append(j)
    else:
        nextCustomer[i] = j

print(f"Solution contains {len(nextCustomer[0])} routes:")
routeNumber = 0
visitedCustomers = [False] * (numCustomers + 1)
for firstCustomer in nextCustomer[0]:
    print(f"Route {routeNumber}: 0 -> ", end="")
    vehicleLoad = 0
    currentCustomer = firstCustomer
    while currentCustomer != 0:
        print(f"{currentCustomer} -> ", end="")
        visitedCustomers[currentCustomer] = True
        vehicleLoad += demands[currentCustomer]
        currentCustomer = nextCustomer[currentCustomer]
    print(f"0, load = {vehicleLoad} of {vehicleCapacity}")
    if vehicleLoad > vehicleCapacity:
        print("Vehicle capacity is exceeded!")
    routeNumber += 1

print("Unvisited customers: ", end="")
for c in customers:
    if visitedCustomers[c] == False:
        print(f"{c}, ", end="")
Y=np.array(visitedCustomers)
        
 # free resources
model.dispose()
gp.disposeDefaultEnv()

       
    