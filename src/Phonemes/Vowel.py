
class Digraph(AbstractPhoneme):

    def addToList(self, phonemes):
        phonemes.append(self.value)

    def __getFromList(self, phonemes):
        return list(filter(lambda x : x in ['a', 'e', 'i', 'o', 'u'], phonemes))
