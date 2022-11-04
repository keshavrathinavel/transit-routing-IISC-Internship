from collections import defaultdict
import heapq

# filename = './sample_net.tntp'
filename = r'python_exam\\ChicagoSketch_net.tntp'
with open(filename, 'r') as file:
    lines = [line.rstrip() for line in file]

metadata_lines = lines[:6]
header_line = lines[8]
data_lines = lines[9:]

num_nodes = 1 + int(metadata_lines[1].rsplit(' ')[-1])
## adding one because nodes are 1-based indexed

adjacency_matrix = [[0]*num_nodes for i in range(num_nodes)]
adjacency_list = defaultdict(list)
## DO NOT DO adjacency_matrix = [[0]*num_nodes]*num_nodes

for line in data_lines:
    if line:
        line_as_list = line.rsplit('\t')
        init_node = int(line_as_list[1])
        term_node = int(line_as_list[2])
        length = float(line_as_list[4])
        # print(f'{init_node} {term_node} {length}')
        if init_node in adjacency_list:
            adjacency_list[init_node].append([term_node, length])
        else:
            adjacency_list[init_node] = [[term_node, length]]
        # adjacency_matrix[init_node][term_node] = length

 
## adjacency list is the intended graph object for q1

print(adjacency_list)

nodeList = []
for key, value in adjacency_list.items():
    # templis = []
    temp = list(value)
    for i in temp:
        u = key
        v = i[0]
        w = i[1]
        nodeList.append([u, v, w])

def Dijkstraheap(nodeList):
    edges = defaultdict(list)
    for u, v, w in nodeList:
        edges[u].append((v, w))
    


## nodeList has all the nodes of the graph where u is init_node, v is term_node and w is the distance      
# print(nodeList)      


