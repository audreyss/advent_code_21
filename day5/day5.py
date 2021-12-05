import numpy as np


class Point(object):
    def __init__(self, list_coord):
        self.X = int(list_coord[0])
        self.Y = int(list_coord[1])

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)


def main(filename, size, diagonal_line=False):
    arr = np.zeros((size, size))

    with open(filename, 'r') as file:
        while line := file.readline().rstrip():
            points = line.split(' -> ')
            pt1 = Point(points[0].split(','))
            pt2 = Point(points[1].split(','))

            if pt1.X == pt2.X:
                # vertical line
                min_y, max_y = min([pt1.Y, pt2.Y]), max([pt1.Y, pt2.Y])
                arr[pt1.X, min_y:(max_y + 1)] += 1
            elif pt1.Y == pt2.Y:
                # horizontal line
                min_x, max_x = min([pt1.X, pt2.X]), max([pt1.X, pt2.X])
                arr[min_x:(max_x + 1), pt1.Y] += 1
            elif diagonal_line:
                # diagonal line
                down = pt1.X < pt2.X
                right = pt1.Y < pt2.Y
                x, y = pt1.X, pt1.Y
                # loop on each point of the line
                while x != pt2.X:
                    arr[x, y] += 1
                    x = (x + 1) if down else (x - 1)
                    y = (y + 1) if right else (y - 1)

                arr[x, y] += 1

    print("Number of points: {}".format(np.count_nonzero(arr > 1)))


if __name__ == "__main__":
    main('day5_input.txt', 1000)
    main('day5_input.txt', 1000, True)
    # 5442 et 19571
