import re

from day02 import Counter


def read_input():
    with open('data/input3.txt') as f:
        lines = f.read().splitlines()
    return lines


regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')


def overlapping(claims):
    counter = Counter()
    for claim in claims:
        (n, x, y, w, h) = map(lambda v: int(v), regex.match(claim).groups())
        for x1 in range(x, x + w):
            for y1 in range(y, y + h):
                counter[(x1, y1)] += 1
    return counter


def part1(claims):
    counter = overlapping(claims)
    return len(list(filter(lambda v: v > 1, counter.values())))


def part2(claims):
    counter = overlapping(claims)
    for claim in claims:
        (n, x, y, w, h) = map(lambda v: int(v), regex.match(claim).groups())
        single = True
        for x1 in range(x, x + w):
            for y1 in range(y, y + h):
                if counter[(x1, y1)] > 1:
                    single = False
        if single:
            return n


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
