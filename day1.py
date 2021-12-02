def main():
    with open('day1_input.txt', 'r') as file:
        lines = [int(line.rstrip()) for line in file.read().split('\n')]

    incr = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            incr += 1

    print("Part1\nNumber of times a depth measurement increases: {}".format(incr))


def main_part2(window_size):
    with open('day1_input.txt', 'r') as file:
        lines = [int(line.rstrip()) for line in file.read().split('\n')]


    incr = 0
    prev = sum(lines[:window_size])
    for i in range(1, len(lines) - window_size + 1):
        cur = sum(lines[i:(i + window_size)])
        if cur > prev:
            incr += 1
        prev = cur

        

    print("Part2\nNumber of times a depth measurement increases: {}".format(incr))


if __name__ == "__main__":
    main()
    main_part2(3)