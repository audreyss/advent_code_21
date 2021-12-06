def main(filename, nb_days):
    with open(filename, 'r') as file:
        list_fish = [int(elt) for elt in file.readline().rstrip().split(',')]

    timers = {timer: list_fish.count(timer) for timer in set(list_fish)}

    for i in range(nb_days):
        nb_new_fish = timers[0] if 0 in timers.keys() else 0
        timers = {(timer - 1): timers[timer] for timer in timers.keys() if timer != 0}
        timers[6] = (timers[6] + nb_new_fish) if 6 in timers.keys() else nb_new_fish
        timers[8] = nb_new_fish

    print('Number of fish after %s days: %s' % (nb_days, sum(timers.values())))


if __name__ == "__main__":
    main('day6_input.txt', 80)
    main('day6_input.txt', 256)

