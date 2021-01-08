from collections import deque


def read_input():
    with open('data/input5.txt') as f:
        lines = f.read().splitlines()
    return lines


def react(line):
    stack = deque()
    for i in line:
        if len(stack) == 0:
            stack.append(i)
        else:
            ii = stack.pop()
            if i.lower() != ii.lower() or i == ii:
                stack.append(ii)
                stack.append(i)
    return len(stack)


def part1(lines):
    return react(lines[0])


def part2(lines):
    line = lines[0]
    letters = []
    for i in line:
        if i.lower() not in letters:
            letters.append(i.lower())
    lengths = []
    for i in letters:
        line2 = line.replace(i, '').replace(i.upper(), '')
        length = react(line2)
        print("'{}' - {}".format(i, length))
        lengths.append(length)
    return min(lengths)


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
