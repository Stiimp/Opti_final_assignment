
import numpy as np

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

inp = read_input('GAP_2.txt')
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

used_cap = np.zeros(m, dtype=int)
assigned_machine = np.zeros(n, dtype=int)
use_cost = np.zeros(n, dtype=int)

for j in range(n): # for all jobs
    cheapest = 100000
    cheapest_machine = -1
    for i in range(m): #for all machines
        if costs[i][j] < cheapest and used_cap[i] + capacity_req[i][j] < capacity_mac[i]:
            cheapest = costs[i][j]
            cheapest_machine = i
    assigned_machine[j] = cheapest_machine
    used_cap[cheapest_machine] += capacity_req[cheapest_machine][j]
    use_cost[j] = cheapest


print("Capacity used for the machine: " + str(used_cap))
print("Machine assigned to job: " + str(assigned_machine))
print("Total cost: " + str(sum(use_cost)))




