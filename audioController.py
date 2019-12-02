import sys
import threading
import time

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint, QThread
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QSizePolicy
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

import popupSub
import overwrapSub
import audioCapture
import audioFeatureSearch
import textRecog
import textTranslator

class AudioCaptureThread(QThread):

    def __init__(self, audioHandler):
        QThread.__init__(self)

        self.audio = audioCapture.AudioCapture(audioHandler)

    def __del__(self):
        self.audio.stop()
        self.wait()

    def run(self):
        # your logic here
        self.audio.run()

    def stop(self):
        self.terminate()

class AudioSubController(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.resize(200, 100)
        self.setWindowTitle('Langtopia - Audio Subtitles')
        self.setStyleSheet("background-color: BLACK; color: LIME; border: 1px solid black")

        self.label_title = QLabel()
        self.label_title.setText('Audio Subtitles')

        self.button_translate = QToolButton()
        self.button_translate.setText('skip')
        self.button_translate.clicked.connect(self.buttonClicked)
        self.button_translate.setSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding) # 버튼 크기 일정하게

        self.button_quit = QToolButton()
        self.button_quit.setText('quit')
        self.button_quit.clicked.connect(self.quitClicked)
        self.button_quit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.gridlayout = QGridLayout()
        self.gridlayout.addWidget(self.label_title, 0, 0, 1, 2)
        self.gridlayout.addWidget(self.button_translate, 1, 0, 1, 1)
        self.gridlayout.addWidget(self.button_quit, 1, 1, 1, 1)

        self.setLayout(self.gridlayout)

        self.audio = AudioCaptureThread(self.audioHandler)
        self.audioSearch = audioFeatureSearch.AudioFeatureSearch()
        self.popup_sub = popupSub.PopupSub()
        #self.trans = textTranslator.TextTranslator()

        self.oldPos = self.pos()

        self.skip = False

        self.audio.start()
        self.showing = False
        self.popup_sub.showSub(0.8, ' ')

    def audioHandler(self, dat):
        #print('audio captured:', dat)
        idx = self.audioSearch.search(dat)
        if idx is not None:
            print(idx)
            if not self.showing:
                self.showing = True
                #self.audio.stop()
                self.label_title.setText('Audio Subtitles\n' + self.audioSearch.info[idx])
                self.popup_sub.showSub(0.8, self.audioSearch.info[idx])
                self.skip = False
                self.playSub(idx)
                self.showing = False
                #self.audio.start()

    def playSub(self, idx):
        sub = self.audioSearch.subs[idx]

        st = time.time()
        for s in sub:
            while True:
                time.sleep(0.1)
                nt = time.time()
                if nt - st >= s[0] or self.skip:
                    break
            self.popup_sub.showSub(0.8, s[1])
            if self.skip:
                self.skip = False
                self.popup_sub.showSub(0.8, ' ')
                self.label_title.setText('Audio Subtitles')
                break

        time.sleep(5)
        self.popup_sub.showSub(0.8, ' ')
        self.label_title.setText('Audio Subtitles')

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        #print(delta)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def quitClicked(self):
        self.close()

    def buttonClicked(self):
        self.skip = True


app = QApplication(sys.argv)
audio_sub_control = AudioSubController()
audio_sub_control.show()

sys.exit(app.exec_())