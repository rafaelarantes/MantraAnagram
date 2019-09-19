import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Phonemes.Suffix import Suffix

class SufixTests(unittest.TestCase):
    
    def testGetDigraphFromLetters(self):
        letters = ['r']
        sufix = Suffix(letters)
        letter = sufix.getValue()

        self.assertEqual(True, letter in sufix.getSuffixes())

    def testAddToList(self):
        final_letters = []
        letters = ['s']
        sufix = Suffix(letters)
        sufix.addToList(final_letters)

        self.assertEqual(True, len(final_letters) > 0 and final_letters[0] in sufix.getSuffixes())

    def testAddEmptyValueToList(self):
        final_letters = []
        letters = []
        sufix = Suffix(letters)
        sufix.addToList(final_letters)

        self.assertEqual(True, len(final_letters) == 0)

    def testWhenHasOthersTypesOfPhonemes(self):
        letters = ['u', 'c', 'y', 'o', 'l', 'j', 'i', 'b', 'r', 'e', 'z', 'a', 'f', 'g', 'h']
        sufix = Suffix(letters)
        letter = sufix.getValue()

        self.assertEqual('', letter)

if __name__ == '__main__':
    unittest.main()