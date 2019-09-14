
class Consonant(AbstractPhoneme):

    def addToList(self, phonemes):
        phonemes.append(self.value)

        

        if self.next_phoneme is not None:
            self.next_phoneme(phonemes)
    
    def __getFromList(self, phonemes):
        return list(filter(lambda x : x not in ['a', 'e', 'i', 'o', 'u', 'r', 's'], phonemes))


