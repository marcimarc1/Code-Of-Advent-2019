from shapely.geometry import LineString
#read data
filename='D3/data.txt'
wires = []
with open(filename) as f:
    for lines in f.readlines():
        wires.append(lines)
        wires[-1] = wires[-1].strip('\n').split(',')


def generate_line(inputs,start_point):
    direction = inputs[0]
    length = int(inputs[1:])
    if direction == 'R':
        endpoitnt = (start_point[0]+ length,start_point[1])    
        return endpoitnt
    if direction == 'L':
        endpoitnt = (start_point[0]-length,start_point[1])
        return endpoitnt
    if direction == 'U':
        endpoitnt = (start_point[0],start_point[1]+length)
        return endpoitnt
    if direction == 'D':
        endpoitnt = (start_point[0],start_point[1]-length)
        return endpoitnt


def generate_wire(wire):
    start_point = (0,0)
    lines = [start_point]
    for l in wire:
        start_line = lines[-1]
        lines.append(generate_line(l, start_line))
    return lines

def manhattan(point1, point2):
    return(abs(point1[0]-point2[0]) + abs(point1[1]-point[2]))

def wire_intersect(wire1 , wire2):
    inter = []
    for p in range(len(wire1)-1):
        line = LineString([wire1[p],wire1[p+1]])
        for q in range(len(wire2)-1):
            line2 = LineString([wire2[q],wire2[q+1]])
            inter.append(line.intersection(line2))
    return inter 



def wire_intersect_and_distance(wire1 , wire2):
    inter = []
    wire1_dist = 0 
    for p in range(len(wire1)-1):
        line = LineString([wire1[p],wire1[p+1]])
        wire1_dist += line.length
        wire2_dist = 0 
        for q in range(len(wire2)-1):
            line2 = LineString([wire2[q],wire2[q+1]])
            wire2_dist += line2.length 
            inter.append([line.intersection(line2), wire1_dist+wire2_dist])
            if not inter[-1][0].is_empty:
                rest1 = LineString([inter[-1][0],wire1[p+1]])
                rest2 = LineString([inter[-1][0],wire2[q+1]])
                inter[-1][1] = inter[-1][1]-rest1.length-rest2.length
    return inter 


w = [generate_wire(i) for i in wires]
inter = wire_intersect_and_distance(w[0],w[1])
small = 0 
min_dist = 10000000000
steps = 0
min_steps = 1000000000000
for i in inter:
    if i[0].is_empty == False:
        #dist = abs(i.x)+abs(i.y)
        steps = i[1]
        print(steps)
        if steps <1:
            continue
        if min_steps>steps:
            min_steps = steps

print(min_steps)