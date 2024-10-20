import networkx as nx
import matplotlib.pyplot as plt

#bellman-ford psuedo

#distance list = infinite
#predecessor list = 0
#relaxing of nodes
#for all nodes:
#    if distance(u) + weight(u -> v) < distance(v):
#        distance(v) = distance(u) + weight(u -> v)
#        predecessor list(v) = u
#negative cycle test
#for all edges:
#    if distance(u) + weight(u->v) < distance(v)
#        print('negative cycle')

def BellmanFord(Graph, source): #takes input of a networkx graph and integer representing the source node
    n = Graph.number_of_nodes()
    #initialise a list for distance travelled and node predecessor
    distance = list()
    pred = list()

    for i in range(n): #set distance list with infinity and predecessor list with 0
        distance.append(float('inf'))
        pred.append(0)
    distance[source] = 0

    for _ in range(n-1): #relax the edges if the distance is shorter and update predecessor
        for u, v, data in Graph.edges(data=True):
            weight = data.get('weight')

            if distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                pred[v] = u

    for u, v, data in Graph.edges(data=True): #tests if the graph has a negative cycle(s)
        weight = data.get('weight')
        if distance[u] + weight < distance[v]:
            print('Negative cycle detected')

    return distance, pred

def get_coords(text_file):
    coordMat = list()
    with open(text_file, 'r') as reader:
        for line in reader:
            line = line.rstrip('\n')
            a = line.split()
            a[0] = int(a[0])
            if 0 <= 1 < len(a):
                for i in range(len(a)):
                    a[i] = int(a[i])
            coordMat.append(a)
    return coordMat

def graphConstructor(elist):
    Gr = nx.DiGraph()
    infolist = elist.copy()
    infolist.pop(0)
    for i in range(elist[0][0]+1):
        Gr.add_node(i)
    for u in range(Gr.number_of_nodes()):
        for v in range(u+1,Gr.number_of_nodes()):
            f = infolist[u][1]
            if v-u>1:
                d = 0
                for x in range(u,v):
                    d += infolist[x][0]
            else:
                d = infolist[u][0]
            c = infolist[u][2]
            edgecost = f+c*d
            Gr.add_edge(u,v,weight=edgecost)



    return Gr

lotM = get_coords('lotsizing_n6.txt')
print(lotM)
G = graphConstructor(lotM)



v = list()
for i in range(G.number_of_nodes()):
    v.append(i)
h = BellmanFord(G,0)

print('Dist: ' + str(h[0]))
print('V:    ' + str(v))
print('Path: ' + str(h[1]))

pos = {
    0:(0, 0),
    1:(1, 3),
    2:(2, 5),
    3:(3, 7),
    4:(4, 5),
    5:(5, 3),
    6:(6, 0)
}

nx.draw(G,pos,with_labels=True, node_size=100, linewidths=10, arrowsize=30)
edge_labels= dict([((n1,n2), d['weight'])
                   for n1,n2,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
plt.show()