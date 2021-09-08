# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python
import unittest

import re


def disemvowel(sentence):
    return re.sub('(?i)[aeiou]', '', sentence)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('LL', disemvowel('AaLOL'))  # add assertion here


if __name__ == '__main__':
    unittest.main()
