import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Phonemes.Vowel import Vowel

class VowelTests(unittest.TestCase):
    
    def testGetVowelFromLetters(self):
        letters = ['u', 'c', 'y', 'o', 'l', 'j', 'i', 'b', 'r', 'e', 'z', 'a', 'f']
        vowel = Vowel(letters)
        letter = vowel.getValue()

        self.assertEqual(True, letter in vowel.getVowels())

    def testAddToList(self):
        final_letters = []
        letters = ['a', 'b', 'c', 'd', 'e', 'f']
        vowel = Vowel(letters)
        vowel.addToList(final_letters)

        self.assertEqual(True, len(final_letters) > 0 and final_letters[0] in Vowel.getVowels())

    def testAddEmptyValueToList(self):
        final_letters = []
        letters = []
        vowel = Vowel(letters)
        vowel.addToList(final_letters)

        self.assertEqual(True, len(final_letters) == 0)

    def testAddVowelInFirstPositionWhenLastElementIsVowel(self):
        final_letters = ["c", "o", "r", "e"]
        letters = ["i"]
        vowel = Vowel(letters)
        vowel.addToList(final_letters)

        self.assertEqual(''.join(["i", "c", "o", "r", "e"]), ''.join(final_letters))       

if __name__ == '__main__':
    unittest.main()