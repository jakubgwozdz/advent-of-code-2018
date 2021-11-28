from unittest import TestCase

from day07 import part1, part2, read_input


class Test(TestCase):

    def test_example1(self):
        i = """\
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".splitlines()
        self.assertEqual("CABDFE", part1(i))

    def test_part1(self):
        self.assertEqual("GJFMDHNBCIVTUWEQYALSPXZORK", part1(read_input()))

    def test_example2(self):
        i = """\
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".splitlines()
        self.assertEqual(None, part2(i))

    def test_part2(self):
        self.assertEqual(None, part2(read_input()))
