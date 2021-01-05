from unittest import TestCase

from day03 import part1, part2, read_input


class Test(TestCase):

    def test_example1(self):
        claims = """\
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
""".splitlines()
        self.assertEqual(part1(claims), 4)

    def test_part1(self):
        self.assertEqual(part1(read_input()), 104241)

    def test_example2(self):
        claims = """\
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
""".splitlines()
        self.assertEqual(part2(claims), 3)

    def test_part2(self):
        self.assertEqual(part2(read_input()), 806)
