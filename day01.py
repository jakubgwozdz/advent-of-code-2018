def process(current, line):
    if line[:1] == '+':
        return current + int(line[1:])
    elif line[:1] == '-':
        return current - int(line[1:])


if __name__ == '__main__':
    with open('data/input1.txt') as f:
        changes = f.read().splitlines()

    freq = 0
    for change in changes:
        freq = process(freq, change)

    print(freq)

    found = set()
    freq = 0
    index = 0
    while freq not in found:
        found.add(freq)
        freq = process(freq, changes[index])
        index = index + 1
        if index >= len(changes):
            index = 0

    print(freq)
