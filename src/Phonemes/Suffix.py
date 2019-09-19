from Phonemes.AbstractPhoneme import AbstractPhoneme

suffixes = ['r', 's']
class Suffix(AbstractPhoneme):

    def _setProperties(self, phrase_letters):
        self.next_phoneme = None

    def _add(self, diagram_letters):
        diagram_letters.append(self.value)

    def _getFromList(self, phrase_letters):
        if self.__hasAnotherTypeOfPhonemeInListThatIsNotSuffix(phrase_letters):
            return list(filter(lambda x : x in suffixes, phrase_letters))

        return []

    def __hasAnotherTypeOfPhonemeInListThatIsNotSuffix(self, phrase_letters):
        return len(list(filter(lambda x : x not in suffixes, phrase_letters))) == 0


    @staticmethod
    def getSuffixes():
        return suffixes