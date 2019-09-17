#from .LetterUtils import LetterUtils
from random import shuffle
from Phonemes.Consonant import Consonant
from Phonemes.Digraph import Digraph
from Phonemes.Vowel import Vowel
from Phonemes.Suffix import Suffix

class PhonemesFactory:
  
    b =  """def __moveFirstLetterPhonemeForList(self, phonemes, letters):
        if len(phonemes) > 0:
            letters.append(phonemes[0])
            phonemes = LetterUtils.removeLetters([phonemes[0]], phonemes)
        return phonemes

    def __moveFirstLetterPhonemeForListByIndex(self, phonemes, letters, index):
        if len(phonemes) > 0:
            letters.insert(index, phonemes[0])
            phonemes = LetterUtils.removeLetters([phonemes[0]], phonemes)

        return phonemes
        

    def __valueOfListContainsInAnotherList(self, first_list, second_list):
        return len([i for i in first_list if i in second_list]) > 0

    def __getFirstUnsedVowelInList(self, vowelsNotUsedYet, letters):
        for vowel in range(0, len(vowelsNotUsedYet)):
            if vowelsNotUsedYet[vowel] in letters and letters.index(vowelsNotUsedYet[vowel]) < len(letters):
                return vowelsNotUsedYet[vowel]
        
        return None
    
    def __lastElementOfListIsVowel(self, letters):
        return letters[len(letters)-1] in ['a', 'e', 'i', 'o', 'u']


    def addEndConsonants(self, ending_consonants, letters):
        vowelsNotUsedYet = ['a', 'e', 'i', 'o', 'u']

        while len(ending_consonants) > 0:
            if not self.__lastElementOfListIsVowel(letters) and self.__valueOfListContainsInAnotherList(vowelsNotUsedYet, letters):
                vowelNotUsedYet = self.__getFirstUnsedVowelInList(vowelsNotUsedYet, letters)

                if vowelNotUsedYet is not None:
                    self.__moveFirstLetterPhonemeForListByIndex(ending_consonants, letters, letters.index(vowelNotUsedYet) + 1)
                    vowelsNotUsedYet.remove(vowelNotUsedYet) 
            else:
                ending_consonants = self.__moveFirstLetterPhonemeForList(ending_consonants, letters)

    def addRemainingVowels(self, vowels, letters):
        while len(vowels) > 0:
            if len(letters) > 0 and self.__lastElementOfListIsVowel(letters):
                self.__moveFirstLetterPhonemeForListByIndex(vowels, letters, 0)
            else:
                self.__moveFirstLetterPhonemeForList(vowels, letters)"""


    def addPhonemes(self, diagram_letters, letters):
        phonemes_names = [Consonant.__name__, Digraph.__name__, Suffix.__name__, Vowel.__name__]
        
        while len(letters) > 0:
            shuffle(phonemes_names)
            for phoneme_name in phonemes_names:
                self.__addPhonemeToList(phoneme_name, diagram_letters, letters, Vowel.__name__)


    def __addPhonemeToList(self, phoneme_name, phonemes, letters, next_phoneme_name = None):
        next_phoneme = None
        phoneme_class = globals()[phoneme_name]

        if next_phoneme_name is not None:
            next_phoneme = globals()[next_phoneme_name]

        phoneme = phoneme_class(letters, next_phoneme(letters))
        phoneme.addToList(phonemes)

    e = """def addDigraphConsonantVowel(self, digraphs, consonants, vowels, letters):
        vowelsNotUsedYet = ['a', 'e', 'i', 'o', 'u']
        consonants_first = True

        while(len(digraphs) > 0 or len(consonants) > 0):
            if not consonants_first and len(digraphs) > 0:
                digraphs = self.addDigraph(digraphs, letters)
                vowels = self.addVowel(vowels, letters)

            elif len(consonants) > 0:
                if len(vowels) > 0:
                    consonants = self.addConsonant(consonants, letters)
                else:
                    vowelNotUsedYet = self.__getFirstUnsedVowelInList(vowelsNotUsedYet, letters)
                    
                    if vowelNotUsedYet is not None:
                        self.__moveFirstLetterPhonemeForListByIndex(consonants, letters, letters.index(vowelNotUsedYet) + 1)
                        vowelsNotUsedYet.remove(vowelNotUsedYet)
                    else:
                        consonants = self.addConsonant(consonants, letters)

                if len(vowels) > 0:
                    vowels = self.addVowel(vowels, letters)
            
            consonants_first = False
        
        return digraphs, consonants, vowels
    """