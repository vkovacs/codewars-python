# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python
import unittest


def duplicate_count(text):
    if len(text) == 0: return 0

    frequency = {}

    for char in text:
        char = char.lower()
        frequency[char] = frequency.get(char, 0) + 1

    duplicate_counter = 0
    for k, v in frequency.items():
        if v > 1: duplicate_counter += 1

    return duplicate_counter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(0, duplicate_count(""))
        self.assertEqual(0, duplicate_count("abcde"))
        self.assertEqual(1, duplicate_count("abcdeaa"))
        self.assertEqual(2, duplicate_count("abcdeaB"))
        self.assertEqual(2, duplicate_count("Indivisibilities"))


if __name__ == '__main__':
    unittest.main()
