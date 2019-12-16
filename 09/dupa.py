import tkinter as tk

class button():
    idn=0
    btn=0
    def dupa(self):
        print(self)


window=tk.Tk()
window.title("Sudoku by M")
window.geometry("1024x768")
#menu=tk.Label(bg="black")
window.configure(background="light yellow")
#btn=tk.Button(window, text="Nowa gra", height=3, width=10, bd=2, activebackground="yellow")
#btn.grid()


x=button()
x.idn=1
x.btn=tk.Button(window, text="Nowa gra", height=3, width=10, bd=2, activebackground="yellow", command=lambda:button.dupa(x.idn))
y=button()
y.idn=10
y.btn=tk.Button(window, text="Nowa gra", height=3, width=10, bd=2, activebackground="yellow", command=lambda:button.dupa(y.idn))

x.btn.grid()
y.btn.grid()

