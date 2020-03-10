import os, sys, threading
sys.path.append(r"C:\Users\Lenovo\PycharmProjects\Beginner Project")

from tkinter import *
from tkinter.filedialog import askopenfilename
from Beginner.PhantomWinamp.musicPlayer import player



musicdir = r'C:\Users\Lenovo\Downloads\Music'

class Main(Frame, player):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack(fill=BOTH, expand=YES)
        self.master.title("Phantom Winamp")
        self.master.resizable(1, 0)

        self.filename = 'No file opened'

        self.makeWidgets()

    def makeWidgets(self):
        namebar = Label(self)
        namebar.config(text=self.filename, width=70, justify=CENTER)
        namebar.pack(side=LEFT)

        openbtn = Button(self)
        openbtn.config(text='Open', command=self.open, width=10)
        openbtn.pack(side=LEFT, anchor=E, expand=YES)

        self.namebar = namebar
        self.openbtn = openbtn

    def open(self):
        filename = askopenfilename(initialdir=musicdir)
        if filename:
            self.filename = os.path.basename(filename)
            self.namebar.config(text=self.filename)
            self.namebar.update()
            thread = threading.Thread(target=self.play, args=(filename,))
            thread.start()


# self-test code
if __name__ == '__main__':
    win = Tk()
    app = Main(win)
    app.mainloop()
