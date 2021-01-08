from unittest import TestCase

from day05 import part1, part2, read_input


class Test(TestCase):

    def test_example1(self):
        i = 'dabAcCaCBAcCcaDA'.splitlines()
        self.assertEqual(10, part1(i))

    def test_part1(self):
        self.assertEqual(10564, part1(read_input()))

    def test_example2(self):
        i = 'dabAcCaCBAcCcaDA'.splitlines()
        self.assertEqual(4, part2(i))

    def test_part2(self):
        self.assertEqual(6336, part2(read_input()))
