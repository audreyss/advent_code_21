import numpy as np


def expand_array(array, nb_lines, nb_col):
    for _ in range(4):
        for i in range(nb_lines):
            array[i].extend([(elt + 1) if elt < 9 else 1 for elt in array[i][-nb_col:]])

    for _ in range(4):
        last_lines = array[-nb_lines:]
        for i in range(nb_lines):
            array.append([(elt + 1) if elt < 9 else 1 for elt in last_lines[i]])

    return array


def update_neighbor(u, v, array, dist, prev):
    tmp = dist[u] + array[v]
    if tmp < dist[v]:
        dist[v] = tmp
        prev[v] = u
    return dist, prev


def main(filename, expand=False):
    with open(filename, 'r') as file:
        array = [[int(elt) for elt in line] for line in file.read().split('\n')]
        nb_lines, nb_col = len(array), len(array[0])
        if expand:
            array = expand_array(array, nb_lines, nb_col)
            nb_lines, nb_col = len(array), len(array[0])

        array = [item for sublist in array for item in sublist]

    dist = [float('inf')] * len(array)
    dist[0] = 0
    unvisited = [i for i in range(len(array))]
    prev = [-1] * len(array)

    while len(unvisited) != 0:
        dist_unvisited = [dist[vertex] for vertex in unvisited]
        u = unvisited[dist_unvisited.index(min(dist_unvisited))]
        unvisited.remove(u)

        if u == nb_lines * nb_col - 1:
            break

        i, j = u // nb_lines, u % nb_lines
        neighbors = [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]

        for neighbor in neighbors:
            v = neighbor[0] * nb_lines + neighbor[1]
            if 0 <= neighbor[0] < nb_lines and 0 <= neighbor[1] < nb_col and v in unvisited:
                dist, prev = update_neighbor(u, v, array, dist, prev)

    print("Cost: %s" % dist[nb_lines * nb_col - 1])


if __name__ == "__main__":
    main('day15_input.txt')
    main('day15_input.txt', True)

