from string import ascii_lowercase
from Phonemes.AbstractPhoneme import AbstractPhoneme
from Phonemes.Vowel import Vowel
from Phonemes.Suffix import Suffix

consonants = list(filter(lambda x : x not in Vowel.getVowels() + Suffix.getSuffixes(), ascii_lowercase))
class Consonant(AbstractPhoneme):

    def _setProperties(self, letters):
        self.exists_vowel_yet = len([i for i in letters if i in Vowel.getVowels()]) > 0

    def __getVowelIndexNeverUsed(self, letters):
        vowels_in_letters = [i for i in letters if i in Vowel.getVowels()]
        for v in vowels_in_letters:
            i = letters.index(v)
            if (len([i for i in letters[i+1 : i+2] if i in Vowel.getVowels()]) > 0) or letters[i+2 : i+3] == [] or len([i for i in letters[i+2 : i+3] if i in Vowel.getVowels()]) > 0:
                return i+1

        return len(letters)

    def _add(self, phonemes):
        if self.exists_vowel_yet:
            phonemes.append(self.value)
        else:
            phonemes.insert(self.__getVowelIndexNeverUsed(phonemes), self.value)

    
    def _getFromList(self, phonemes):
        return list(filter(lambda x : x in consonants, phonemes))

    @staticmethod
    def getConsonants():
        return consonants

