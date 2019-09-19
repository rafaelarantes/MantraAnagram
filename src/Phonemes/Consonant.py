from string import ascii_lowercase
from Phonemes.AbstractPhoneme import AbstractPhoneme
from Phonemes.Vowel import Vowel
from Phonemes.Suffix import Suffix

consonants = list(filter(lambda x : x not in Vowel.getVowels() + Suffix.getSuffixes(), ascii_lowercase))
class Consonant(AbstractPhoneme):

    def _setProperties(self, phrase_letters):
        self.exists_vowel_yet = len([i for i in phrase_letters if i in Vowel.getVowels()]) > 0

    def _add(self, diagram_letters):
        if self.exists_vowel_yet:
            diagram_letters.append(self.value)
        else:
            diagram_letters.insert(self.__getVowelIndexNeverUsed(diagram_letters), self.value)

    def __getVowelIndexNeverUsed(self, diagram_letters):
        vowels_in_diagram_letters = [i for i in diagram_letters if i in Vowel.getVowels()]
        for vowel in vowels_in_diagram_letters:
            vowel_index = diagram_letters.index(vowel)
            if self.__valueOfIndexAfterVowelIsVowel(diagram_letters, vowel_index, 1) or self.__valueOfIndexAfterVowelIsVowel(diagram_letters, vowel_index, 2):
                return vowel_index+1

        return len(diagram_letters)
    
    def __valueOfIndexAfterVowelIsVowel(self, diagram_letters, vowel_index, next_index):
        if diagram_letters[vowel_index+next_index : vowel_index+next_index+1] == []:
            return True

        return len([i for i in diagram_letters[vowel_index+next_index : vowel_index+next_index+1] if i in Vowel.getVowels()]) > 0
    
    def _getFromList(self, phrase_letters):
        return list(filter(lambda x : x in consonants, phrase_letters))

    @staticmethod
    def getConsonants():
        return consonants

