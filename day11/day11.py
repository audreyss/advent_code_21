import numpy as np

dir_line = [-1, -1, -1, 0, 0, 1, 1, 1]
dir_col = [-1, 0, 1, -1, 1, -1, 0, 1]


def update_array(array, flashes):
    array = array + 1
    pos_flashes = np.where(array > 9)
    queue = [(pos_flashes[0][i], pos_flashes[1][i]) for i in range(len(pos_flashes[0]))]
    visited = []

    while len(queue) > 0:
        pos = queue.pop(0)
        if pos in visited:
            continue

        i, j = pos
        for ind_dir in range(len(dir_line)):
            a, b = i + dir_line[ind_dir], j + dir_col[ind_dir]
            if 0 <= a < len(array) and 0 <= b < len(array[0]):
                array[a, b] += 1

        for ind_dir in range(len(dir_line)):
            a, b = i + dir_line[ind_dir], j + dir_col[ind_dir]
            if 0 <= a < len(array) and 0 <= b < len(array[0]) and array[a, b] > 9:
                queue.append((a, b))

        visited.append(pos)
        flashes += 1
    array = np.where(array > 9, 0, array)
    return array, flashes


def main(filename, nb_steps):
    with open(filename, 'r') as file:
        lines = [[int(elt) for elt in line.rstrip()] for line in file.readlines()]
    array = np.array(lines)

    flashes = 0
    for _ in range(nb_steps):
        array, flashes = update_array(array, flashes)
    print("Number of flashes: %s" % flashes)

    step = nb_steps
    while not np.all(array == 0):
        array, flashes = update_array(array, flashes)
        step += 1
    print("Full flash %s" % step)


if __name__ == "__main__":
    main('day11_input.txt', 100)
