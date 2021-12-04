import numpy as np
import re


def get_score(check_val_arr, list_mat, nb, id_mat=-1):
    if id_mat == -1:
        id_mat = np.argwhere(check_val_arr)[0][0]
    mat = np.where(list_mat[id_mat] == -1, 0, list_mat[id_mat])
    print("Number: {}".format(nb))
    print("Sum: {}".format(np.sum(mat)))
    print("Final score: {}".format(nb * np.sum(mat)))
    return True


def main(filename):
    with open(filename, 'r') as file:
        list_mat = []
        lines = []
        while line := file.readline():
            if line == '\n':
                list_mat.append(np.array(lines))
                lines = []
            else:
                lines.append([int(nb) for nb in re.split('[, ]', line.rstrip()) if nb.isdigit()])
        list_mat.append(np.array(lines))

    nbs, list_mat = list_mat[0][0], list_mat[1:]

    got_first = False
    last_check_val = []

    for nb in nbs:
        # For each matrix: change called nb values (nb) to -1
        list_mat = [np.where(mat == nb, -1, mat) for mat in list_mat]
        # [np.all(mat == -1, axis=1) for mat in list_mat] -> for each matrix, check if all values in rows are equal to
        # -1, get a np.array for each matrix with True or False for each row
        # np.any(..., axis=1) -> check for each matrix if one row is complete of marked nbs (-1), get a np.array of
        # (nbs_of_matrices) True/False values
        check_val_row = np.any([np.all(mat == -1, axis=1) for mat in list_mat], axis=1)
        check_val_col = np.any([np.all(mat == -1, axis=0) for mat in list_mat], axis=1)
        check_val = [check_val_row[i] or check_val_col[i] for i in range(len(list_mat))]

        if not got_first and np.any(check_val):
            print("Part one")
            got_first = get_score(check_val_row, list_mat, nb)
            print("----------------------")

        if np.all(check_val):
            print("Part two")
            curr = np.argwhere(check_val).reshape(len(list_mat)).tolist()
            prev = last_check_val.reshape(len(list_mat) - 1).tolist()
            id_last_mat = list(set(curr) - set(prev))[0]
            get_score(check_val_row, list_mat, nb, id_last_mat)
            break

        last_check_val = np.argwhere(check_val)


if __name__ == "__main__":
    main('day4_input.txt')
