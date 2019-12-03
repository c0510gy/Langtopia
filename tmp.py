import pickle

f = open(r'.\audioDatas\1.pickle', 'rb')
a = pickle.load(f)
f.close()

a[0] = '🎵 Will Joseph Cook - Take Me Dancing'
f = open(r'.\audioDatas\1.pickle', 'wb')
pickle.dump(a, f)
f.close()