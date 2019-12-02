try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


class TextRecog(object):

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    def getText(self, img):
        dat = pytesseract.image_to_data(img)
        #print(dat)

        dat = dat.replace('\n', '\t').split('\t')
        rows = [dat[i * 12:i * 12 + 12] for i in range(1, len(dat) // 12)]
        detected = []
        for i in range(len(rows)):
            if int(rows[i][10]) >= 40:
                if len(detected) > 0 and abs(detected[-1][0] + detected[-1][2] - int(rows[i][6])) <= 20 and abs(detected[-1][1] - int(rows[i][7])) <= 20:
                    detected[-1][4] += ' ' + rows[i][11]
                    detected[-1][2] = int(rows[i][6]) - detected[-1][0] + int(rows[i][8])
                else:
                    detected.append([int(rows[i][6]), int(rows[i][7]), int(rows[i][8]), int(rows[i][9]), rows[i][11]])
                #if len(detected) == 0 or rows[i - 1][0] != rows[i][0]:
                #    # [left, top, width, height, text]
                #    detected.append([int(rows[i][6]), int(rows[i][7]), int(rows[i][8]), int(rows[i][9]), rows[i][11]])
                #elif rows[i - 1][0] == rows[i][0]:
                #    detected[-1][4] += ' ' + rows[i][11]

        ret = []
        for i in range(len(detected)):
            detected[i][4] = detected[i][4].strip()
            if len(detected[i][4]) > 0:
                ret.append(detected[i])

        return ret