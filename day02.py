class Counter(dict):
    def __missing__(self, key):
        return 0


def read_input():
    with open('data/input2.txt') as f:
        lines = f.read().splitlines()
    return lines


def part1():
    boxes = read_input()
    twos = 0
    threes = 0
    for box in boxes:
        chars = Counter()
        for c in box:
            chars[c] += 1
        if any(v == 2 for v in chars.values()):
            twos += 1
        if any(v == 3 for v in chars.values()):
            threes += 1

    return twos * threes


def part2():
    boxes = read_input()
    for box1 in boxes:
        for box2 in boxes:
            c = 0
            i = 0
            while i < len(box1):
                if box1[i] != box2[i]:
                    c += 1
                i += 1
                if c > 1:
                    break
            if c == 1:
                i = 0
                r = ''
                while i < len(box1):
                    if box1[i] == box2[i]:
                        r += box1[i]
                    i += 1
                return r


if __name__ == '__main__':
    print(part1())
    print(part2())
