
class Digraph(AbstractPhoneme):

    def addToList(self, phonemes):
        phonemes.append(self.value)

        if self.next_phoneme is not None:
            self.next_phoneme(phonemes)

    def __getFromList(self, phonemes):
        digraphs = []

        for digraph in ['ch', 'lh', 'nh', 'gu', 'qu', 'sc', 'sç', 'xc', 'xs',
                        'gh', 'th', 'sh', 'zh', 'rh', 'ph', 'wh', 'wr', 'ck',
                        'kn', 'dg', 'pn', 'ps', 'ng',
                       ]:
            lettersDigraph = list(digraph)
            
            if lettersDigraph[0] in phonemes and lettersDigraph[1] in phonemes and len(list(filter(lambda x : lettersDigraph[0] in list(x) or lettersDigraph[1] in list(x), digraphs))) == 0:
                digraphs.append[digraph]

        return digraphs
        
        