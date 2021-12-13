import numpy as np


def get_array(lines):
    coords, folds = [], []
    fold_line = False
    max_x, max_y = 0, 0
    for line in lines:
        if line == '':
            fold_line = True
            continue

        if fold_line:
            axe = line.split('=')[0].split(' ')[-1]
            folds.append((axe, int(line.split('=')[-1])))
        else:
            line_split = line.split(',')
            max_x, max_y = max(max_x, int(line_split[0])), max(max_y, int(line_split[1]))
            coords.append((int(line_split[0]), int(line_split[-1])))

    array = np.zeros((max_y + 1, max_x + 1))
    for coord in coords:
        array[coord[1], coord[0]] = 1
    return array, folds


def main(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split('\n')]

    array, folds = get_array(lines)

    for fold in folds:
        if fold[0] == 'y':
            array1, array2 = array[:fold[1]], array[fold[1] + 1:]
            for i in range(len(array1)):
                array1[i] = np.where(array2[-i - 1] == 1, 1, array1[i])
        else:
            array1, array2 = array[:, :fold[1]], array[:, fold[1] + 1:]
            for i in range(len(array1)):
                array1[i] = np.where(np.flip(array2[i] == 1, 0), 1, array1[i])
        array = array1
        print('Number of dots after %s: %s' % (fold, np.count_nonzero(array)))

    with open('result.txt', 'w') as f:
        for line in array:
            s = "".join(['#' if elt == 1 else '.' for elt in line]) + '\n'
            f.write(s)


if __name__ == "__main__":
    main('day13_input.txt')
