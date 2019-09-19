from random import shuffle
from Phonemes.Consonant import Consonant
from Phonemes.Digraph import Digraph
from Phonemes.Vowel import Vowel
from Phonemes.Suffix import Suffix

phonemes_names = [Consonant.__name__, Digraph.__name__, Suffix.__name__, Vowel.__name__]
class PhonemesFactory:
    
    def getPhonemes(self):
        phonemes_class = []
        shuffle(phonemes_names)
        for phoneme_name in phonemes_names:
            phonemes_class.append(globals()[phoneme_name])
        
        return phonemes_class
    
    def getVowel(self):
        return Vowel

            



