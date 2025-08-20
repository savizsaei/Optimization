#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 22:12:50 2025

@author: saviz
"""

# Binary Knapsack Problem using IBM CPLEX with docplex

from docplex.mp.model import Model

# Item weights and values
weights = [14, 25, 19, 14, 19, 11, 18, 15]
values =  [15, 10, 18, 11,  7,  2,  8,  9]
capacity = 30
num_items = len(weights)

# Create model
model = Model(name="Binary_Knapsack_Problem")

# Decision variables: x[i] = 1 if item i is selected, 0 otherwise
x = model.binary_var_list(num_items, name="x")

# Add capacity constraint
model.add_constraint(
    sum(weights[i] * x[i] for i in range(num_items)) <= capacity,
    ctname="Weight_Capacity"
)

# Define the objective: maximize total value
model.maximize(
    sum(values[i] * x[i] for i in range(num_items))
)

# Print model info
model.print_information()

# Solve the model
solution = model.solve()

# Display the solution
if solution:
    print("\n=== Optimal Solution Found ===")
    print("Selected items:")
    for i in range(num_items):
        if x[i].solution_value > 0.5:
            print(f"Item {i+1}: Weight = {weights[i]}, Value = {values[i]}")
    print(f"\nTotal Value: {model.objective_value}")
    print(f"Total Weight: {sum(weights[i] for i in range(num_items) if x[i].solution_value > 0.5)}")
else:
    print("No feasible solution found (Infeasible)")
