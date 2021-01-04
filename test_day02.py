from unittest import TestCase

from day02 import part1
from day02 import part2


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(part1(), 5478)

    def test_part2(self):
        self.assertEqual(part2(), 'qyzphxoiseldjrntfygvdmanu')
