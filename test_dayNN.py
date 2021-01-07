from unittest import TestCase

from dayNN import part1, part2, read_input


class Test(TestCase):

    def test_example1(self):
        i = """\
""".splitlines()
        self.assertEqual(None, part1(i))

    def test_part1(self):
        self.assertEqual(None, part1(read_input()))

    def test_example2(self):
        i = """\
""".splitlines()
        self.assertEqual(None, part2(i))

    def test_part2(self):
        self.assertEqual(None, part2(read_input()))
