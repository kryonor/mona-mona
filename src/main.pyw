import os
import sys
import tkinter as tk


__version__ = 0.1


class MonaMona(object):
    def __init__(self):
        self.win = tk.Tk()
        self.win.title(f"MonaMona v{__version__}")
        self.win.geometry("1280x720") # 16:9 TODO create a field in settings for it


if __name__ == "__main__":
    app = MonaMona()
