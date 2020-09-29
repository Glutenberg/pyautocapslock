from ahk import AHK


class CapsLockManager:
    def __init__(self):
        self.ahk = AHK()

    def _toggle_capslock(self):
        if self.ahk.key_state("CapsLock", "T"):
            self.ahk.set_capslock_state("off")
        else:
            self.ahk.set_capslock_state("on")

    def set_capslock_on(self):
        if self.ahk.key_state("CapsLock", "T"):
            pass
        else:
            self.ahk.set_capslock_state("on")

    def set_capslock_off(self):
        if self.ahk.key_state("CapsLock", "T"):
            self.ahk.set_capslock_state("off")
        else:
            pass
