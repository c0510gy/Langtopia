from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
import sys

from settingManager import settingManager

class OverwrapSub(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.rectangles = [] # detected boxes
        self.subs = [] # detected texts
        self.selected = -1 # selected box
        self.lbl = QLabel(self)

        self.setWindowFlags(
                  Qt.FramelessWindowHint # hides the window controls
                | Qt.WindowStaysOnTopHint # forces window to top... maybe
                | Qt.SplashScreen # this one hides it from the task bar!
                )
        # alternative way of making base window transparent
        self.setAttribute(Qt.WA_TranslucentBackground, True) #100% transparent

        self.setMouseTracking(True)

    def setSub(self, x, y, w, h, text):

        self.lbl.setText(text)

        fsize = 12
        '''
        minf, maxf = 1, 100
        while minf <= maxf:
            mid = (minf + maxf) >> 1

            self.lbl.setFont(QtGui.QFont("맑은 고딕", mid, QtGui.QFont.Light))
            width = self.lbl.fontMetrics().boundingRect(self.lbl.text()).width()
            height = self.lbl.fontMetrics().boundingRect(self.lbl.text()).height()

            if width <= w and height <= h + 10:
                minf = mid + 1
                fsize = mid
            else:
                maxf = mid - 1
        '''

        width = self.lbl.fontMetrics().boundingRect(self.lbl.text()).width()
        height = self.lbl.fontMetrics().boundingRect(self.lbl.text()).height()
        self.lbl.setFont(QtGui.QFont("맑은 고딕", fsize, QtGui.QFont.Light))
        self.lbl.setStyleSheet('border: 2px solid black; border-radius: 10px; background-color: {}; color: {}'\
                               .format(settingManager.screenSetting['background_color'], settingManager.screenSetting['font_color']))
        self.lbl.setGeometry(x, y, width + 15, height + 5)

    def addSub(self, x, y, w, h, text):
        self.rectangles.append([x, y, w, h])
        self.subs.append(text)

    def mousePressEvent(self, QMouseEvent):
        self.close()
        #print(QMouseEvent.pos())

    def mouseReleaseEvent(self, QMouseEvent):
        self.close()
        cursor = QtGui.QCursor()
        #print(cursor.pos())

    def mouseMoveEvent(self, event):
        #print(event.x(), event.y())
        x, y = event.x(), event.y()
        for i in range(len(self.rectangles)):
            rec = self.rectangles[i]
            if rec[0] <= x <= rec[0] + rec[2] and rec[1] <= y <= rec[1] + rec[3]:
                self.selected = i
                popy = rec[1] - 40
                if popy <= 0:
                    popy = rec[1] + rec[3] + 20
                self.setSub(rec[0], popy, rec[2], rec[3], self.subs[i])

        #if self.selected == -1:
        #    self.lbl = None

    def paintEvent(self, event=None):
        painter = QtGui.QPainter(self)

        painter.setOpacity(0.005)
        painter.setBrush(Qt.white)
        painter.setPen(QtGui.QPen(Qt.white))
        painter.drawRect(self.rect())

        for i in range(len(self.rectangles)):
            rec = self.rectangles[i]
            painter.setOpacity(1)
            if self.selected == i:
                painter.setOpacity(0.3)
                painter.setBrush(QtGui.QBrush(QtGui.QColor(settingManager.screenSetting['selected_color']), Qt.SolidPattern))
            else:
                painter.setBrush(Qt.transparent)

            painter.setPen(QtGui.QPen(Qt.red, 1, Qt.SolidLine))
            painter.drawRect(rec[0], rec[1], rec[2], rec[3])

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = OverwrapSub()
    myWindow.addSub(300, 300, 100, 100, 'Hello')
    myWindow.showFullScreen()

    sys.exit(app.exec_())