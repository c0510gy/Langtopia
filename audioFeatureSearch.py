import pickle
import os
from scipy import spatial
from scipy import signal
import matplotlib.pyplot as plt

class AudioFeatureSearch(object):

    def __init__(self):
        feature_vectors = []
        self.thresholds = []

        self.infos = []
        i = 0
        while os.path.isfile(r'.\audioDatas\{}.pickle'.format(i)):
            f = open(r'.\audioDatas\{}.pickle'.format(i), 'rb')
            info = pickle.load(f)
            f.close()
            self.infos.append(info[:2])
            feature_vectors.append(info[2][0])
            self.thresholds.append(info[2][1])
            i += 1

        self.kd_tree = spatial.KDTree(feature_vectors)

    def getName(self, idx):
        return self.infos[idx][0]

    def getSubtitles(self, idx):
        return self.infos[idx][1]

    def search(self, dat):
        dist, idx = self.kd_tree.query(dat)
        #print(dat)
        #print(dist, idx)
        if dist < self.thresholds[idx]:
            print(dist, idx)

            '''
            fulldat_concat = np.concatenate(fulldat)
            f, Pxx_den = signal.periodogram(fulldat_concat, RATE)
            plt.semilogy(f, Pxx_den)
            plt.ylim([1e-7, 1e2])
            plt.xlabel('frequency [Hz]')
            plt.ylabel('PSD [V**2/Hz]')
            plt.show()
            '''

            return idx
