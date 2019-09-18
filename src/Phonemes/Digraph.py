from Phonemes.AbstractPhoneme import AbstractPhoneme

digraphs = ['ch', 'lh', 'nh', 'gu', 'qu', 'sc', 'sç', 'xc', 'xs',
                        'gh', 'th', 'sh', 'zh', 'rh', 'ph', 'wh', 'wr', 'ck',
                        'kn', 'dg', 'pn', 'ps', 'ng',
           ]

class Digraph(AbstractPhoneme):
    
    def _setProperties(self, letters):
        pass

    def _add(self, phonemes):
        phonemes.append(self.value)
        
    def _getFromList(self, phonemes):
        digraph_result = []

        for digraph in digraphs:
            lettersDigraph = list(digraph)
            
            if lettersDigraph[0] in phonemes and lettersDigraph[1] in phonemes and len(list(filter(lambda x : lettersDigraph[0] in list(x) or lettersDigraph[1] in list(x), digraph_result))) == 0:
                digraph_result.append(digraph)

        return digraph_result
        
    @staticmethod
    def getDigraphs():
        return digraphs