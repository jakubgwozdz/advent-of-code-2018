import re


class Lists(dict):
    def __missing__(self, key):
        return []


def read_input():
    with open('data/input7.txt') as f:
        lines = f.read().splitlines()
    return lines


input_regex = re.compile(r'Step (\w) must be finished before step (\w) can begin\.')


def part1(lines):
    dependencies = Lists()
    dependants = Lists()
    result = ""
    for line in lines:
        (a, b) = input_regex.match(line).groups()
        dependants[a] += b
        dependants[b] = dependants[b]
        dependencies[b] += a
        dependencies[a] = dependencies[a]

    while len(dependencies):
        c = min(filter(lambda key: len(dependencies[key]) == 0, dependencies))
        result += c
        dependencies.pop(c)
        for v in dependants[c]:
            dependencies[v].remove(c)
    return result


def part2(i):
    pass


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
