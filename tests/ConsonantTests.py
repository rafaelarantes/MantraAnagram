import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from Phonemes.Consonant import Consonant

class ConsonantTests(unittest.TestCase):
    
    def testGetConsonantFromLetters(self):
        letters = ['u', 'c', 'y', 'o', 'l', 'j', 'i', 'b', 'r', 'e', 'z', 'a', 'f']
        consonant = Consonant(letters)
        letter = consonant.getValue()

        self.assertEqual(True, letter in Consonant.getConsonants())

    def testAddToList(self):
        final_letters = []
        letters = ['a', 'b', 'c', 'd', 'e', 'f']
        consonant = Consonant(letters)
        consonant.addToList(final_letters)

        self.assertEqual(True, len(final_letters) > 0 and final_letters[0] in consonant.getConsonants())

    def testAddEmptyValueToList(self):
        final_letters = []
        letters = []
        consonant = Consonant(letters)
        consonant.addToList(final_letters)

        self.assertEqual(True, len(final_letters) == 0)

    def testAddInFirstIndexVowelNeverUsedWhenNoHasMoreVowel(self):
        letters = ['g']
        final_letters = ['w', 'h', 'i', 't', 'e']
        consonant = Consonant(letters)
        consonant.addToList(final_letters)

        self.assertEqual(''.join(['w', 'h', 'i', 'g' 't', 'e']), ''.join(final_letters))
 
    def testAddInSecondIndexVowelNeverUsedWhenNoHasMoreVowel(self):
        letters = ['f']
        final_letters = ['l', 'i', 'g', 'h', 't', 's', 'h', 'o', 't']
        consonant = Consonant(letters)
        consonant.addToList(final_letters)

        self.assertEqual(''.join(['l', 'i', 'g', 'h', 't', 's', 'h', 'o', 'f' 't']), ''.join(final_letters))
 

    def testAddInLastPositionWhenNoHasMoreVowelAndNoHasMoreVowelNerverUsed(self):
        letters = ['g']
        final_letters = ['v', 'i', 'c', 't', 'o', 'r', 'y']
        consonant = Consonant(letters)
        consonant.addToList(final_letters)

        self.assertEqual(''.join(['v', 'i', 'c', 't', 'o', 'r', 'y', 'g']), ''.join(final_letters))


if __name__ == '__main__':
    unittest.main()