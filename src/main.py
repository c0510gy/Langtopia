import sys
import qdarkstyle
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QSizePolicy, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QToolButton, QLabel, QPushButton

from src import audioController, overwrapSubController

from src.settingWindow import SettingWindow

class ToggleButton(QToolButton):
    def __init__(self, controller):
        super().__init__()
        #self.setText('OFF')
        self.setFont(QtGui.QFont("맑은 고딕", 20, QtGui.QFont.Light))

        self.setFixedSize(360, 176)

        self.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Expanding)
        self.setStyleSheet("background-image:url(./images/OFF.png);border:0px")

        self.setCheckable(True)
        self.toggled.connect(self.slot_toggle)

        self.controller = controller
        self.controller_instance = None

    def remoteToggle(self):
        self.toggle()
        #self.click()
        #self.toggled.emit(False)

    def slot_toggle(self, state):
        ##CEFDFF
        #self.setStyleSheet("background-color: %s" % ({True: "green", False: "red"}[state]))
        if state:
            self.controller_instance = self.controller(self.remoteToggle)
            self.controller_instance.show()
            self.sender().setStyleSheet("background-image:url(./images/ON.png);border:0px")
        else:
            self.controller_instance.remoteStop()
            self.controller_instance = None
            self.sender().setStyleSheet("background-image:url(./images/OFF.png);border:0px")
        #self.setText({True: "ON", False: "OFF"}[state])

class ItemContainer(QVBoxLayout):
    def __init__(self, title, controller):
        super().__init__()

        self.label_title = QLabel()
        self.label_title.setText(title)
        self.label_title.setFont(QtGui.QFont("맑은 고딕", 20, QtGui.QFont.Light))


        self.button_toggle = ToggleButton(controller)

        self.addWidget(self.label_title)
        self.addWidget(self.button_toggle)
        #self.addLayout(self.hlayout)

        #self.setCheckable(True)
        #self.toggled.connect(self.slot_toggle)

class Langtopia(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Langtopia')

        self.settingWindow = SettingWindow()

        self.screen_controller = overwrapSubController.OverwrapSubController
        self.audio_controller = audioController.AudioSubController
        self.toggle_screen = ItemContainer('Screen Translator', self.screen_controller)
        self.toggle_audio = ItemContainer('Audio Subtitles', self.audio_controller)

        self.hlayout = QHBoxLayout()
        self.hlayout.addLayout(self.toggle_screen)
        self.hlayout.addLayout(self.toggle_audio)

        self.hlayout2 = QHBoxLayout()

        self.label_version = QLabel()
        self.label_version.setText('Ver. 0.0.1')
        self.button_setting = QPushButton()
        self.button_setting.setText('설정')
        self.button_setting.setMinimumSize(100, 30)
        self.button_setting.clicked.connect(self.settingButtonClicked)

        self.hlayout2.addWidget(self.label_version)
        self.hlayout2.addStretch(1)
        self.hlayout2.addWidget(self.button_setting)

        self.vlayout = QVBoxLayout()
        self.vlayout.addLayout(self.hlayout)
        self.vlayout.addLayout(self.hlayout2)


        self.setLayout(self.vlayout)

        self.setFixedSize(800, 300)

    def settingButtonClicked(self):
        self.settingWindow.show()

    def closeEvent(self, event):
        # 강력한 종료 필요
        self.screen_controller = None
        self.audio_controller = None
        self.destroy()


app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#app.setStyle('Fusion')

langtopia = Langtopia()
langtopia.show()

sys.exit(app.exec_())