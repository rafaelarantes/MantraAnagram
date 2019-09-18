import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from MantraAnagram import MantraAnagram
from TextUtils import TextUtils


class MantraAnagramTests(unittest.TestCase):
    
    def testWordsEnglish(self):
        phrases = [
                    'I think this is good',
                    'I would like to go to Egypt',
                    'Peace is the solution for the world',
                    'We can\'t teleport yet'
                  ]

        mantra = MantraAnagram()
        for p in phrases:
            phrase = mantra.generate(p)

            p = TextUtils.RemoveSpecialCharacters(p)
            p = TextUtils.RemoveDuplicateCharacters(p)

            self.assertEqual(len(list(phrase)), len(list(p)))

    def testWordsPortuguese(self):
        phrases = [
                    'Eu acho que isso é bom',
                    'Eu gostaria de ir ao egito',
                    'A paz é a solução para o mundo',
                    'Ainda não podemos nos teletransportar'
                  ]

        mantra = MantraAnagram()
        for p in phrases:
            phrase = mantra.generate(p)

            p = TextUtils.RemoveSpecialCharacters(p)
            p = TextUtils.RemoveDuplicateCharacters(p)

            self.assertEqual(len(list(phrase)), len(list(p)))
    
    def testSmallWords(self):
        phrases = [
                'hi',
                'oi',
                'hello',
                'alô',
                'olá',
                'good'
            ]

        mantra = MantraAnagram()
        for p in phrases:
            phrase = mantra.generate(p)

            p = TextUtils.RemoveSpecialCharacters(p)
            p = TextUtils.RemoveDuplicateCharacters(p)

            self.assertEqual(len(list(phrase)), len(list(p)))        

    def testWordsWithSothingATypeOfCharacter(self):
        phrases = [
                'aa',
                'bb',
                'scsc',
            ]

        mantra = MantraAnagram()
        for p in phrases:
            phrase = mantra.generate(p)

            p = TextUtils.RemoveSpecialCharacters(p)
            p = TextUtils.RemoveDuplicateCharacters(p)

            self.assertEqual(len(list(phrase)), len(list(p)))
    

if __name__ == '__main__':
    unittest.main()