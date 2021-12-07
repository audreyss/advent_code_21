def main(filename, constant=True):
    with open(filename, 'r') as file:
        list_pos = [int(elt) for elt in file.readline().rstrip().split(',')]

    list_fuel = []
    for i in range(max(list_pos)):
        if constant:
            tmp = [abs(pos - i) for pos in list_pos]
        else:
            tmp = [sum(range(abs(pos - i) + 1)) for pos in list_pos]
        list_fuel.append(sum(tmp))

        if i > 0 and list_fuel[i - 1] < list_fuel[i]:
            break

    min_fuel = min(list_fuel)
    print("Index min value and min value: %s %s" % (list_fuel.index(min_fuel), min_fuel))


if __name__ == "__main__":
    main('day7_input.txt')
    main('day7_input.txt', False)



