import pickle
import os

class ScreenFeatureSearch(object):

    def __init__(self):
        self.subMap = dict()
        
        for file in os.listdir('./screenDatas/'):
            if file.endswith('.pickle'):
                fpath = os.path.join('./screenDatas/', file)

                f = open(fpath, 'rb')
                features = pickle.load(f)
                f.close()

                for f in features:
                    self.subMap[f[0].strip()] = f[1]

    def search(self, text):
        if text.strip() in self.subMap:
            return self.subMap[text.strip()]
        return None
