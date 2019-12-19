from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtWidgets import QLabel
import sys

from src.settingManager import settingManager

class PopupSub(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(
                  Qt.FramelessWindowHint # hides the window controls
                | Qt.WindowStaysOnTopHint # forces window to top... maybe
                | Qt.SplashScreen # this one hides it from the task bar!
                )
        # alternative way of making base window transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True) #100% transparent

        self.lbl = QLabel(self)
        self.lbl.setStyleSheet('background-color: {}; color: {}'\
                               .format(settingManager.audioSetting['background_color'], settingManager.audioSetting['font_color']))
        self.setGeometry(0, 0, 0, 0)
        self.show()

    def showSub(self, yrate, text):
        self.lbl.setText(text)

        fsize = 25

        self.lbl.setFont(QtGui.QFont("맑은 고딕", fsize, QtGui.QFont.Light))

        width = self.lbl.fontMetrics().boundingRect(self.lbl.text()).width()
        height = self.lbl.fontMetrics().boundingRect(self.lbl.text()).height()
        if '\n' in text:
            width = self.lbl.fontMetrics().boundingRect(self.lbl.text().split('\n')[0]).width()
            width = max(width, self.lbl.fontMetrics().boundingRect(self.lbl.text().split('\n')[1]).width())
            height *= 2

        width += 15

        centerPoint = QDesktopWidget().availableGeometry().center()
        # setGeometry() 순서 주의
        self.setGeometry(centerPoint.x() - width // 2, int(centerPoint.y() * 2 * yrate), width, height)
        self.lbl.setGeometry(0, 0, width, height)

        #self.lbl.repaint()
        #self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = PopupSub()
    myWindow.showSub(0.8, '안녕 하세요')
    sys.exit(app.exec_())