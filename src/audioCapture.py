import pyaudio
import numpy as np
import time
from collections import deque

CHUNK = 2**10
RATE = 44100

class AudioCapture(object):

    def __init__(self, handler):
        self.p = pyaudio.PyAudio()

        self.handler = handler

        self.isAborted = False

    def run(self):
        default_input = self.p.get_default_input_device_info()
        input_index = default_input['index']

        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,
                                  frames_per_buffer=CHUNK, input_device_index=input_index)

        print('started')
        #self.handler.emit()
        st = time.time()

        l = 215 #430

        dat = deque()

        while not self.isAborted:
            data = np.fromstring(self.stream.read(CHUNK), dtype=np.int16)
            peak = np.average(np.abs(data)) * 2

            dat.append(peak)
            if len(dat) > l:
                dat.popleft()

            if len(dat) == l:
                self.handler(dat)
                #self.handler.emit()

    def stop(self):
        self.isAborted = True

        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
