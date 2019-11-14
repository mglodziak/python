import tkinter as tk
import groby_rysowanko as groby
import pickle
HEIGHT=3
WIDTH=15
BD=3


def start(*args):

    name=args[0].get()
    try:
        i1=int(args[1].get())
    except:
        error("Współrzędna x musi być liczbą!") ##ujemne gówno!!!
    else:
        try:
            i2=int(args[2].get())
        except:
            error("Współrzędna y musi być liczbą!")
        else:
            print(i1,i2,name)
            args[3].destroy()
            i3=groby.kwartal(i1,i2)
            #print(i3)
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

    
def error(arg):
    win = tk.Toplevel()
    win.title("BŁĄD!")
    win.geometry("400x400+250+100")
    ok=tk.Button(win, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:win.destroy(),\
                     background="green", activebackground="yellow")
    tk.Label(win, text=arg, justify='center', font="20").pack(pady=100)
    #print(arg)
    ok.place(x=125,y=250)
    
    
    
def start_koparka(*args):
    name=args[0].get()
    try:
        i1=int(args[1].get())
    except:
        error("Współrzędna x musi być liczbą!")
    else:
        try:
            i2=int(args[2].get())
    #print(i1,i2,name)
        except:
            error("Współrzędna y musi być liczbą!")
            args[3].destroy()
        else:
            try:
                with open(name, "rb") as new_filename:
                    pp = pickle.load(new_filename)
            except:
                error("Kwatera nie instnieje")
            else:
                i3=groby.koparka(pp,i1,i2)
                if i3==1:
                    error("Już tu kopałeś!")
                elif i3==2:
                    error("Trupów nie wykopujemy...")
                elif i3==100:
                    error("Podałeś niepoprawne dane!")
                else:
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
    try:
        i1=int(args[1].get())
    except:
        error("Pierwsza współrzędna musi być liczbą!")
    else:
        try:
            i2=int(args[2].get())
        except:
            error("Druga współrzędna musi być liczbą!")
        else:
            try:
                i3=int(args[3].get())
            except:
                error("Trzecia współrzędna musi być liczbą!")
            else:
                args[4].destroy()
                try:
                    with open(name, "rb") as new_filename:
                        pp = pickle.load(new_filename)
                except:
                    error("Kwatera nie instnieje")
                else:
                    #print(pp)
                    i5=groby.zakop_rozgwiazde(pp,i1,i2,i3)
                    if i5==1:
                        error("Wykop tutaj najpierw dołek!")
                    elif i5==2:
                        error("Tu już jest coś zakopane!")
                    elif i3==100:
                        error("Podałeś niepoprawne dane!")
                    else:
                        #print(i5)
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
    try:
        i1=int(args[1].get())
        i2=int(args[2].get())
        i3=int(args[3].get())
        i4=int(args[4].get())
        args[5].destroy()
    except:
        error("Parametry muszą być liczbami!")
    else:
        try:
            with open(name, "rb") as new_filename:
                pp = pickle.load(new_filename)
            #print(pp)
        except:
            error("Kwatera nie istnieje")
        else:
            i5=groby.zakop_slimaka(pp,i1,i2,i3,i4)
            if i5==1:
                error("Wykop tutaj najpierw dołek!")
            elif i5==2:
                error("Tu już jest coś zakopane!")
            elif i3==100:
                error("Podałeś niepoprawne dane!")
            else:
            #print(i5)
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
    try:
        with open(arg, "rb") as new_filename:
            pp = pickle.load(new_filename)
    except:
        error("Podana kwatera nie istnieje!")
        window.destroy()
    else:
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
    try:
        with open(name, "rb") as new_filename:
            pp = pickle.load(new_filename)
    except:
        error("Podana kwatera nie istnieje!")
        window.destroy()
    else:
        stat=groby.statystyki(pp)
    
    print(stat) ##dać to w okienku!!
    
    
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
    o.geometry("640x552+0+0")

    out=tk.Text(width=50, height=10, bg="grey")
    p1=tk.Button(o, text="Dodaj kwaterę",height=HEIGHT, width=WIDTH,bd=BD,activebackground="yellow",\
             command=okienko_kwatera)
    p2=tk.Button(o, text="Wykop dołek",height=HEIGHT, width=WIDTH,bd=BD,activebackground="yellow",\
             command=wykop_dolki)
    p3=tk.Button(o, text="Zakop rozgwiazdę",height=HEIGHT, width=WIDTH,bd=BD,activebackground="yellow",\
             command=rozgwiazda)
    p4=tk.Button(o, text="Zakop ślimaka", height=HEIGHT, width=WIDTH,bd=BD,activebackground="yellow",\
             command=slimak)
    p5=tk.Button(o, text="Rysuj kwaterę",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=rysuj)
    p6=tk.Button(o, text="Statystyki",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=lambda:statystyki(out))
    p7=tk.Button(o, text="Print",height=HEIGHT, width=WIDTH, activebackground="yellow",\
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
