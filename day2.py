def main(filename):
    with open(filename, 'r') as file:
        commands = [line.rstrip() for line in file.read().split('\n')]
    
    horizontal, depth = (0, 0)
    for cmd in commands:
        cmd = cmd.split(' ')
        if cmd[0] == 'forward':
            horizontal += int(cmd[1])
        elif cmd[0] == 'down':
            depth += int(cmd[1])
        else:
            depth -= int(cmd[1])

    print("Part1\nMultiplication: {}".format(horizontal*depth))


def main_part2(filename):
    with open(filename, 'r') as file:
        commands = [line.rstrip() for line in file.read().split('\n')]
    
    horizontal, depth, aim = (0, 0, 0)
    for cmd in commands:
        cmd = cmd.split(' ')
        if cmd[0] == 'forward':
            horizontal += int(cmd[1])
            depth += aim * int(cmd[1])
        elif cmd[0] == 'down':
            aim += int(cmd[1])
        else:
            aim -= int(cmd[1])

    print("Part2\nMultiplication: {}".format(horizontal*depth))


if __name__ == "__main__":
    main('day2_input.txt')
    main_part2('day2_input.txt')
