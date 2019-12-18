import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QSizePolicy
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

import popupSub
import overwrapSub
import screenCapture
import textRecog
import textTranslator
import screenFeatureSearch

class OverwrapSubController(QWidget):

    def __init__(self, remoteToggle, parent=None):
        super().__init__(parent)

        self.remoteToggle = remoteToggle

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.resize(200, 100)
        self.setWindowTitle('Langtopia - Screen Translator')
        #self.setStyleSheet("background-color: BLACK; color: LIME; border: 1px solid black")

        self.label_title = QLabel()
        self.label_title.setText('Screen Translator')

        self.button_translate = QToolButton()
        self.button_translate.setText('translate')
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

        self.screen = screenCapture.ScreenCapture()
        self.textrecog = textRecog.TextRecog()
        self.trans = textTranslator.TextTranslator()
        self.screenSearch = screenFeatureSearch.ScreenFeatureSearch()

        self.popups = []

        self.oldPos = self.pos()


    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)

        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def quitClicked(self):
        self.stop()
        self.close()

    def buttonClicked(self):
        for i in self.popups:
            i.close()

        self.popups = []

        screen_image = self.screen.getScreen()
        text_info_list = self.textrecog.getText(screen_image)

        self.overwrap = overwrapSub.OverwrapSub()

        text_str_list = []
        translated = []
        indexes = []
        for i in range(len(text_info_list)):
            #print(text_info_list[i][4])
            searched = self.screenSearch.search(text_info_list[i][4])
            translated.append(searched)
            if searched is None:
                text_str_list.append(text_info_list[i][4])
                indexes.append(i)
            else:
                translated[-1] = '✔️ ' + translated[-1]
                print(searched)

        google_translated = self.trans.translate_list(text_str_list) #[i[4] for i in text_info_list]
        for i in range(len(indexes)):
            translated[indexes[i]] = google_translated[i]

        for i in range(len(text_info_list)):
            #translated = i[4] #self.trans.translate(i[4])

            self.overwrap.addSub(text_info_list[i][0], text_info_list[i][1], text_info_list[i][2], text_info_list[i][3], translated[i])
            #self.overwrap.addSub(text_info_list[i][0], text_info_list[i][1], text_info_list[i][2], text_info_list[i][3], translated[i])
            #popup = popupSub.PopupSub(i[0], i[1], i[2], i[3], translated)
            #self.popups.append(popup)
            #popup.show()

        self.overwrap.showFullScreen()

    def stop(self):
        self.remoteToggle()
        self.destroy()

    def remoteStop(self):
        self.destroy()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    popup_control = OverwrapSubController()
    popup_control.show()

    sys.exit(app.exec_())