import tkinter as tk
import groby_rysowanko as groby
import pickle
HEIGHT=3
WIDTH=15
BD=3


def start(*args):

    name=args[0].get()
    i1=int(args[1].get())
    i2=int(args[2].get())
    print(i1,i2,name)
    args[3].destroy()
    i3=groby.kwartal(i1,i2)
    print(i3)
    with open(name, "wb") as internal_filename:
        pickle.dump(i3, internal_filename)

def okienko_kwatera():
    window = tk.Toplevel()
    window.title("Dodaj kwaterę")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:start(e1,e2,e3,window), background="green", activebackground="yellow")
    name=tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    height=tk.Label(window, text="Ilość wierszy").place(x=30,y=80)
    width=tk.Label(window, text="Ilość kolumn").place(x=30,y=110)
    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)
 
    e1.place(x=150,y=50)
    e2.place(x=150,y=80)
    e3.place(x=150,y=110)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)


def wykop_dolki():
    window = tk.Toplevel()
    window.title("Wykop dołek")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:start_koparka(e1,e2,e3,window), background="green", activebackground="yellow")
    name=tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    height=tk.Label(window, text="Numer wiersza").place(x=30,y=80)
    width=tk.Label(window, text="Numer kolumny").place(x=30,y=110)
    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)
 
    e1.place(x=150,y=50)
    e2.place(x=150,y=80)
    e3.place(x=150,y=110)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def start_koparka(*args):
    name=args[0].get()
    i1=int(args[1].get())
    i2=int(args[2].get())
    print(i1,i2,name)
    args[3].destroy()
    with open(name, "rb") as new_filename:
        pp = pickle.load(new_filename)
    print(pp)
    i3=groby.koparka(pp,i1,i2)
    print(i3)
    with open(name, "wb") as internal_filename:
        pickle.dump(i3, internal_filename)

def rozgwiazda():
    window = tk.Toplevel()
    window.title("Zakop rozgwiazdę")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:start_rozgwiazda(e1,e2,e3,e4,window), background="green", activebackground="yellow")
    tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    tk.Label(window, text="Numer wiersza").place(x=30,y=80)
    tk.Label(window, text="Numer kolumny").place(x=30,y=110)
    tk.Label(window,text="Ilość ramion").place(x=30,y=140)
    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)
    e4 = tk.Entry(window)
 
    e1.place(x=150,y=50)
    e2.place(x=150,y=80)
    e3.place(x=150,y=110)
    e4.place(x=150,y=140)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def start_rozgwiazda(*args):
    name=args[0].get()
    i1=int(args[1].get())
    i2=int(args[2].get())
    i3=int(args[3].get())
    args[4].destroy()
    with open(name, "rb") as new_filename:
        pp = pickle.load(new_filename)
    print(pp)
    
    i5=groby.zakop_rozgwiazde(pp,i1,i2,i3)
    print(i5)
    with open(name, "wb") as internal_filename:
        pickle.dump(i5, internal_filename)


def slimak():
    window = tk.Toplevel()
    window.title("Zakop ślimaka")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:start_slimak(e1,e2,e3,e4,e5,window), background="green", activebackground="yellow")
    tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    tk.Label(window, text="Numer wiersza").place(x=30,y=80)
    tk.Label(window, text="Numer kolumny").place(x=30,y=110)
    tk.Label(window,text="Średnica").place(x=30,y=140)
    tk.Label(window,text="Ilość zwojów").place(x=30,y=170)
    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)
    e4 = tk.Entry(window)
    e5 = tk.Entry(window)
 
    e1.place(x=150,y=50)
    e2.place(x=150,y=80)
    e3.place(x=150,y=110)
    e4.place(x=150,y=140)
    e5.place(x=150,y=170)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def start_slimak(*args):
    name=args[0].get()
    i1=int(args[1].get())
    i2=int(args[2].get())
    i3=int(args[3].get())
    i4=int(args[4].get())
    args[5].destroy()
    with open(name, "rb") as new_filename:
        pp = pickle.load(new_filename)
    print(pp)
    
    i5=groby.zakop_slimaka(pp,i1,i2,i3,i4)
    print(i5)
    with open(name, "wb") as internal_filename:
        pickle.dump(i5, internal_filename)


def rysuj():
    window = tk.Toplevel()
    window.title("Rysuj")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:rysuj_cmentarz(e1,window), background="green", activebackground="yellow")
    tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    e1 = tk.Entry(window)
  
    e1.place(x=150,y=50)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def rysuj_cmentarz(arg1, window):

    arg=str(arg1.get())
    with open(arg, "rb") as new_filename:
        pp = pickle.load(new_filename)
    print(pp)
    groby.rysuj(pp)
    window.destroy()

def statystyki(win):
    window = tk.Toplevel()
    window.title("Statystyki")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:stats(e1,window,win), background="green", activebackground="yellow")
    tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    e1 = tk.Entry(window)
  
    e1.place(x=150,y=50)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def stats(e1, window, win):
    name=str(e1.get())
    window.destroy()
    with open(name, "rb") as new_filename:
        pp = pickle.load(new_filename)
    
    stat=groby.statystyki(pp)
    #win.insert(END,stat+"\n")
    print(stat)
    
    
def print_obj():

    window = tk.Toplevel()
    window.title("Print")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:prt(e1,window), background="green", activebackground="yellow")
    tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    e1 = tk.Entry(window)
  
    e1.place(x=150,y=50)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def prt(e1, window):
    name=str(e1.get())
    window.destroy()
    with open(name, "rb") as new_filename:
        pp = pickle.load(new_filename)
    print(pp)
    

def main():
    o=tk.Tk()
    o.title("Cmentarz by M")
    o.geometry("640x580+0+0")

    out=tk.Text(width=50, height=10, bg="grey")
    p1=tk.Button(o, text="Dodaj kwaterę",height=HEIGHT, width=WIDTH,bd=BD,activebackground="yellow",\
             command=okienko_kwatera)
    p2=tk.Button(o, text="Wykop dołek",height=HEIGHT, width=WIDTH,bd=BD,activebackground="yellow",\
             command=wykop_dolki)
    p3=tk.Button(o, text="Zakop rozgwiazdę",height=HEIGHT, width=WIDTH,bd=BD,activebackground="yellow",\
             command=rozgwiazda)
    p4=tk.Button(o, text="Zakop ślimaka", height=HEIGHT, width=WIDTH,bd=BD,activebackground="yellow",\
             command=slimak)
    p5=tk.Button(o, text="Rysuj to gówno!",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=rysuj)
    p6=tk.Button(o, text="Statystyki",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=lambda:statystyki(out))
    p7=tk.Button(o, text="Coming soon",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=print_obj)
    p8=tk.Button(o, text="Zakończ",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=o.destroy)
    
    
    p1.grid(row=1,column=1)
    p2.grid(row=2,column=1)
    p3.grid(row=3,column=1)
    p4.grid(row=4,column=1)
    p5.grid(row=5,column=1)
    p6.grid(row=6,column=1)
    p7.grid(row=7,column=1)
    p8.grid(row=8,column=1)
    out.grid(row=2,column=2,rowspan=3, padx=40)
    

    o.mainloop()

    

main()
