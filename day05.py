from collections import deque


def read_input():
    with open('data/input5.txt') as f:
        lines = f.read().splitlines()
    return lines


def react(line, *, ignore=''):
    stack = deque()
    for i in line:
        if i.lower() == ignore:
            pass
        if len(stack) == 0:
            stack.append(i)
        else:
            ii = stack.pop()
            if i.lower() != ii.lower() or i == ii:
                stack.append(ii)
                stack.append(i)
    return stack


def part1(lines):
    return len(react(lines[0]))


def part2(lines):
    line = lines[0]
    stacks = dict()
    for i in line:
        if i.lower() not in stacks:
            stacks[i.lower()] = deque()
    line = react(line)
    for c in stacks:
        for i in line:
            if i.lower() == c:
                pass
            elif len(stacks[c]) == 0:
                stacks[c].append(i)
            else:
                ii = stacks[c].pop()
                if i.lower() != ii.lower() or i == ii:
                    stacks[c].append(ii)
                    stacks[c].append(i)
    return len(min(stacks.values(), key=lambda k: len(k)))


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
