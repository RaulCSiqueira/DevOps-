from collections import defaultdict 

def normalize_key(key):
    return ''.join([char.lower() for char in key if char.isalpha()])

class NormalizedDict(dict):
    def __setitem__(self, k, v):
        super().__setitem__(normalize_key(k), v)

    def __getitem__(self, k):
        return super().__getitem__(normalize_key(k))
    
class AdjustedValueDict(dict):
    def __init__(self, factor, *args, **kwargs):
        self.factor = factor
        super().__init__(*args, **kwargs)

    def __setitem__(self, k ,v):
        super().__setitem__(k, v *self.factor)
        
class PlayerScoreDict(NormalizedDict, AdjustedValueDict, defaultdict): ...


if __name__ == '__main__':
    print(PlayerScoreDict.mro())
    scores = PlayerScoreDict(1_000, int)
    scores['Ada Lovelace'] = 1_314
    scores['Carl Sagan  '] = 1_236
    scores['Grace Hopper'] = 2_349

    print(scores)
    print('The value for MiSSING is: ', scores['MISSING'])