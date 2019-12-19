import threading
import speech_recognition as sr
import time
import queue

class SpeechToText(object):

    def __init__(self, speechHandler):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        print(sr.Microphone.list_microphone_names())
        self.mic = sr.Microphone(device_index=1)
        self.audios = queue.Queue()

        self.speechHandler = speechHandler
        self.isAborted = False

    def audioListenner(self):
        while not self.isAborted:
            with self.mic as source:
                # st = time.time()
                audio = self.r.listen(source, phrase_time_limit=3)  # , timeout=3
                self.audios.put(audio)
                # print(time.time() - st)
                # print(r.recognize_sphinx(audio))
                # r.recognize_google(audio)

    def start(self):
        self.isAborted = False

        self.t = threading.Thread(target=self.audioListenner)
        self.t.start()

        while True:
            if not self.audios.empty():
                audio = self.audios.get()
                text = self.r.recognize_sphinx(audio)
                self.speechHandler(text)
                #print(self.r.recognize_sphinx(audio))

    def stop(self):
        self.isAborted = True