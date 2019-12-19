
class SettingManager(object):

    def __init__(self):
        self.screenSetting = dict()
        self.audioSetting = dict()

        self.screenSetting['font_color'] = '#008080'
        self.screenSetting['background_color'] = '#D3D3D3'
        self.screenSetting['selected_color'] = '#FFFF00'

        self.audioSetting['font_color'] = '#FFFFFF'
        self.audioSetting['background_color'] = '#000000'

settingManager = SettingManager()
