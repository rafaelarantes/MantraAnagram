from Phonemes.AbstractPhoneme import AbstractPhoneme

digraphs = ['ch', 'lh', 'nh', 'gu', 'qu', 'sc', 'sç', 'xc', 'xs',
                        'gh', 'th', 'sh', 'zh', 'rh', 'ph', 'wh', 'wr', 'ck',
                        'kn', 'dg', 'pn', 'ps', 'ng',
           ]

class Digraph(AbstractPhoneme):
    
    def _setProperties(self, phrase_letters):
        pass

    def _add(self, diagram_letters):
        diagram_letters.append(self.value)
        
    def _getFromList(self, phrase_letters):
        digraph_result = []

        for digraph in digraphs:
            lettersDigraph = list(digraph)
            
            if lettersDigraph[0] in phrase_letters and lettersDigraph[1] in phrase_letters and self.__notExistsLettersInList(lettersDigraph[0], lettersDigraph[1], digraph_result):
                digraph_result.append(digraph)

        return digraph_result

    def __notExistsLettersInList(self, first_letter, second_letter, digraph_list):
        return len(list(filter(lambda x : first_letter in list(x) or second_letter in list(x), digraph_list))) == 0

        
    @staticmethod
    def getDigraphs():
        return digraphs