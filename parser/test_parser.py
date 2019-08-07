import unittest
from .parser import parse

class TestParser(unittest.TestCase):
    def test_no_nests(self):
        string = "a b c d e"
        expected = ["a", "b", "c", "d", "e"]
        parsed = parse(string)
        self.assertEqual(parsed, expected)

    def test_nested(self):
        # Case 1
        string = "a b (c d e)"
        expected = [['c', 'd', 'e'], 'a', 'b']
        parsed = parse(string)
        self.assertEqual(parsed, expected)

        # Case 2
        string = "a (b) c (d e)"
        expected = [['b'], ['d', 'e'], 'a', 'c']
        parsed = parse(string)
        self.assertEqual(parsed, expected)

        # Case 3
        string = "a ((b) c) (d e)"
        expected = [[['b'], 'c'], ['d', 'e'], 'a']
        parsed = parse(string)
        self.assertEqual(parsed, expected)

        # Case 4 - Cannot parse
        string = ") a b ("
        with self.assertRaises(ValueError) as ctx:
            parse(string)
