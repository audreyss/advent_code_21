def main(filename):
    with open(filename, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]

    open_matching = {'(': ')', '[': ']', '{': '}', '<': '>'}
    char_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    s, completion_str = 0, []
    for line in lines:
        stack, corrupted = [], False

        for c in line:
            if c in open_matching:
                stack.append(c)
                continue
            if open_matching[stack[-1]] != c:
                s += char_points[c]
                corrupted = True
                break
            stack.pop(-1)

        if not corrupted:
            match = [open_matching[c] for c in stack]
            match.reverse()
            completion_str.append("".join(match))

    print("Total syntax error: %s" % s)

    char_points_p2 = {')': 1, ']': 2, '}': 3, '>': 4}
    scores_pt2 = []
    for st in completion_str:
        score = 0
        for c in st:
            score = score * 5 + char_points_p2[c]
        scores_pt2.append(score)
    scores_pt2.sort()
    print("Middle score: %s" % scores_pt2[len(scores_pt2) // 2])


if __name__ == "__main__":
    main('day10_input.txt')
