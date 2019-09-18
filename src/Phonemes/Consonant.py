from Phonemes.AbstractPhoneme import AbstractPhoneme
from Phonemes.Vowel import Vowel
from Phonemes.Suffix import Suffix


class Consonant(AbstractPhoneme):

    def setProperties(self, letters):
        self.exists_vowel_yet = len([i for i in letters if i in Vowel.getVowels()]) > 0
        self.index_vowel_never_used = self.__getVowelIndexNeverUsed(letters)

    def __getVowelIndexNeverUsed(self, letters):
        vowels_in_letters = [i for i in letters if i in Vowel.getVowels()]
        for v in vowels_in_letters:
            i = letters.index(v)
            if letters[i+1 : i+1] in Vowel.getVowels():
                return i+1
            elif letters[i+2 : i+2] in Vowel.getVowels():
                return i+2
        
        return len(letters)-1

    def add(self, phonemes):
        if self.exists_vowel_yet:
            phonemes.append(self.value)
        else:
            phonemes.insert(self.index_vowel_never_used, self.value)

    
    def getFromList(self, phonemes):
        return list(filter(lambda x : x not in Vowel.getVowels() + Suffix.getSuffixes(), phonemes))

