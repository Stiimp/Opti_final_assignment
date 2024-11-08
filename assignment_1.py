import networkx as nx
import queue
import matplotlib.pyplot as plt

def kahn(Gr): #takes input of a directed graph from the networkx library
    # initialise a list for the indegrees of all nodes in graph G
    n = G.number_of_nodes()
    inDeg = list()
    # intialise a queue that contains nodes with an indegree of 0
    q = queue.Queue()
    k = 0
    for l in range(max(Gr.nodes)+1):
        if Gr.has_node(l):
            inDeg.append(Gr.in_degree(l))  # Fills our indegree list
            if (inDeg[k]) == 0:
                q.put(l)  # Fills our queue
            k += 1
        else:
            inDeg.append(-1)
            k += 1
    index = 0  # error reference
    order = []  # the output with the final topological orderingS
    while not q.empty():
        # fills the order list with the node that is in the front of the queue
        at = q.get()
        order.append(at)

        index += 1
        # searches the downstream neighbors and modifies the indegree to represent removal of upstream nodes
        for cnode in Gr.successors(at):
            inDeg[cnode] -= 1
            if (inDeg[cnode] == 0):  # if the node has no upstream nodes adds it to the queue
                q.put(cnode)
    if index != n:
        return None  # if the graph contains cycles the function will return none
    return order

def get_coords(text_file):
    coordMat = list()
    with open(text_file, 'r') as reader:
        for line in reader:
            line = line.rstrip('\n')
            a = line.split()
            a[0] = int(a[0])
            if 0 <= 1 < len(a):
                a[1] = int(a[1])
            coordMat.append(a)
    return coordMat

def graphConstructor(elist):
    nodeAdapt = not(0 in elist)
    H = nx.DiGraph()
    Gr = nx.DiGraph()
    for i in range(len(elist)):
        if len(elist[i]) == 1:
            continue
        else:
            #nodeAdapt makes it so that we start from node 0 instead of node 1
            H.add_edge(elist[i][0]-nodeAdapt, elist[i][1]-nodeAdapt)
    #recreate the graph with the nodes sorted in order
    #node_sorted = sorted(H.nodes)
    Gr.add_nodes_from(sorted(H.nodes))
    Gr.add_edges_from(H.edges)
    return Gr

edgeList = get_coords('node_info.txt')
print(edgeList)
G = graphConstructor(edgeList)
print('The topological order of the graph is: ' + str(kahn(G)))

pos = nx.planar_layout(G)
nx.draw(G,pos,with_labels=True, node_size=100, linewidths=10, arrowsize=30)
plt.show()