from ahk import AHK


class WindowWatcher:
    def __init__(self, watch_list=None):
        self.watch_list = watch_list

    @property
    def active_window(self):
        ahk = AHK()
        return ahk.active_window

    def check_for_match(self):
        """Checks if active window has a match in match list

        :return:
        :rtype: bool
        """
        if self.active_window.process in self.watch_list:
            return True
        else:
            return False
