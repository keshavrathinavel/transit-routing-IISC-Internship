"""
CiSTUP Internship: Round 1
Enter the solution for Q1 here.
Note: You may use may define any additional class, functions if necessary.
However, DO NOT CHANGE THE TEMPLATE CHANGE THE TEMPLATE OF THE FUNCTIONS PROVIDED.
"""
from collections import defaultdict


def Dij_generator():
    """
    Reads the ChicagoSketch_net.tntp and convert it into suitable python object on which you will implement shortest-path algorithms.

    Returns:
        graph_object: variable containing network information.
    """
    filename = r'python_exam\\ChicagoSketch_net.tntp'
    with open(filename, 'r') as file:
        lines = [line.rstrip() for line in file]

    # metadata_lines = lines[:6]
    # header_line = lines[8]
    data_lines = lines[9:]

    # num_nodes = 1 + int(metadata_lines[1].rsplit(' ')[-1])
    ## adding one because nodes are 1-based indexed

    # adjacency_matrix = [[0]*num_nodes for i in range(num_nodes)]
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

    

    graph_object = adjacency_list
    try:
        # Enter your code here
        return graph_object
    except:
        return graph_object


def Q1_dijkstra(source: int, destination: int, graph_object) -> int:
    """
    Dijkstra's algorithm.

    Args:
        source (int): Source stop id
        destination (int): : destination stop id
        graph_object: python object containing network information

    Returns:
        shortest_path_distance (int): length of the shortest path.

    Warnings:
        If the destination is not reachable, function returns -1
    """
    
    try:
        # Enter your code here
        # nodeList = []
        # edges = defaultdict(list)
        # for key, value in graph_object.items():
        #     # templis = []
        #     temp = list(value)
        #     for i in temp:
        #         u = key
        #         v = i[0]
        #         w = i[1]
        #         nodeList.append([u, v, w])
        
        # for u, v, w in nodeList:
        #     edges[u].append(v, w)

        # minHeap = [(0, source)]
        # visit = set()
        # t = 0
        # while minHeap:
        #     w1, n1 = heapq.heappop(minHeap)
        #     if n1 in visit:
        #         continue
        #     visit.add(n1)
        #     t = max(t, w1)
        #     for n2, w2 in edges[n1]:
        #         if n2 not in visit:
        #             heapq.heappush(minHeap, (w1+w2, n2))
        # return t if len(visit) == destination else -1
        
        def dijkstra(graph, src, dst=None):
            nodes = []
            for n in graph:
                nodes.append(n)
                nodes += [x[0] for x in graph[n]]

            q = set(nodes)
            nodes = list(q)
            dist = dict()
            prev = dict()
            for n in nodes:
                dist[n] = float('inf')
                prev[n] = None
            dist[src] = 0
            while q:
                u = min(q, key=dist.get)
                q.remove(u)

                if dst is not None and u == dst:
                    return dist[dst], prev

                for v, w in graph.get(u, ()):
                    alt = dist[u] + w
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u

            return dist
        
        # def find_path(pr, node):  # generate path list based on parent points 'prev'
        #     p = []
        #     while node is not None:
        #         p.append(node)
        #         node = pr[node]
        #     return p[::-1]

        # d, prev = dijkstra(source, destination, graph_object)
        shortest_path_distance = dijkstra(graph_object, source, destination)    
        return shortest_path_distance
    except:
        return shortest_path_distance

graph_object = Dij_generator()

print(Q1_dijkstra(253, 127, graph_object))

from time import time



def evaluate_Q1(sample_input1):
    marks = 0
    avg_runtime = 1
    graph_object = None
    try:
        from Q1 import Dij_generator, Q1_dijkstra
        graph_object = Dij_generator()
        start_time = time()
        candidate_output = [round(Q1_dijkstra(source, destination, graph_object)) for source, destination in sample_input1]
        avg_runtime = avg_runtime + (time() - start_time) / len(sample_input1)
        if candidate_output == output_Q1Q2:
            marks = marksQ1
    except:
        pass
    return marks, graph_object, avg_runtime

def main():
    print("Running Q1")
    marksQ1, graph_object, avg_runtime = evaluate_Q1(input_Q1Q2)
    total = marksQ1 
    print(f"Marks in Q1: {marksQ1}")

    print(f"Avg Runtime in seconds for Q1: {avg_runtime}")
    print(f"Final Score: {total}")
    return marksQ1

if __name__ == "__main__":
    input_Q1Q2 = [(253, 127), (139, 305), (148, 99), (363, 134), (778, 396), (650, 759), (724, 547), (788, 412), (105, 1)]
    output_Q1Q2 = [38, 59, 29, 76, 30, 70, 53, 59, 51]
    input_Q3 = [('3003', '3004'), ('15', '6476b50b-bb5e-48e0-b2d9-e25aead5e3fd'), ('7', '8'), ('7', '80'), ('19', '3010'),
                ('3895ff8a-6cc3-44af-a8b5-23636fd1dba6', 'a7274768-ade1-4b21-b3b6-7f368d2a684b')]
    output3 = [2, 1, 0, 0, 1, 1]
    marksQ1, marksQ2, marksQ3 = 2, 4, 4
    main()