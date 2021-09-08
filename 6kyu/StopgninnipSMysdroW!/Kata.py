# https://www.codewars.com/kata/5264d2b162488dc400000001
import unittest


def spin_words(sentence):
    words = sentence.split(" ")

    reversed_sentence = ""

    for word in words:
        if len(word) >= 5:
            reversed_sentence += word[::-1] + " "
        else:
            reversed_sentence += word + " "

    return reversed_sentence[:-1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual("Hey wollef sroirraw", spin_words("Hey fellow warriors"))
        self.assertEqual("This is a test", spin_words("This is a test"))
        self.assertEqual("This is rehtona test", spin_words("This is another test"))


if __name__ == '__main__':
    unittest.main()
