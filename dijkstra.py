from functools import reduce
import math
import sys 
import matplotlib.pyplot as plt

labels = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J'
}

coords = {
    'A': (3, 3),
    'B': (6, 3),
    'C': (0, 3),
    'D': (0, 5),
    'E': (3, 1),
    'F': (9, 3),
    'G': (2, 5),
    'H': (9, 7),
    'I': (4, 5),
    'J': (4, 7)
}

adjacent = [
    #0th row
    [0, 2, 2, math.sqrt(5), 0, 0, 0, 0, 0, 0],
    #1st row
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    #2nd row
    #3rd row
    [2, 0, 0, 1, math.sqrt(5), 0, 0, 0, 0, 0],
    [math.sqrt(5), 0, 1, 0, 0, 0, 1, 0, 0, 0],
    #4th row
    [0, 0, math.sqrt(5), 0, 0, math.sqrt(26), 0, 0, 0, 0],
    #5th row
    [0, 2, 0, 0, math.sqrt(26), 0, 0, 3, math.sqrt(17), 0],
    #6th row
    [0, 0, 0, 1, 0, 0, 0, 0, 0, math.sqrt(2)],
    #7th row
    [0, 0, 0, 0, 0, 3, 0, 0, 0, 4],
    #8th row
    [0, 0, 0, 0, 0, math.sqrt(17), 0, 0, 0, 1],
    #9th row
    [0, 0, 0, 0, 0, 0, math.sqrt(2), 4, 1, 0]
]

graph = {
    'A': [('B', 2), ('C', 2), ('D', math.sqrt(5))],
    'B': [('A', 2), ('F', 2)],
    'C': [('A', 2), ('D', 1), ('E', math.sqrt(5))],
    'D': [('A', math.sqrt(5)), ('C', 1), ('G', 1)],
    'E': [('C', math.sqrt(5)), ('F', math.sqrt(26))],
    'F': [('B', 2), ('E', math.sqrt(26)), ('I', math.sqrt(17))],
    'G': [('D', 1), ('J', math.sqrt(2))],
    'H': [('F', 3), ('J', 4)],
    'I': [('F', math.sqrt(17)), ('J', 1)],
    'J': [('G', math.sqrt(2)), ('H', 4), ('I', 1)]
}

x_points = [coords[i][0] for i in sorted(coords)]
y_points = [coords[i][1] for i in sorted(coords)]

plt.plot(x_points, y_points, 'bo')

plt.axis([-1, 10, -1, 10])

plt.grid()

for i in range(10):
    plt.text(x_points[i] - 0.5, y_points[i] + 0.25, labels[i])

for i in range(10):
    for j in range(10):
        if adjacent[i][j]:
            plt.plot([x_points[i], x_points[j]], [y_points[i], y_points[j]], 'b')

def dijkstras(graph, start, end):
    infer = reduce(lambda x, y: x + y, (i[1] for j in graph for i in graph[j]))
    
    distance = dict.fromkeys(graph, infer)

    previous = dict.fromkeys(graph)

    log = list(graph)

    distance[start] = 0

    while log:
        u = min(log, key = lambda x: distance[x])
        log.remove(u)

        for v, w in graph[u]:
            alternate = distance[u] + w

            if alternate < distance[v]:
                distance[v] = alternate
                previous[v] = u
    
    traveled = []

    temp = end

    while temp != start:
        traveled.append(previous[temp])

        temp = previous[temp]
    
    traveled.reverse()
    traveled.append(end)

    return (" -> ".join(traveled), distance[end])

traverse, dist = dijkstras(graph, 'A', 'H')

print(traverse)

drawing = traverse.split("-> ")

plt.plot([coords[n.rstrip()][0] for n in drawing], [coords[n.rstrip()][1] for n in drawing])

print("Distance: {}".format(dist))

plt.show()