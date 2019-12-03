import pickle
import os

class ScreenFeatureSearch(object):

    def __init__(self):
        self.subMap = dict()

        i = 0
        while os.path.isfile(r'.\screenDatas\{}.pickle'.format(i)):
            f = open(r'.\screenDatas\{}.pickle'.format(i), 'rb')
            features = pickle.load(f)
            f.close()
            for f in features:
                self.subMap[f[0].strip()] = f[1]
            i += 1

    def search(self, text):
        if text.strip() in self.subMap:
            return self.subMap[text.strip()]
        return None
