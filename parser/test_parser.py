import unittest
from .parser import parse

def sort(unsorted_list: list):
    """
    Recursively sort list of lists
    """
    for elem in unsorted_list:
        if isinstance(elem, list):
            sort(elem)

class TestParser(unittest.TestCase):
    def test_no_nests(self):
        string = "a b c d e"
        expected = sort(["a", "b", "c", "d", "e"])
        parsed = sort(parse(string))
        self.assertEqual(parsed, expected)

    def test_nested(self):
        # Case 1
        string = "a b (c d e)"
        expected = sort(["a", "b", ["c", "d", "e"]])
        parsed = sort(parse(string))
        self.assertEqual(parsed, expected)

        # Case 2
        string = "a (b) c (d e)"
        expected = sort(["a", ["b"], "c", ["d", "e"]])
        parsed = sort(parse(string))
        self.assertEqual(parsed, expected)

        # Case 3
        string = "a ((b) c) (d e)"
        expected = sort(["a", [["b"], "c"], ["d", "e"]])
        parsed = sort(parse(string))
        self.assertEqual(parsed, expected)
