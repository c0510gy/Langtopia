import pyautogui

class ScreenCapture(object):

    def __init__(self):
        pass

    def getScreen(self):
        capturedImage = pyautogui.screenshot()
        return capturedImage
