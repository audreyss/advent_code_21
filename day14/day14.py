def main(filename, nb_steps):
    with open(filename, 'r') as file:
        polymer = file.readline().rstrip()
        file.readline()
        rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in file.read().split('\n')}

    polymer_list = [polymer[i:i + 2] for i in range(len(polymer) - 1)]
    pair_occurrences = {pair: polymer_list.count(pair) for pair in set(polymer_list)}

    # we keep track of the pair occurrences and forget about the order
    for n in range(nb_steps):
        tmp = {}
        for pair, nb in pair_occurrences.items():
            elt = rules[pair]
            pair1, pair2 = pair[0] + elt, elt + pair[1]
            tmp[pair1] = tmp[pair1] + nb if pair1 in tmp else nb
            tmp[pair2] = tmp[pair2] + nb if pair2 in tmp else nb
        pair_occurrences = tmp

    nb_occ = {}
    for pair, nb in pair_occurrences.items():
        nb_occ[pair[0]] = nb_occ[pair[0]] + nb if pair[0] in nb_occ else nb
    nb_occ[polymer[-1]] += 1
    print('Subtraction result: %s' % (max(nb_occ.values()) - min(nb_occ.values())))


if __name__ == "__main__":
    main('day14_input.txt', 10)
    main('day14_input.txt', 40)
