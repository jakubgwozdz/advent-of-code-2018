from unittest import TestCase

from day01 import part1
from day01 import part2


class Test(TestCase):
    def test_part1(self):
        self.assertEqual(part1(), 585)

    def test_part2(self):
        self.assertEqual(part2(), 83173)
