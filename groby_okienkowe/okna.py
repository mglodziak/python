# -*- coding: utf-8 -*-
import tkinter as tk
import groby_rysowanko as groby
import groby_rysowanko_fast as fast
import pickle
HEIGHT=3
WIDTH=15
BD=3
global FONT_SIZE
FONT_SIZE=14


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
            args[3].destroy()
            if i1>11:
                error("Niepoprawny rozmiar kwatery. Max x=11")
            elif i1<1:
                error("Niepoprawny rozmiar kwatery. Min x=1")
            elif i2>11:
                error("Niepoprawny rozmiar kwatery. Max y=11")
            elif i2<1:
                error("Niepoprawny rozmiar kwatery. Min y=1")
            else:
                i3=groby.kwartal(i1,i2)
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
            
        else:
            try:
                with open(name, "rb") as new_filename:
                    pp = pickle.load(new_filename)
            except:
                error("Kwatera nie instnieje")
            else:
                if i1<0:
                    error("Współrzędna x nie może być ujemna!")
                elif i2<0:
                    error("Współrzędna y nie może być ujemna!")
                else:                    
                    i3=groby.koparka(pp,i1,i2)
                    args[3].destroy()
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
                    i5=groby.zakop_rozgwiazde(pp,i1,i2,i3)
                    if i5==1:
                        error("Wykop tutaj najpierw dołek!")
                    elif i5==2:
                        error("Tu już jest coś zakopane!")
                    elif i3==100:
                        error("Podałeś niepoprawne dane!")
                    else:
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
        
def rysuj_fast():
    window = tk.Toplevel()
    window.title("Rysuj")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:rysuj_cmentarz_fast(e1,window), background="green", activebackground="yellow")
    tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    e1 = tk.Entry(window)
  
    e1.place(x=150,y=50)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def rysuj_cmentarz_fast(arg1, window):

    arg=str(arg1.get())
    try:
        with open(arg, "rb") as new_filename:
            pp = pickle.load(new_filename)
    except:
        error("Podana kwatera nie istnieje!")
        window.destroy()
    else:
        fast.rysuj(pp)
        window.destroy()

def statystyki(win, main):
    window = tk.Toplevel()
    window.title("Statystyki")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:stats(e1,window,win,main), background="green", activebackground="yellow")
    tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    e1 = tk.Entry(window)
  
    e1.place(x=150,y=50)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def stats(e1, window, win, main):
    name=str(e1.get())
    try:
        with open(name, "rb") as new_filename:
            pp = pickle.load(new_filename)
    except:
        error("Podana kwatera nie istnieje!")
        window.destroy()
    else:
        global file
        file=name
        print(file)
        drukuj(main)
        window.destroy() 
        
##        win.delete(1.0,tk.END)
##        stat=groby.statystyki(pp)
##        i=4
##        while i>=0:
##            win.insert(1.0,list(stat.values())[i])
##            win.insert(1.0,": ")
##            win.insert(1.0,list(stat)[i])
##            win.insert(1.0,"\n")
##            i=i-1
##        win.insert(1.0,"\n")
##        win.insert(1.0, name)
##        win.insert(1.0, "Kwatera: ")
##        window.destroy()    
    
def print_obj(win):
    window = tk.Toplevel()
    window.title("Print")
    window.geometry("400x400+250+100")
    anuluj=tk.Button(window, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:window.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(window, text="OK", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:prt(e1,window,win), background="green", activebackground="yellow")
    tk.Label(window, text="Nazwa kwatery").place(x=30,y=50)
    e1 = tk.Entry(window)
  
    e1.place(x=150,y=50)
    ok.place(x=30,y=250)
    anuluj.place(x=220,y=250)

def prt(e1, window,win):
    name=str(e1.get())
    window.destroy()
    try:
        with open(name, "rb") as new_filename:
            pp = pickle.load(new_filename)
    except:
        error("Podana kwatera nie istnieje!")
    else:
        win.delete(1.0,tk.END)
        win.insert(1.0,pp)



def drukuj(out):
    try:
        with open(file, "rb") as new_filename:
            pp = pickle.load(new_filename)
    except:
        frame=tk.Frame(out, width=10, height=50)
        d1=tk.Label(frame, text="dupa", bg="grey",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
        d1.pack()
    else:
        frame=tk.Frame(out, width=10, height=50)
        stat=groby.statystyki(pp)

        str1=str(list(stat)[0])
        str2=str(list(stat.values())[0])
        str3=str1+": "+str2
        str4=str(list(stat)[1])
        str5=str(list(stat.values())[1])
        str6=str4+": "+str5
        str7=str(list(stat)[2])
        str8=str(list(stat.values())[2])
        str9=str7+": "+str8
        str10=str(list(stat)[3])
        str11=str(list(stat.values())[3])
        str12=str10+": "+str11
        str13=str(list(stat)[4])
        str14=str(list(stat.values())[4])
        str15=str13+": "+str14
        
        d1=tk.Label(frame, text=str3, bg="grey",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
        d2=tk.Label(frame, text=str6, bg="grey",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
        d3=tk.Label(frame, text=str9, bg="grey",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
        d4=tk.Label(frame, text=str12, bg="grey",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
        d5=tk.Label(frame, text=str15, bg="grey",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
        d01=tk.Label(frame, text=' ', bg="grey",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
        
        frame.place(x=0,y=0)    
        d1.pack()
        d2.pack()
        d3.pack()
        d4.pack()
        d5.pack()
        d01.pack()

##def drukuj2(out):
##    frame=tk.Frame(out, width=10, height=50)
##    dupa1=tk.Label(frame, text="dupa\n xx\ndd\nff", bg="red",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
##    dupa2=tk.Label(frame, text="xddx", bg="green",anchor='nw', width=50, height=1, font=("Helvetica",FONT_SIZE))
##    frame.place(x=0,y=0)    
##    dupa1.pack()
##    dupa2.pack()


def plus(arg, out):
    #8-25
    if arg<25:
        arg=arg+2
    global FONT_SIZE
    FONT_SIZE=arg
    drukuj(out)
    print(FONT_SIZE)
    #return FONT_SIZE

def minus(arg, out):
    if arg>9:
        arg=arg-2
    global FONT_SIZE
    FONT_SIZE=arg
    drukuj(out)
    print(FONT_SIZE)
    
    #return FONT_SIZE

def main():
    o=tk.Tk()
    
    o.title("Cmentarz by M")
    o.geometry("640x552+0+0")

    #out=tk.Text( width=50, height=15,bg="light grey")#, font=("Helvetica",11))
    out=tk.Label( width=50, height=15, bg="grey")#, font=("Helvetica",11))
        
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
    p6=tk.Button(o, text="Rysuj kwaterę szybko",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=rysuj_fast)
    p7=tk.Button(o, text="Statystyki",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=lambda:statystyki(out,out))
    #p8=tk.Button(o, text="Wypisz kwaterę",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             #bd=BD,command=lambda:print_obj(out))
    p9=tk.Button(o, text="Zakończ",height=HEIGHT, width=WIDTH, activebackground="yellow",\
             bd=BD,command=o.destroy)
    
    p01=tk.Button(o, text="+", height=HEIGHT//2, width=WIDTH//4, activebackground="yellow",\
             bd=BD,command=lambda:plus(FONT_SIZE, out))
    p02=tk.Button(o, text="-", height=HEIGHT//2, width=WIDTH//4, activebackground="yellow",\
             bd=BD,command=lambda:minus(FONT_SIZE, out))
    p1.grid(row=1,column=1)
    p2.grid(row=2,column=1)
    p3.grid(row=3,column=1)
    p4.grid(row=4,column=1)
    p5.grid(row=5,column=1)
    p6.grid(row=6,column=1)
    p7.grid(row=7,column=1)
    #p8.grid(row=8,column=1)
    p9.grid(row=9,column=1)
    out.grid(row=2,column=2,rowspan=4, padx=40,columnspan=2)
    drukuj(out)
        
    p01.grid(row=6, column=2, sticky=tk.E)
    p02.grid(row=6, column=3, sticky=tk.W)

    o.mainloop()
    

main()
