from Phonemes.AbstractPhoneme import AbstractPhoneme

vowels = ['a', 'e', 'i', 'o', 'u']
class Vowel(AbstractPhoneme):
    
    def _setProperties(self, phrase_letters):
        self.next_phoneme = None

    def _add(self, diagram_letters):
        if self.__lastElementOfListIsVowel(diagram_letters):
            diagram_letters.insert(0, self.value)
        else:
            diagram_letters.append(self.value)

    def __lastElementOfListIsVowel(self, diagram_letters):
        if len(diagram_letters) > 0:
            return diagram_letters[len(diagram_letters)-1] in vowels
        
        return False            

    def _getFromList(self, phrase_letters):
        return list(filter(lambda x : x in vowels, phrase_letters))

    @staticmethod
    def getVowels():
        return vowels