from Phonemes.AbstractPhoneme import AbstractPhoneme

suffixes = ['r', 's']
class Suffix(AbstractPhoneme):

    def _setProperties(self, letters):
        self.next_phoneme = None

    def _add(self, phonemes):
        phonemes.append(self.value)

    def _getFromList(self, phonemes):
        if self.__hasAnotherTypeOfPhonemeInListThatIsNotSuffix(phonemes):
            return list(filter(lambda x : x in suffixes, phonemes))

        return []

    def __hasAnotherTypeOfPhonemeInListThatIsNotSuffix(self, letters):
        return len(list(filter(lambda x : x not in suffixes, letters))) == 0


    @staticmethod
    def getSuffixes():
        return suffixes