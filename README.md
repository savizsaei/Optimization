# Optimization

📊 Optimization & Scheduling Problems

This repository contains Python scripts and Jupyter notebooks that demonstrate the implementation of classical optimization problems using techniques such as linear programming, branch and bound, and decomposition methods. The collection is intended for students, researchers, and practitioners who want to understand and experiment with optimization models in Python.

📂 Repository Contents
1. Scheduling

File: Scheduling.ipynb

Description: Demonstrates scheduling problem formulations and solution methods. Includes model setup, constraints, and optimization for resource allocation over time.

2. Lot Sizing Problem

File: LotSizingProblem.py

Description: Implements the classic lot-sizing model for production planning. Focuses on cost minimization under constraints such as demand satisfaction, setup costs, and inventory holding.

3. Capacitated Facility Location Problem (CFLP)

File: Capacitatd_Facility_Location_Problem_for_Lagrangian_Decomposition.py

Description: Solves the CFLP using Lagrangian Decomposition, a relaxation technique to handle capacity and assignment constraints efficiently.

4. Branch and Bound

File: BranchAndBound.ipynb

Description: Illustrates the Branch and Bound algorithm for solving integer programming problems. Provides a step-by-step demonstration with visual explanations.

5. Knapsack Problem

File: knapsack.py

Description: Implements the 0-1 Knapsack Problem, a fundamental combinatorial optimization problem. Explores brute-force, greedy, and dynamic programming approaches.

🚀 Getting Started
Requirements

Python 3.8+

Common libraries:

pip install numpy pandas matplotlib pulp gurobipy


(Some scripts may require commercial solvers like Gurobi; others use open-source solvers such as PuLP.)

Running the Code

For Python scripts:

python LotSizingProblem.py


For Jupyter notebooks:

jupyter notebook Scheduling.ipynb

🎯 Learning Objectives

By working through this repository, you will:

Understand the formulation of classical optimization problems.

Learn how to implement models in Python with mathematical programming solvers.

Explore exact methods (Branch & Bound) and approximation/relaxation techniques (Lagrangian Decomposition).

Build intuition on when to use different methods depending on problem structure.

📌 Applications

These optimization problems are foundational in:

Supply Chain & Logistics

Manufacturing & Production Planning

Resource Allocation & Scheduling

Operations Research & Decision Sciences

📜 License

This repository is provided for educational and research purposes.
