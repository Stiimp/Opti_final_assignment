
import numpy as np

from assignment_4 import cheapest, capacity_req


def read_input(text_file):
    inp_mat = list()
    with open(text_file, 'r') as reader:
        for line in reader:
            line = line.rstrip('\n')
            a = line.split()
            for i in range(len(a)):
                a[i] = int(a[i])
            inp_mat.append(a)
    return inp_mat

inp = read_input('GAP_1.txt')
print("Raw input: " + str(inp))



m = int(inp[0][0])
n = int(inp[0][1])
costs = list()
capacity_req = list()
capacity_mac = inp[len(inp)-1]
for i in range(m):
    costs.append(inp[i+1])
    capacity_req.append(inp[i+m+1])
print("Number of machines: " + str(m))
print("Number of jobs: " + str(n))
print("Costs of assigning machines: " + str(costs))
print("Capacity required to use machine: " + str(capacity_req))
print("Capacity of the machines: " + str(capacity_mac))

res = []
for i in range(m):
    for j in range(m):
        for k in range(m):
            for l in range(m):
                for v in range(m):
                    res.append((i, j, k, l, v))

print("All possible combinations: " + str(res))

#filter the ones with too much capacity use
used_cap = np.zeros(m, dtype=int)
over_cap = np.zeros(len(res)-1, dtype=int)
for h in range(len(res)-1):
    machine = 0
    used_cap = np.zeros(m, dtype=int)
    for u in range(len(res[h])-1):
        #print(u)
        machine = res[h][u]
        #print(machine)
        used_cap[machine] += capacity_req[machine][u]
    for f in range(m):
        if used_cap[f] > capacity_mac[f]:
            over_cap[h] = 1

#print(over_cap)


#calculate the cheapest
use_cost = np.zeros(n, dtype=int)
cheapest = 100000
assigns = list()
for t in range(len(res)-1):
    if not over_cap[t]:
        cost = 0
        for g in range(n):

            cost += costs[res[t][g]][g]
        if cost < cheapest:
            cheapest = cost
            assigns = res[t]

print("Total cost: " + str(cheapest))
cap = np.zeros(m,dtype=int)
for p in range(n):
    cap[assigns[p]] += capacity_req[assigns[p]][p]
print("Capacity used for the machine: " + str(cap))
print("Machine assigned to job: " + str(assigns))





