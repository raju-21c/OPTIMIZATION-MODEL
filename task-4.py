import pulp

# 1. Initialize the problem
model = pulp.LpProblem("Production_Maximization", pulp.LpMaximize)

# 2. Define the decision variables
# The variables are non-negative integers (number of products)
widgets = pulp.LpVariable('widgets', lowBound=0, cat='Integer')
gadgets = pulp.LpVariable('gadgets', lowBound=0, cat='Integer')

# 3. Define the objective function
# Maximize profit: 5 * widgets + 7 * gadgets
model += 5 * widgets + 7 * gadgets, "Total Profit"

# 4. Define the constraints
# Steel constraint: 1*widgets + 2*gadgets <= 10
model += 1 * widgets + 2 * gadgets <= 10, "Steel Constraint"

# Labor constraint: 2*widgets + 1*gadgets <= 8
model += 2 * widgets + 1 * gadgets <= 8, "Labor Constraint"

# 5. Solve the problem
model.solve()

# 6. Display the solution status and results
print("Status:", pulp.LpStatus[model.status])
print(f"Optimal number of widgets to produce: {widgets.varValue}")
print(f"Optimal number of gadgets to produce: {gadgets.varValue}")
print(f"Maximum total profit: ${model.objective.value()}")
