import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Phonemes.Digraph import Digraph

class DigraphsTests(unittest.TestCase):
    
    def testGetDigraphFromLetters(self):
        letters = ['u', 'c', 'y', 'o', 'l', 'j', 'i', 'b', 'r', 'e', 'z', 'a', 'f', 'g', 'h']
        digraph = Digraph(letters)
        letter = digraph.getValue()

        self.assertEqual(True, letter in digraph.getDigraphs())

    def testAddToList(self):
        final_letters = []
        letters = ['u', 'c', 'y', 'o', 'l', 'j', 'i', 'b', 'r', 'e', 'z', 'a', 'f', 'g', 'h']
        digraph = Digraph(letters)
        digraph.addToList(final_letters)

        self.assertEqual(True, len(final_letters) > 0 and final_letters[0] in digraph.getDigraphs())

    def testAddEmptyValueToList(self):
        final_letters = []
        letters = []
        digraph = Digraph(letters)
        digraph.addToList(final_letters)

        self.assertEqual(True, len(final_letters) == 0)

if __name__ == '__main__':
    unittest.main()