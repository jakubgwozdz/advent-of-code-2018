def process(current, line):
    if line[:1] == '+':
        return current + int(line[1:])
    elif line[:1] == '-':
        return current - int(line[1:])


def read_input():
    with open('data/input1.txt') as f:
        lines = f.read().splitlines()
    return lines


def part1(changes):
    freq = 0
    for change in changes:
        freq = process(freq, change)
    return freq


def part2(changes):
    found = set()
    freq = 0
    index = 0
    while freq not in found:
        found.add(freq)
        freq = process(freq, changes[index])
        index = index + 1
        if index >= len(changes):
            index = 0
    return freq


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
