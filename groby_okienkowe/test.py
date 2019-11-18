try:
    import Tkinter as tk
    import tkFont
#    import ttk  # not used here
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
#    import tkinter.ttk as ttk  # not used here

class App:
    def __init__(self):
        root=tk.Tk()
        # create a custom font
        self.customFont = tkFont.Font(family="Helvetica", size=12)

        # create a couple widgets that use that font
        buttonframe = tk.Frame()
        label = tk.Label(root, text="Hello, world", font=self.customFont)
        text = tk.Text(root, width=20, height=2, font=self.customFont)
        buttonframe.pack(side="top", fill="x")
        label.pack()
        text.pack()
        text.insert("end","press +/- buttons to change\nfont size")

        # create buttons to adjust the font
        bigger = tk.Button(root, text="+", command=self.OnBigger)
        smaller = tk.Button(root, text="-", command=self.OnSmaller)
        bigger.pack(in_=buttonframe, side="left")
        smaller.pack(in_=buttonframe, side="left")

        root.mainloop()

    def OnBigger(self):
        '''Make the font 2 points bigger'''
        size = self.customFont['size']
        self.customFont.configure(size=size+2)

    def OnSmaller(self):
        '''Make the font 2 points smaller'''
        size = self.customFont['size']
        self.customFont.configure(size=size-2)

app=App()
