from collections import deque

from day02 import Counter


def read_input():
    with open('data/input6.txt') as f:
        lines = f.read().splitlines()
    return lines


def parse(line):
    ax, ay = line.split(',')
    return int(ax), int(ay)


def extend(r, v):
    if v in r:
        return r
    elif v < r.start:
        return range(v, r.stop)
    elif v >= r.stop:
        return range(r.start, v + 1)


def part1(lines):
    coords = [parse(line) for line in lines]
    (x0, y0) = next(iter(coords))
    range_x = range(x0, x0 + 1)
    range_y = range(y0, y0 + 1)
    for c in coords:
        (x, y) = c
        range_x = extend(range_x, x)
        range_y = extend(range_y, y)

    print("x: {}, y: {}".format(range_x, range_y))
    counter = Counter()

    queue = deque()
    dists = {}

    for c in coords:
        queue.append(c)
        dists[c] = (0, {c})

    while len(queue) > 0:

        c = queue.popleft()
        root = dists[c]
        (x, y) = c
        if x in range_x:
            process((x + 1, y), root, dists, queue)
            process((x - 1, y), root, dists, queue)
        if y in range_y:
            process((x, y + 1), root, dists, queue)
            process((x, y - 1), root, dists, queue)

    print("finished with queue")

    for x in range_x:
        for y in range_y:
            (_, closest) = dists[(x, y)]
            if len(closest) == 1:
                counter[next(iter(closest))] += 1

    print("calculated area")
    print(counter)

    for x in range_x:
        cleanup_infinities((x, range_y.start), counter, dists)
        cleanup_infinities((x, range_y.stop - 1), counter, dists)
    for y in range_y:
        cleanup_infinities((range_x.start, y), counter, dists)
        cleanup_infinities((range_x.stop - 1, y), counter, dists)

    return counter[max(counter, key=lambda v: counter[v])]


def cleanup_infinities(c, counter, dists):
    (_, closest) = dists[c]
    if len(closest) == 1:
        counter[next(iter(closest))] = 0


def process(c1, root, distances, queue):
    (d, rs) = root
    if d < 0:
        return
    (d1, rs1) = v1 = (d + 1, rs)
    if c1 in distances:
        (d0, rs0) = distances[c1]
        if d0 < d1:
            pass
        elif d0 > d1:
            pass
        elif rs0 == rs:
            pass
        else:
            distances[c1] = (d0, rs0 | rs)
    else:
        distances[c1] = v1
        queue.append(c1)


def part2(i):
    pass


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
