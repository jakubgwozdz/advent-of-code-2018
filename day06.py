from day02 import Counter


def read_input():
    with open('data/input6.txt') as f:
        lines = f.read().splitlines()
    return lines


def parse(line):
    ax, ay = line.split(',')
    return int(ax), int(ay)


def part1(lines):
    coords = list(parse(line) for line in lines)
    for c in coords:
        print(c)
    # list(map(lambda line: list(map(lambda d: int(d), line.split(','))), lines))
    min_x = min(coords, key=lambda k: k[0])[0]
    min_y = min(coords, key=lambda k: k[1])[1]
    max_x = max(coords, key=lambda k: k[0])[0]
    max_y = max(coords, key=lambda k: k[1])[1]
    print("x: {}-{}, y: {}-{}".format(min_x, max_x, min_y, max_y))
    counter = Counter()

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            distances = iter((c, dist(c, (x, y))) for c in coords)
            min_dist = min(distances, key=lambda c: c[1])
            if not any(filter(lambda c: c[1] == min_dist[1] and c != min_dist, distances)):
                counter[tuple(min_dist[0])] += 1

    for x in range(min_x, max_x):
        min_dist = min(((c, dist(c, (x, min_y - 1))) for c in coords), key=lambda c: c[1])
        counter[tuple(min_dist[0])] = 0
        min_dist = min(((c, dist(c, (x, max_y + 1))) for c in coords), key=lambda c: c[1])
        counter[tuple(min_dist[0])] = 0
    for y in range(min_y, max_y):
        min_dist = min(((c, dist(c, (min_x - 1, y))) for c in coords), key=lambda c: c[1])
        counter[tuple(min_dist[0])] = 0
        min_dist = min(((c, dist(c, (max_x + 1, y))) for c in coords), key=lambda c: c[1])
        counter[tuple(min_dist[0])] = 0

    return counter[max(counter, key=lambda c: counter[c])]


def dist(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2
    return abs(x1 - x2) + abs(y1 - y2)


def part2(i):
    pass


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
