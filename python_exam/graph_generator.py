'''
I have created a sample_net.tntp with only 3 nodes.
Look at that file and the print statements of this file. 
After you're satisfied with the output, you can suppress
this file's print statements and change the tntp filename.

The adjacency_matrix is your graph_object
'''


# filename = r'./sample_net.tntp'
filename  = r"C:\Users\kesha\Documents\GitHub\transit-routing-IISC-Internship\python_exam\ChicagoSketch_net.tntp"
with open(filename, 'r') as file:
    lines = [line.rstrip() for line in file]

metadata_lines = lines[:6]
header_line = lines[8]
data_lines = lines[9:]

num_nodes = 1 + int(metadata_lines[1].rsplit(' ')[-1])
# adding one because nodes are 1-based indexed

adjacency_matrix = [[0]*num_nodes for i in range(num_nodes)]
# DO NOT DO adjacency_matrix = [[0]*num_nodes]*num_nodes

for line in data_lines:
    if line:
        line_as_list = line.rsplit('\t')
        init_node = int(line_as_list[1])
        term_node = int(line_as_list[2])
        length = float(line_as_list[4])
        # print(f'{init_node} {term_node} {length}')
        adjacency_matrix[init_node][term_node] = length
print(adjacency_matrix)

