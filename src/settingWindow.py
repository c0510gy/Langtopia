import os
from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QColorDialog, QGroupBox, QListWidget, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QGridLayout, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from src.TabWidget import TabWidget

from shutil import copyfile

from src.settingManager import settingManager

class SettingScreen(QWidget):

    def __init__(self):
        super().__init__()

        vlayout = QVBoxLayout()

        group1 = QGroupBox('번역 글자 색')
        group2 = QGroupBox('번역 글자 배경 색')
        group3 = QGroupBox('선택 색')

        self.color_label1 = QLabel(settingManager.screenSetting['font_color'])
        self.color_label1.setStyleSheet('color: {}; background-color: {};'\
                                        .format(self.getComplementary(settingManager.screenSetting['font_color']), settingManager.screenSetting['font_color']))
        self.color_label2 = QLabel(settingManager.screenSetting['background_color'])
        self.color_label2.setStyleSheet('color: {}; background-color: {};'\
                                        .format(self.getComplementary(settingManager.screenSetting['background_color']), settingManager.screenSetting['background_color']))
        self.color_label3 = QLabel(settingManager.screenSetting['selected_color'])
        self.color_label3.setStyleSheet('color: {}; background-color: {};'\
                                        .format(self.getComplementary(settingManager.screenSetting['selected_color']), settingManager.screenSetting['selected_color']))

        button1 = QPushButton('색 선택')
        button1.tag = 'font_color'
        button1.lbl = self.color_label1
        button1.clicked.connect(self.buttonClicked)
        button2 = QPushButton('색 선택')
        button2.tag = 'background_color'
        button2.lbl = self.color_label2
        button2.clicked.connect(self.buttonClicked)
        button3 = QPushButton('색 선택')
        button3.tag = 'selected_color'
        button3.lbl = self.color_label3
        button3.clicked.connect(self.buttonClicked)

        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()
        hlayout3 = QHBoxLayout()

        hlayout1.addWidget(self.color_label1)
        hlayout1.addWidget(button1)
        hlayout2.addWidget(self.color_label2)
        hlayout2.addWidget(button2)
        hlayout3.addWidget(self.color_label3)
        hlayout3.addWidget(button3)

        group1.setLayout(hlayout1)
        group2.setLayout(hlayout2)
        group3.setLayout(hlayout3)

        vlayout.addWidget(group1)
        vlayout.addWidget(group2)
        vlayout.addWidget(group3)

        vlayout.addStretch(1)

        self.setLayout(vlayout)

    def getComplementary(self, color):
        r, g, b = tuple([int(color[1:][i * 2:i * 2 + 2], 16) for i in range(3)])
        compColor = '#{:02x}{:02x}{:02x}'.format(255 - r, 255 - g, 255 - b)
        return compColor

    def buttonClicked(self):
        btn = self.sender()
        color = QColorDialog.getColor()
        if color.isValid():
            settingManager.screenSetting[btn.tag] = color.name()
            btn.lbl.setText(color.name())
            btn.lbl.setStyleSheet('color: {}; background-color: {};'\
                                  .format(self.getComplementary(settingManager.screenSetting[btn.tag]), settingManager.screenSetting[btn.tag]))


class SettingAudio(QWidget):

    def __init__(self):
        super().__init__()

        vlayout = QVBoxLayout()

        group1 = QGroupBox('자막 글자 색')
        group2 = QGroupBox('자막 배경 색')

        self.color_label1 = QLabel(settingManager.audioSetting['font_color'])

        self.color_label1.setStyleSheet('color: {}; background-color: {};'\
                                        .format(self.getComplementary(settingManager.audioSetting['font_color']), settingManager.audioSetting['font_color']))
        self.color_label2 = QLabel(settingManager.audioSetting['background_color'])
        self.color_label2.setStyleSheet('color: {}; background-color: {};'\
                                        .format(self.getComplementary(settingManager.audioSetting['background_color']), settingManager.audioSetting['background_color']))

        button1 = QPushButton('색 선택')
        button1.tag = 'font_color'
        button1.lbl = self.color_label1
        button1.clicked.connect(self.buttonClicked)
        button2 = QPushButton('색 선택')
        button2.tag = 'background_color'
        button2.lbl = self.color_label2
        button2.clicked.connect(self.buttonClicked)

        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()

        hlayout1.addWidget(self.color_label1)
        hlayout1.addWidget(button1)
        hlayout2.addWidget(self.color_label2)
        hlayout2.addWidget(button2)

        group1.setLayout(hlayout1)
        group2.setLayout(hlayout2)

        vlayout.addWidget(group1)
        vlayout.addWidget(group2)

        vlayout.addStretch(1)

        self.setLayout(vlayout)

    def getComplementary(self, color):
        r, g, b = tuple([int(color[1:][i * 2:i * 2 + 2], 16) for i in range(3)])
        compColor = '#{:02x}{:02x}{:02x}'.format(255 - r, 255 - g, 255 - b)
        return compColor

    def buttonClicked(self):
        btn = self.sender()
        color = QColorDialog.getColor()
        if color.isValid():
            settingManager.audioSetting[btn.tag] = color.name()
            btn.lbl.setText(color.name())
            btn.lbl.setStyleSheet('color: {}; background-color: {};'\
                                  .format(self.getComplementary(settingManager.audioSetting[btn.tag]), settingManager.audioSetting[btn.tag]))

class SettingSubsManager(QWidget):

    def __init__(self):
        super().__init__()

        vlayout = QVBoxLayout()

        group1 = QGroupBox('자막 캡슐 목록')

        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()

        self.subsList = QListWidget()
        for file in os.listdir('./audioDatas/'):
            if file.endswith('.pickle'):
                self.subsList.addItem(file)
        hlayout1.addWidget(self.subsList)

        group1.setLayout(hlayout1)
        vlayout.addWidget(group1)

        button1 = QPushButton('자막 캡슐 제거')
        button1.clicked.connect(self.removeCapsule)
        button2 = QPushButton('자막 캡슐 추가')
        button2.clicked.connect(self.addCapsule)

        hlayout2.addStretch(1)
        hlayout2.addWidget(button1)
        hlayout2.addWidget(button2)

        vlayout.addLayout(hlayout2)

        self.setLayout(vlayout)

    def refreshList(self):
        self.subsList.clear()
        for file in os.listdir('./audioDatas/'):
            if file.endswith('.pickle'):
                self.subsList.addItem(file)

    def removeCapsule(self):
        if len(self.subsList.selectedItems()) > 0:
            ret = QMessageBox.question(self, '자막 캡슐 제거', "자막 캡슐 {}를 제거하시겠습니까?".format(self.subsList.currentItem().text()), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ret == QMessageBox.Yes:
                os.remove('./audioDatas/{}'.format(self.subsList.currentItem().text()))
                self.refreshList()
        else:
            QMessageBox.information(self, '자막 캡슐 제거', '제거할 캡슐을 선택해 주세요.')

    def addCapsule(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Pickle Files (*.pickle)", options=options)
        if fileName:
            copyfile(fileName, './audioDatas/' + os.path.basename(fileName))
            self.refreshList()



class SettingTransManager(QWidget):

    def __init__(self):
        super().__init__()

        vlayout = QVBoxLayout()

        group1 = QGroupBox('번역 캡슐 목록')

        hlayout1 = QHBoxLayout()
        hlayout2 = QHBoxLayout()

        self.subsList = QListWidget()
        for file in os.listdir('./screenDatas/'):
            if file.endswith('.pickle'):
                self.subsList.addItem(file)
        hlayout1.addWidget(self.subsList)

        group1.setLayout(hlayout1)
        vlayout.addWidget(group1)

        button1 = QPushButton('번역 캡슐 제거')
        button1.clicked.connect(self.removeCapsule)
        button2 = QPushButton('번역 캡슐 추가')
        button2.clicked.connect(self.addCapsule)

        hlayout2.addStretch(1)
        hlayout2.addWidget(button1)
        hlayout2.addWidget(button2)

        vlayout.addLayout(hlayout2)

        self.setLayout(vlayout)

    def refreshList(self):
        self.subsList.clear()
        for file in os.listdir('./screenDatas/'):
            if file.endswith('.pickle'):
                self.subsList.addItem(file)

    def removeCapsule(self):
        if len(self.subsList.selectedItems()) > 0:
            ret = QMessageBox.question(self, '번역 캡슐 제거',
                                       "번역 캡슐 {}를 제거하시겠습니까?".format(self.subsList.currentItem().text()),
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if ret == QMessageBox.Yes:
                os.remove('./screenDatas/{}'.format(self.subsList.currentItem().text()))
                self.refreshList()
        else:
            QMessageBox.information(self, '번역 캡슐 제거', '제거할 캡슐을 선택해 주세요.')

    def addCapsule(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "Pickle Files (*.pickle)", options=options)
        if fileName:
            copyfile(fileName, './screenDatas/' + os.path.basename(fileName))
            self.refreshList()

class SettingWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('설정')
        layout = QGridLayout()
        self.tab = TabWidget()
        self.tab.addTab(SettingScreen(), QtGui.QIcon("./icons/comment.png"), 'Screen 번역')
        self.tab.addTab(SettingAudio(), QtGui.QIcon("./icons/comment.png"), 'Audio 자막')
        self.tab.addTab(SettingSubsManager(), QtGui.QIcon("./icons/database.png"), '자막 관리')
        self.tab.addTab(SettingTransManager(), QtGui.QIcon("./icons/database.png"), '번역 관리')
        self.resize(800, 500)
        layout.addWidget(self.tab, 0, 0)
        self.setLayout(layout)