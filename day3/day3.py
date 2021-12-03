def part1(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split('\n')]

    len_lines, len_str = len(lines), len(lines[0])
    nb_of_1 = [sum([int(lines[i][j]) for i in range(len_lines)]) for j in range(len_str)]

    gamma = ['1' if nb1 > (len_lines - nb1) else '0' for nb1 in nb_of_1]
    gamma = int("".join(gamma), 2)
    print("Gamma rate {}".format(gamma))

    epsilon = ['1' if nb1 < (len_lines - nb1) else '0' for nb1 in nb_of_1]
    epsilon = int("".join(epsilon), 2)
    print("Epsilon rate {}".format(epsilon))

    print("Gamma * Epsilon {}".format(epsilon * gamma))


def part2(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split('\n')]
    len_lines, len_str = len(lines), len(lines[0])

    nbs_for_oxygen, nbs_for_co2 = list(lines), lines
    for i in range(len_str):
        if len(nbs_for_oxygen) == 1:
            break
        nbs_with_1 = [nb for nb in nbs_for_oxygen if nb[i] == '1']
        nbs_with_0 = [nb for nb in nbs_for_oxygen if nb[i] == '0']

        if len(nbs_with_1) >= len(nbs_with_0):
            nbs_for_oxygen = nbs_with_1
        else:
            nbs_for_oxygen = nbs_with_0

    for i in range(len_str):
        if len(nbs_for_co2) == 1:
            break
        nbs_with_1 = [nb for nb in nbs_for_co2 if nb[i] == '1']
        nbs_with_0 = [nb for nb in nbs_for_co2 if nb[i] == '0']

        if len(nbs_with_1) < len(nbs_with_0):
            nbs_for_co2 = nbs_with_1
        else:
            nbs_for_co2 = nbs_with_0

    if len(nbs_for_oxygen) != 1 or len(nbs_for_co2) != 1:
        print("Error: too large")
        return

    oxygen, co2 = nbs_for_oxygen[0], nbs_for_co2[0]
    print('Oxygen generator rating value ' + oxygen)
    print('CO2 scrubber rating value ' + co2)
    print('Multiplication oxygen * co2 {}'.format(int(oxygen, 2) * int(co2, 2)))


if __name__ == "__main__":
    part1('day3_input.txt')
    part2('day3_input.txt')
