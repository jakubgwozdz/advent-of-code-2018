import re

from day02 import Counter


class CounterOfCounters(dict):
    def __missing__(self, key):
        return Counter()


def read_input():
    with open('data/input4.txt') as f:
        lines = f.read().splitlines()
    return lines


regex1 = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}] Guard #(\d+) begins shift')
regex2 = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})] falls asleep')
regex3 = re.compile(r'\[\d{4}-\d{2}-\d{2} \d{2}:(\d{2})] wakes up')


def parse(i):
    i.sort()
    guards = CounterOfCounters()
    guard = 0
    asleep = 0
    for line in i:
        m1 = regex1.match(line)
        m2 = regex2.match(line)
        m3 = regex3.match(line)
        if m1:
            guard = int(m1.group(1))
        elif m2:
            asleep = int(m2.group(1))
        elif m3:
            awake = int(m3.group(1))
            guards_minutes = guards[guard]
            for m in range(asleep, awake):
                guards_minutes[m] += 1
            guards[guard] = guards_minutes
        else:
            print('invalid line `' + line + '`')
            exit(-1)
    return guards


def part1(i):
    guards = parse(i)

    max_guard = max(guards, key=lambda g: sum(guards[g].values()))
    max_minute = max(guards[max_guard], key=lambda m: guards[max_guard][m])
    return max_guard * max_minute


def part2(i):
    guards = parse(i)

    max_guard = max(guards, key=lambda g: guards[g][max(guards[g], key=lambda m: guards[g][m])])
    max_minute = max(guards[max_guard], key=lambda m: guards[max_guard][m])
    return max_guard * max_minute


def display(guards):
    print('{:>5}: '.format(''), end='')
    for m in range(0, 60):
        print('{:>3}'.format(m), end='')
    print()
    for g in guards:
        print('{:>5}: '.format(g), end='')
        for m in range(0, 60):
            print('{:>3}'.format(guards[g][m]), end='')
        print()


if __name__ == '__main__':
    print(part1(read_input()))
    print(part2(read_input()))
