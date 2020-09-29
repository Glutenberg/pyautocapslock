import time

from pyautocapslock.manager import CapsLockManager
from pyautocapslock.watcher import WindowWatcher

watch_list = ["C:\\Program Files\\SOLIDWORKS Corp\\SOLIDWORKS\\SLDWORKS.exe"]

watcher = WindowWatcher(watch_list)
manager = CapsLockManager()

while True:
    if watcher.check_for_match():
        manager.set_capslock_on()
    else:
        manager.set_capslock_off()

    print(watcher.active_window.process)
    time.sleep(0.1)
