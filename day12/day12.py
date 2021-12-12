def check_occ(visited):
    l_vertex = set(visited)
    for v in l_vertex:
        if v.islower() and visited.count(v) == 2:
            return True
    return False


def dfs(vertex, paths, end, visited, cur_path, nb_paths, double_allowed):
    if not double_allowed and vertex in visited and vertex.islower():
        return nb_paths
    if double_allowed and vertex in visited and vertex in ['start', 'end']:
        return nb_paths
    if double_allowed and vertex in visited and vertex.islower() and check_occ(visited) and vertex not in ['start', 'end']:
        return nb_paths

    visited.append(vertex)
    cur_path.append(vertex)
    if vertex == end:
        nb_paths += 1
    else:
        for child in paths[vertex]:
            nb_paths = dfs(child, paths, end, visited, cur_path, nb_paths, double_allowed)

    cur_path.pop()
    visited.remove(vertex)
    return nb_paths


def main(filename, double_allowed):
    with open(filename, 'r') as file:
        lines = [line.rstrip() for line in file.readlines()]

    paths = {}
    for line in lines:
        split = line.split('-')
        if split[0] in paths:
            paths[split[0]].append(split[1])
        else:
            paths[split[0]] = [split[1]]
        if split[1] in paths:
            paths[split[1]].append(split[0])
        else:
            paths[split[1]] = [split[0]]

    print(dfs('start', paths, 'end', [], [], 0, double_allowed))


if __name__ == "__main__":
    main('day12_input.txt', False)
    main('day12_input.txt', True)
