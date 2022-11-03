import re
import itertools

inputLocation = r'C://Users//kesha//Documents//GitHub//transit-routing-IISC-Internship//python_exam//'
# inputLocation2 = 'Data/'


od = {}
class data:
    line_value = []
    init_node = []
    term_node = []
    capacity = []
    length = []
    free_flow_time = []
    b = []
    power = []
    speed = []
    toll = []
    link_type = []


# origin_no = []  # our starting Origin number in case the file doesn't begin with one
with open(inputLocation+"ChicagoSketch_net.tntp", "r") as f:
    dat = data()
    templis = []
    for line in f:
        if line.startswith("<NUMBER OF ZONES>"):
            num_zones = int(line[18:].strip())
            continue
        if line.startswith("<NUMBER OF NODES>"):
            num_nodes = int(line[18:].strip())
            continue
        if line.startswith("<NUMBER OF LINKS>"):
            num_links = int(line[18:].strip())
            continue
        else:
            if line.startswith('<'):
                continue
            if not line: continue
            # if line.startswith("<END OF METADATA>"):
            #     for i in range(0,3):
            #         next(f)
            else:
                elements = line.split(";")
                for element in elements:
                    if not element:
                        continue
                    dat.line_value.append(re.split(r'\t+', element))
    del dat.line_value[0:4]
    # dat.line_value.sort()
    # list(dat.line_value for dat.line_value,_ in itertools.groupby(dat.line_value) )
    recurring_elements = []
    for elem in dat.line_value:
        if elem not in recurring_elements:
            recurring_elements.append(elem)
    dat.line_value = recurring_elements
    for sub_list in dat.line_value:
        for item in sub_list:
            templis = item.split()
            print(templis)
            

           
    
    f.close()
print("num_zones: " + str(num_zones))
print("num_nodes: " + str(num_nodes))
print("num_links: " + str(num_links))
# print(dat.line_value)
# print(dat.init_node)

    
    # for line in f:
    #     line = line.rstrip()  # we're not interested in the newline at the end
    #     if not line:  # empty line, skip
    #         continue
    #     if line.startswith("Origin"):
    #         origin_no = int(line[7:].strip())  # grab the integer following Origin
    #     else:
    #         elements = line.split(";")  # get our elements by splitting by semi-colon
    #         for element in elements:  # loop through each of them:
    #             if not element:  # we're not interested in the last element
    #                 cont  inue
    #             element_no, element_value = element.split(":")  # get our pair
    #             # beware, these two are now most likely padded strings!
    #             # that's why we'll strip them from whitespace and convert to integer/float
    #             if(origin_no != int(element_no.strip())):
    #                 od[(origin_no, int(element_no.strip()))] = float(element_value.strip())



# network = {}
# with open(inputLocation+"SiouxFalls_net.tntp", "r") as f:
#     next(f)
#     for line in f:
#         line = line.rstrip()
#         line = line.split(";")[[]].split('\t')
#         #print([line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]])
#         network[line[1], line[2]] = [line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]]


# def printOD_flows():
#     outFile = open(inputLocation2 + "demand.dat", "w")
#     tmpOut = "origin\tdest\tdemand"
#     outFile.write(tmpOut+"\n")
#     for d in od:
#         tmpOut = str(d[[]])+"\t"+str(d[1])+"\t"+str(od[d])
#         outFile.write(tmpOut+"\n")
#     outFile.close()

# def printNetwork():
#     outFile = open(inputLocation2+"network.dat", "w")
#     tmpOut = "origin\tdest\tcapacity\tlength\tfft\talpha\tbeta\tspeedLimit"
#     outFile.write(tmpOut+"\n")
#     for link in network:
#         tmpOut ='\t'.join(network[link])
#         outFile.write(tmpOut+"\n")
#     outFile.close()




# printOD_flows()
# printNetwork()