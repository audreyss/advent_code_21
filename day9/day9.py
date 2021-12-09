import numpy as np


def get_size_basin(array, i, j, visited):
    val = array[i, j]
    if val == 9 or visited[i, j] == 1:
        return 0
    visited[i, j] = 1
    s = 1
    if i > 0 and array[i - 1, j] > val:
        s += get_size_basin(array, i - 1, j, visited)
    if i < (array.shape[0] - 1) and array[i + 1, j] > val:
        s += get_size_basin(array, i + 1, j, visited)
    if j > 0 and array[i, j - 1] > val:
        s += get_size_basin(array, i, j - 1, visited)
    if j < (array.shape[1] - 1) and array[i, j + 1] > val:
        s += get_size_basin(array, i, j + 1, visited)
    return s


def main(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split('\n')]
        array = np.array([[int(elt) for elt in line] for line in lines])

    nbs = []
    pos_low_pts = []
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            up = array[i - 1, j] if i != 0 else 9
            down = array[i + 1, j] if i != (array.shape[0] - 1) else 9
            left = array[i, j - 1] if j != 0 else 9
            right = array[i, j + 1] if j != (array.shape[1] - 1) else 9
            if min(up, down, right, left) > array[i, j]:
                nbs.append(array[i, j])
                pos_low_pts.append((i, j))

    print("Sum of the risk levels of low points: %s" % sum([nb + 1 for nb in nbs]))

    size_basin = []
    for pos in pos_low_pts:
        visited = np.zeros(array.shape)
        size = get_size_basin(array, pos[0], pos[1], visited)
        size_basin.append(size)

    size_basin.sort()
    print("Product of the sizes of the three largest basins: %s" % np.prod(size_basin[-3:]))


if __name__ == "__main__":
    main('day9_input.txt')



