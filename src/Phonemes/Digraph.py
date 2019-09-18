from Phonemes.AbstractPhoneme import AbstractPhoneme

class Digraph(AbstractPhoneme):
    
    def setProperties(self, letters):
        pass

    def add(self, phonemes):
        phonemes.append(self.value)
        
    def getFromList(self, phonemes):
        digraphs = []

        for digraph in ['ch', 'lh', 'nh', 'gu', 'qu', 'sc', 'sç', 'xc', 'xs',
                        'gh', 'th', 'sh', 'zh', 'rh', 'ph', 'wh', 'wr', 'ck',
                        'kn', 'dg', 'pn', 'ps', 'ng',
                       ]:
            lettersDigraph = list(digraph)
            
            if lettersDigraph[0] in phonemes and lettersDigraph[1] in phonemes and len(list(filter(lambda x : lettersDigraph[0] in list(x) or lettersDigraph[1] in list(x), digraphs))) == 0:
                digraphs.append(digraph)

        return digraphs
        
        