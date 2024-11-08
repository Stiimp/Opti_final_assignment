import pulp as p
import numpy as np
from pulp import lpSum, LpVariable, value

prob = p.LpProblem('Problem', p.LpMaximize)

items = range(7)
objective_coef = [6, 4, 6, 7, 5, 8, 8]
constraint_coef = [5, 6, 8, 6, 4, 6, 5]
constr = 21
#variable
selected = LpVariable.dicts("Selected", items, cat = "Binary")
#objective function
prob += lpSum(selected[i] * objective_coef[i] for i in items)
#constraint
prob += lpSum(selected[i] * constraint_coef[i] for i in items) <= constr

prob.solve()

print('Optima: ')
for i in items:
    if selected[i].value() == 1:
        print(f"Item {i +1} is selected")
print("Max value: ", value(prob.objective))


prob_relaxed = p.LpProblem('Problem_relaxed', p.LpMaximize)
#variable
selected_relaxed = LpVariable.dicts("Selected_relaxed", items, lowBound=0, upBound=1)
#objective
prob_relaxed += lpSum(selected_relaxed[i] * objective_coef[i] for i in items)
#constraint
prob_relaxed += lpSum(selected_relaxed[i] * constraint_coef[i] for i in items) <= constr

prob_relaxed.solve()

print('Optima: ')
for i in items:
    if selected_relaxed[i].value() > 0:
        print(f"Item {i +1} is selected with value: " + str(selected_relaxed[i].value()))
print("Max value: ", value(prob_relaxed.objective))


prob_separation = p.LpProblem('Problem_separation', p.LpMinimize)
#variable
selected_separation = LpVariable.dicts("Selected_separation", items, cat="Binary")
#objective
prob_separation += lpSum((1-selected_relaxed[j].value()) * selected_separation[j] for j in items)
#constraint
prob_separation += lpSum(selected_separation[j] * constraint_coef[j] for j in items) >= constr

prob_separation.solve()
for j in items:
    if selected_separation[j].value() > 0:
        print(f"Item {j + 1} is selected (separated), value: {selected_separation[j].value()}")
print("Max value: ", value(prob_separation.objective))

prob_cover = p.LpProblem('problem_cover', p.LpMaximize)
#vaiable
selected_cover = LpVariable.dicts("selected_cover", items, cat="Binary")
#objective
prob_cover += lpSum(objective_coef[j] * selected_cover[j] for j in items)
#constraint
prob_cover += lpSum(selected_cover[j] * constraint_coef[j] for j in items) <= constr
cover_set = [j for j in items if selected_separation[j].value() == 1]
prob_cover += lpSum(selected_cover[j] * selected_separation[j].value() for j in items) <= len(cover_set) - 1

prob_cover.solve()
print(cover_set)
for j in items:
    if selected_cover[j].value() > 0:
        print(f"Item {j + 1} is selected (cover), value: {selected_cover[j].value()}")
print("Max value: ", value(prob_cover.objective))
