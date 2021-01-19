from unittest import TestCase

from day06 import part1, part2, read_input


class Test(TestCase):

    def test_example1(self):
        i = """\
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
""".splitlines()
        self.assertEqual(17, part1(i))

    def test_part1(self):
        self.assertEqual(3933, part1(read_input()))

    def test_example2(self):
        i = """\
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
""".splitlines()
        self.assertEqual(16, part2(i, 32))

    def test_part2(self):
        self.assertEqual(41145, part2(read_input()))
