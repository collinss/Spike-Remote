from tkinter import *
from tkinter import ttk

from spike import SpikeMessenger

class MainWindow(Tk):
    """ main window for controlling the robot """
    def __init__(self):
        super(MainWindow, self).__init__()

        self.spike_messenger = SpikeMessenger()

        frm = ttk.Frame(self, padding=10)
        frm.grid()
        ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
        ttk.Button(frm, text="\u2190", command=self.move_left).grid(column=1, row=0)
        ttk.Button(frm, text="\u2191", command=self.move_up).grid(column=2, row=0)
        ttk.Button(frm, text="\u2192", command=self.move_right).grid(column=3, row=0)
        ttk.Button(frm, text="\u2193", command=self.move_down).grid(column=4, row=0)
        ttk.Button(frm, text="Quit", command=self.destroy).grid(column=5, row=0)
        self.bind('<Left>', self.move_left)
        self.bind('<Right>', self.move_right)
        self.bind('<Up>', self.move_up)
        self.bind('<Down>', self.move_down)
        self.mainloop()

    def move_up(self, *args):
        self.spike_messenger.move(100, 0)

    def move_down(self, *args):
        self.spike_messenger.move(-100, 0)

    def move_left(self, *args):
        self.spike_messenger.move(100, -100)

    def move_right(self, *args):
        self.spike_messenger.move(100, 100)

if __name__ == "__main__":
    MainWindow()
