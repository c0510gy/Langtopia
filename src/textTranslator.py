from googletrans import Translator

class TextTranslator(object):

    def __init__(self):
        self.translator = Translator()

    def translate_list(self, lst):
        try:
            tr_results = self.translator.translate(lst, src='en', dest='ko')
            ret = []
            for i in tr_results:
                ret.append(i.text)
        except Exception as e: print('error!: ', e)

        return ret

    def translate(self, text):
        tr_results = self.translator.translate(text, src='en', dest='ko')
        return tr_results.text

if __name__ == '__main__':
    translator = Translator()
    tr_results = translator.translate('안녕하세요.', src='ko', dest='en')
    print('Trans(EN):', tr_results.text, tr_results.src, tr_results.dest)

    tr_results = translator.translate('There are statements that can neither be proved nor disproved', src='en', dest='ko')
    print(tr_results.text, tr_results.src, tr_results.dest)