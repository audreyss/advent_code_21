def main_p1(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split('\n')]

    count = 0
    for line in lines:
        patterns, output_values = line.split(' | ')[0], line.split(' | ')[1]
        valid_output = [value for value in output_values.split(' ') if len(value) in [2, 4, 3, 7]]
        count += len(valid_output)

    print("Number of 1, 4, 7 and 8: %s" % count)


def main_p2(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split('\n')]

    total = 0
    for line in lines:
        dict_len_pattern = {len(elt): set(elt) for elt in line.split(' | ')[0].split(' ')}

        nb = 0
        for val in line.split(' | ')[1].split(' '):
            if len(val) == 2:
                nb = nb * 10 + 1
            elif len(val) == 3:
                nb = nb * 10 + 7
            elif len(val) == 4:
                nb = nb * 10 + 4
            elif len(val) == 7:
                nb = nb * 10 + 8
            elif len(val) == 5 and len(set(val) & set(dict_len_pattern[3])) == 3:
                nb = nb * 10 + 3
            elif len(val) == 5 and len(set(val) & set(dict_len_pattern[4])) == 3:
                nb = nb * 10 + 5
            elif len(val) == 5:
                nb = nb * 10 + 2
            elif len(val) == 6 and len(set(val) & set(dict_len_pattern[4])) == 4:
                nb = nb * 10 + 9
            elif len(val) == 6 and len(set(val) & set(dict_len_pattern[3])) == 3:
                nb = nb * 10 + 0
            else:
                nb = nb * 10 + 6
        total += nb

    print("Output values sum: %s" % total)


if __name__ == "__main__":
    main_p1('day8_input.txt')
    main_p2('day8_input.txt')




