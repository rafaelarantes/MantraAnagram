import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from MantraAnagram import MantraAnagram
from collections import OrderedDict
from re import sub 


class MantraAnagramTests(unittest.TestCase):

    def testWordsEnglish(self):
        phrases = [
                    "I think this is good",
                    "I would like to go to Egypt",
                    "Peace is the solution for the world",
                    "We can't teleport yet"
                  ]

        mantra = MantraAnagram()
        for p in phrases:
            phrase = mantra.generate(p)

            self.assertEqual(len(list(phrase)), len(list("".join(OrderedDict.fromkeys(sub('[^a-z]+', '', p.lower().replace(" ", "")))))))

    def testWordsPortuguese(self):
        phrases = [
                    "Eu acho que isso é bom",
                    "Eu gostaria de ir ao egito",
                    "A paz é a solução para o mundo",
                    "Ainda não podemos nos teletransportar"
                  ]

        mantra = MantraAnagram()
        for p in phrases:
            phrase = mantra.generate(p)

            self.assertEqual(len(list(phrase)), len(list("".join(OrderedDict.fromkeys(sub('[^a-z]+', '', p.lower().replace(" ", "")))))))


if __name__ == '__main__':
    unittest.main()