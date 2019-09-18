from Phonemes.AbstractPhoneme import AbstractPhoneme

vowels = ['a', 'e', 'i', 'o', 'u']
suffix = ['r','s']
class Consonant(AbstractPhoneme):

    def setProperties(self, letters):
        self.exists_vowel_yet = len([i for i in letters if i in vowels]) > 0
        self.index_vowel_never_used = self.__getVowelIndexNeverUsed(letters)

    def __getVowelIndexNeverUsed(self, letters):
        vowels_in_letters = [i for i in letters if i in vowels]
        for v in vowels_in_letters:
            i = letters.index(v)
            if letters[i+1 : i+1] in vowels:
                return i+1
            elif letters[i+2 : i+2] in vowels:
                return i+2
        
        return len(letters)-1

        

    def add(self, phonemes):
        if self.exists_vowel_yet:
            phonemes.append(self.value)
        else:
            phonemes.insert(self.index_vowel_never_used, self.value)

    
    def getFromList(self, phonemes):
        return list(filter(lambda x : x not in vowels + suffix, phonemes))

