import pulp as p
import numpy as np
from pulp import lpSum, LpVariable, value

prob = p.LpProblem('Problem', p.LpMaximize)

items = range(5)
#variable
selected = LpVariable.dicts("Selected", items, cat = "Binary")
#objective function
prob += lpSum(selected[i] * [6, 4, 6, 7, 5, 8, 8][i] for i in items)
#constraint
prob += lpSum(selected[i] * [5, 6, 8, 6, 4, 6, 5][i] for i in items) <= 21

prob.solve()

print('Optima: ')
for i in items:
    if selected[i].value() == 1:
        print(f"Item {i +1} is selected")
print("Max value: ", value(prob.objective))