from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
import sys

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
        self.lbl.setStyleSheet('background-color: black; color: white')
        self.setGeometry(0, 0, 0, 0)
        self.show()

    def showSub(self, yrate, text):
        self.lbl.setText(text)

        fsize = 20

        self.lbl.setFont(QtGui.QFont("맑은 고딕", fsize, QtGui.QFont.Light))

        width = self.lbl.fontMetrics().boundingRect(self.lbl.text()).width()
        height = self.lbl.fontMetrics().boundingRect(self.lbl.text()).height()

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