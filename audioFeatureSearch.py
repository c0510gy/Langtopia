from scipy import spatial
from scipy import signal
import matplotlib.pyplot as plt

class AudioFeatureSearch(object):

    def __init__(self):
        features = []
        features.append([0.4375, 0.4765625, 0.49609375, 0.42578125, 0.4375, 0.4765625, 0.49609375, 0.42578125, 0.490234375, 0.552734375, 0.83203125, 0.935546875, 0.939453125, 1.333984375, 1.96875, 3.095703125, 3.16796875, 3.927734375, 4.64453125, 5.994140625, 6.400390625, 6.20703125, 6.814453125, 9.638671875, 13.6640625, 11.400390625, 13.28515625, 13.05859375, 15.888671875, 15.267578125, 20.884765625, 76.658203125, 550.24609375, 863.93359375, 1620.10546875, 2471.4453125, 2409.904296875, 1977.9921875, 2202.275390625, 2364.806640625, 3488.01171875, 4958.5078125, 4083.677734375, 4266.0390625, 4265.330078125, 3449.767578125, 2706.96484375, 3456.1015625, 4818.908203125, 6181.68359375, 4908.9921875, 1326.28515625, 2938.2890625, 2489.0390625, 1696.41015625, 859.796875, 396.294921875, 159.05078125, 267.83203125, 293.421875, 2227.328125, 2024.234375, 1679.837890625, 1861.7578125, 1777.23828125, 2228.796875, 4062.8984375, 3353.79296875, 2445.892578125, 2662.51171875, 2887.4375, 2617.958984375, 1971.306640625, 2245.1640625, 2429.29296875, 2555.83203125, 2256.603515625, 1356.033203125, 1270.22265625, 1033.8125, 1695.095703125, 1064.931640625, 288.072265625, 174.22265625, 87.40234375, 103.501953125, 104.861328125, 84.0859375, 1048.12109375, 2367.771484375, 2145.890625, 1946.171875, 2108.580078125, 2561.94140625, 1946.251953125, 2219.857421875, 1193.60546875, 850.357421875, 673.431640625, 1211.3359375, 1433.26171875, 1100.1953125, 1461.658203125, 1188.560546875, 1709.58203125, 1456.94921875, 1687.296875, 1131.01953125, 699.5625, 525.416015625, 279.185546875, 443.890625, 775.0390625, 860.591796875, 873.462890625, 966.34375, 903.171875, 965.0, 557.0078125, 331.890625, 273.51953125, 467.791015625, 778.068359375, 811.765625, 718.09765625, 450.7109375, 94.193359375, 78.94140625, 111.509765625, 100.416015625, 190.68359375, 582.787109375, 702.69921875, 547.537109375, 768.609375, 1051.33203125, 1283.953125, 1016.353515625, 759.6953125, 694.953125, 476.837890625, 492.50390625, 850.037109375, 851.337890625, 645.990234375, 203.802734375, 175.580078125, 185.625, 219.115234375, 150.6328125, 359.080078125, 371.564453125, 290.314453125, 279.2734375, 434.921875, 277.384765625, 129.798828125, 158.49609375, 122.486328125, 347.48046875, 287.234375, 193.22265625, 113.84375, 350.6796875, 328.4140625, 223.732421875, 116.552734375, 95.591796875, 134.92578125, 212.166015625, 369.05859375, 362.77734375, 242.978515625, 227.853515625, 176.671875, 267.708984375, 210.33203125, 141.966796875, 149.955078125, 126.951171875, 184.544921875, 143.4765625, 198.7890625, 103.0546875, 55.607421875, 95.54296875, 52.43359375, 51.642578125, 46.15625, 24.232421875, 42.296875, 35.74609375, 30.12109375, 50.60546875, 33.228515625, 27.41015625, 19.115234375, 32.35546875, 42.900390625, 26.955078125, 30.689453125, 30.6015625, 30.78515625, 130.078125, 278.98828125, 103.70703125, 60.7421875, 30.259765625, 32.7890625, 46.869140625, 36.69140625, 40.515625, 32.359375, 35.6015625, 39.66015625])
        features.append([845.27734375, 975.240234375, 1073.78125, 683.525390625, 782.306640625, 624.9765625, 832.1640625, 1380.546875, 1209.9296875, 1321.701171875, 905.45703125, 1209.041015625, 2177.259765625, 1588.193359375, 987.439453125, 1337.076171875, 1053.431640625, 1073.798828125, 774.912109375, 1357.880859375, 1533.880859375, 878.97265625, 1023.98046875, 1042.98828125, 1058.478515625, 1225.177734375, 752.46484375, 832.84375, 1020.990234375, 645.65234375, 669.22265625, 741.685546875, 1319.23046875, 1976.171875, 900.26953125, 845.1328125, 1147.115234375, 727.677734375, 926.6015625, 1300.34765625, 828.142578125, 1058.3515625, 1167.99609375, 1053.880859375, 669.455078125, 679.306640625, 847.828125, 1012.59375, 940.609375, 1088.53515625, 633.30078125, 654.58203125, 767.154296875, 819.310546875, 1060.583984375, 677.626953125, 884.451171875, 786.017578125, 816.65625, 709.4453125, 924.986328125, 773.833984375, 833.498046875, 834.646484375, 881.263671875, 704.82421875, 815.048828125, 581.638671875, 642.078125, 697.689453125, 809.857421875, 1094.95703125, 2281.853515625, 976.775390625, 974.822265625, 766.484375, 1026.806640625, 881.935546875, 738.736328125, 1545.591796875, 1007.71875, 707.568359375, 817.404296875, 1176.375, 865.48046875, 816.638671875, 851.490234375, 726.359375, 1703.408203125, 2615.34765625, 822.505859375, 1087.369140625, 1086.1640625, 798.115234375, 1124.236328125, 774.693359375, 788.921875, 2664.25390625, 2076.458984375, 1105.8671875, 1149.83203125, 1470.90625, 1248.287109375, 1144.90234375, 646.12109375, 925.90234375, 1272.78125, 1515.01171875, 771.953125, 820.162109375, 904.546875, 717.255859375, 700.0390625, 711.76171875, 813.783203125, 725.0234375, 967.357421875, 818.033203125, 1555.634765625, 1023.693359375, 1033.927734375, 982.87890625, 928.005859375, 1594.3046875, 1421.03125, 867.384765625, 978.01953125, 1035.486328125, 1032.900390625, 656.98828125, 1014.73828125, 906.3671875, 739.20703125, 1089.16796875, 1145.580078125, 1157.01953125, 895.1484375, 1186.12109375, 2358.34375, 862.341796875, 724.798828125, 852.71875, 607.396484375, 737.5078125, 765.35546875, 675.38671875, 642.24609375, 754.962890625, 896.416015625, 1203.158203125, 820.015625, 641.212890625, 670.345703125, 754.650390625, 749.197265625, 953.025390625, 1205.013671875, 728.3046875, 808.107421875, 1107.703125, 1511.021484375, 996.09765625, 1309.18359375, 1067.625, 1095.23828125, 1355.05078125, 941.111328125, 796.265625, 1233.1328125, 991.189453125, 1071.60546875, 572.78125, 817.46484375, 907.541015625, 897.95703125, 849.76953125, 521.603515625, 754.1953125, 818.595703125, 620.37890625, 593.048828125, 834.486328125, 824.3046875, 755.322265625, 646.134765625, 931.416015625, 711.009765625, 825.646484375, 865.7890625, 1134.830078125, 752.0390625, 967.259765625, 884.728515625, 714.5546875, 676.86328125, 728.291015625, 746.8515625, 770.54296875, 889.513671875, 630.9453125, 797.89453125, 878.916015625, 679.15625, 874.587890625, 1116.580078125, 862.3359375, 843.1640625, 653.0703125, 684.240234375, 840.87109375, 836.2890625, 627.017578125, 753.34375, 830.44140625, 908.068359375])
        self.threshold = [5000, 5000]
        self.info = ['3 3 Locality Sensitive Hashing 19 24', 'Will Joseph Cook - Take Me Dancing']
        self.subs = []
        self.subs.append([
[1, 'the special case of minhash signatures and later see the general LSH idea.'],
[7, 'First, let\'s remember where we\'ve gotten so far.'],
[10, 'We converted documents to sets of shingles and then we converted the presumably large'],
[15, 'sets of shingles to short signatures, consistently a vectors of integers.'],
[20, 'We can compare two signatures as they make quite close to'],
[24 ,'the Jaccard similarity of their underlying sets.'],
[27, 'Since the signatures are relatively short, we can fit many of them into main memory'],
[31, 'at once and thus compare many different pairs of these signatures without having'],
[35, 'to spend the time needed to read each signature from disk many times.'],
[41, 'The idea behind LSH is to look at the collection of elements, that is,'],
[45, 'signatures in our example here, whose similar pairs we want to find and'],
[49, 'without constructing all pairs of those elements, create a short list of'],
[53, 'candidate pairs whose similarity actually must be measured.'],
[58, 'When constructing candidate pairs,'],
[59, 'you look only at individual elements, not at the pairs themselves.'],
])
        self.subs.append([[1, "Here's to Julian, a man among a million others"], [6.144725799560547, 'Turned his back upon it all'], [10.072923421859741, 'Raise another glass then smash it up into its fragments'], [18.105026960372925, 'Walking barefoot on the ground'], [22.820356607437134, 'And as I fall into the bottle bank (broken glass)'], [28.78082513809204, 'You can make me into anything'], [31.772842168807983, "As long as I'm reflecting you"], [34.82277989387512, "Don't let this love"], [37.48389530181885, 'Well I could be the answer to'], [40.711647033691406, 'All of your prayers'], [43.92404222488403, 'Take me dancing'], [47.013453245162964, "Lonely ain't enough"], [48.874123334884644, 'Well I could be the answer to'], [52.40034008026123, 'All of your prayers'], [55.3791446685791, 'Take me dancing'], [58.473042249679565, 'Sing to Emily, make her laugh and talk her accent'], [64.63629150390625, 'See the colour in her eyes'], [68.11171007156372, "Then I'll take her palm and joke about a life together"], [76.1278784275055, 'Lying, smoking on the ground'], [81.76814579963684, 'And as I fall into the bottle bank (broken glass)'], [87.2914547920227, 'You can make me into anything'], [90.277263879776, "As long as I'm reflecting you"], [93.49574398994446, "Don't let this love"], [95.93912363052368, 'I could be the answer to'], [99.26041197776794, 'All of your prayers'], [102.71418046951294, 'Take me dancing'], [105.24791812896729, "Lonely ain't enough"], [107.71923756599426, 'Well I could be the answer to'], [111.22759175300598, 'All of your prayers'], [114.11046719551086, 'Take me dancing'], [116.9459981918335, 'Every moment (every moment)'], [122.7608757019043, 'Always like this (always like this)'], [128.55525851249695, 'We got our come ups (we got our come ups)'], [134.04070568084717, 'And you [?]'], [139.17076754570007, 'Lonely is your love'], [143.0260591506958, 'Well I could be the answer to'], [146.24212884902954, 'All of your prayers'], [149.30153274536133, 'Take me dancing'], [152.2204306125641, "Lonely ain't enough"], [154.4972517490387, 'Well I could be the answer to'], [157.99039936065674, 'All of your prayers'], [161.12155652046204, 'Take me dancing'], [163.70111751556396, 'We could walk to the city bars'], [166.6850688457489, 'We could swing to Americana'], [169.483008146286, "I don't need much don't make a difference"], [172.47373700141907, 'Just take me dancing'], [175.42982006072998, 'We could walk to the shitty bars'], [178.32625675201416, 'We could swing to Americana'], [181.16872835159302, "I don't need much don't make a difference"], [184.20091152191162, 'Just take me dancing']])
        self.kd_tree = spatial.KDTree(features)

    def search(self, dat):
        dist, idx = self.kd_tree.query(dat)
        #print(dat)
        #print(dist, idx)
        if dist < self.threshold[idx]:
            print(dist, idx)
            return idx
            '''
            fulldat_concat = np.concatenate(fulldat)
            f, Pxx_den = signal.periodogram(fulldat_concat, RATE)
            plt.semilogy(f, Pxx_den)
            plt.ylim([1e-7, 1e2])
            plt.xlabel('frequency [Hz]')
            plt.ylabel('PSD [V**2/Hz]')
            plt.show()
            '''
