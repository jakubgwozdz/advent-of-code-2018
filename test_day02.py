from unittest import TestCase

from day02 import part1, part2, read_input


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(part1(read_input()), 5478)

    def test_part2(self):
        self.assertEqual(part2(read_input()), 'qyzphxoiseldjrntfygvdmanu')
