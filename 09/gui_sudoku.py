import tkinter as tk
import random
import tkinter.font as font

HEIGHT=2
WIDTH=11
BD=3
FONT_SIZE=18

LST=None
level=30

global podpowiedzi
podpowiedzi=0

dane={}
original_dane={}
dane_start_gry={}
yes_or_not={}

labe=[]
btns=[]
removed=[]

def fn(btn):
    global podpowiedzi
    global last_clicked
    st=str(btn)
    x=st[12]
    if x=='.':
        x=1
        try:
            y=st[20]
        except:
            y=1
        res=str(x)+str(y)
        last_clicked=res
        
    else:    
        try:
            y=st[21]
        except:
            y=1
        res=str(x)+str(y)
       # print(res)

        last_clicked=res

    change_color(dane[int(last_clicked)], last_clicked)   
    return last_clicked
    
       
def fn2(btn):
    global podpowiedzi
    st=str(btn)
    x=st[12]
    y=st[13]
    res=str(x)+str(y)
    res=int(res)-9
    global last_clicked
    if yes_or_not[int(last_clicked)]==1:
        dane[int(last_clicked)]=str(res)
        buttons[int(last_clicked)].configure(text=res)
        change_color(dane[int(last_clicked)],last_clicked)


def change_color(n, lc):
    global podpowiedzi
    index=[i for i in range(10,100) if i%10!=0]
    global LST
    if podpowiedzi==1:
        for j in index:
            buttons[j].configure(background="light blue")
            if dane[j]==str(n) and dane[j]!=' ':
                buttons[j].configure(background="steel blue")
                LST=n
            elif dane[j]==' ':
                index2=[i for i in range(10,100) if i%10!=0]
                for k in index2:
                    buttons[k].configure(background="light blue")
                    if dane[k]==str(LST):
                       buttons[k].configure(background="steel blue")

    else:
        for j in index:
            buttons[j].configure(background="light blue")

    buttons[int(lc)].configure(background="chartreuse3")
    
    
def make_sudoku():
    #from stackoverflow
    base  = 3
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
 
    
    index=[i for i in range(10,100) if i%10!=0]
    ix=[]
    for i in range(3):
        for j in range(3):
            x=(i,j)
            ix.append(x)
    for i in range(3):
        for j in range(3,6):
            x=(i,j)
            ix.append(x)
    for i in range(3):
        for j in range(6,9):
            x=(i,j)
            ix.append(x)
            
    for i in range(3,6):
        for j in range(3):
            x=(i,j)
            ix.append(x)
    for i in range(3,6):
        for j in range(3,6):
            x=(i,j)
            ix.append(x)
    for i in range(3,6):
        for j in range(6,9):
            x=(i,j)
            ix.append(x)
            
    for i in range(6,9):
        for j in range(3):
            x=(i,j)
            ix.append(x)
    for i in range(6,9):
        for j in range(3,6):
            x=(i,j)
            ix.append(x)
    for i in range(6,9):
        for j in range(6,9):
            x=(i,j)
            ix.append(x)
            
    for i, j in zip(index, ix):
        dane[i]=str(board[j[0]][j[1]])
        original_dane[i]=str(board[j[0]][j[1]])
    
    index=[i for i in range(10,100) if i%10!=0]
    for j in index:
        yes_or_not[j]=0
   

def remove_some_data(n):
    global removed
    for j in range(n):
        index=[i for i in range(10,100) if i%10!=0]
        ix=random.choice(index)
        if dane[ix]==' ':
            remove_some_data(1)
         
        dane[ix]=' '
        removed.append(ix)
        yes_or_not[ix]=1
     

def usun():
    try:
        if yes_or_not[int(last_clicked)]==1:
            dane[int(last_clicked)]=' ' 
            buttons[int(last_clicked)].configure(text=' ')
            index=[i for i in range(10,100) if i%10!=0]
            for j in index:
                buttons[j].configure(background="light blue")
            buttons[int(last_clicked)].configure(background="chartreuse3")
    
    except:
        pass

def fnct():
    xd=tk.Toplevel()
    xd.title('Spróbuj jeszcze raz!')
    xd.geometry('450x300+400+300')
    tk.Label(xd, text="Rozwiązanie niepoprawne.").place(x=150,y=50)
    ok=tk.Button(xd, text="OK", height=HEIGHT, width=WIDTH,bd=BD, command=lambda:xd.destroy(), background="light blue", activebackground="gold2")
    ok.place(x=175,y=150)

def fnct_good():
    xd=tk.Toplevel()
    xd.title('Gratulacje!')
    xd.geometry('450x300+400+300')
    tk.Label(xd, text="Rozwiązanie poprawne.").place(x=150,y=50)
    ok=tk.Button(xd, text="OK", height=HEIGHT, width=WIDTH,bd=BD, command=lambda:xd.destroy(), background="light blue", activebackground="gold2")
    ok.place(x=175,y=150)
    
def ckeck_one_more_time(): #dziala sprawdzanie w kwadratach
    indeksy=[i for i in range (11,100,10)]
    wzor=[j for j in range(1,10)]
    for b in indeksy:
        index=[k for k in range(b,b+9)]
        tmp=[]
        for j in index: 
            tmp.append(dane[j])
        tmp.sort()
    
        for m in range(9):
          #  print(tmp[m], wzor[m])
            if str(tmp[m])!=str(wzor[m]):
                fnct()
                return

    fr=[1,2,3]
    sr=[4,5,6]
    tr=[7,8,9]
    wzor=[j for j in range(1,10)]

    tab=[]
    tab.append(fr)
    tab.append(sr)
    tab.append(tr)

    for l in range(3):
        for k in range(3):
            tmp=[]
            for i in range(3):
                for j in range(3):
                    x=str(tab[l][i])
                    y=str(tab[k][j])
                    z=x+y
                    tmp.append(int(z))
            tmp.sort()
            tmp_data=[]
            for q in tmp:
                tmp_data.append(dane[q])
            tmp_data.sort()
            for w in range(9):
                if str(tmp_data[w])!= str(wzor[w]):
                    fnct()
                    return
## wiersze
    fr=[1,4,7]
    sr=[2,5,8]
    tr=[3,6,9]
    wzor=[j for j in range(1,10)]

    tab=[]
    tab.append(fr)
    tab.append(sr)
    tab.append(tr)
    
    for l in range(3):
        for k in range(3):
            tmp=[]
            for i in range(3):
                for j in range(3):
                    x=str(tab[l][i])
                    y=str(tab[k][j])
                    z=x+y
                    tmp.append(int(z))
            tmp.sort()
            tmp_data=[]
            for q in tmp:
                tmp_data.append(dane[q])
            tmp_data.sort()
            for w in range(9):
                if str(tmp_data[w])!= str(wzor[w]):
                    fnct()
                    return
    
    fnct_good()
    return
          
    
    

def ok():
    index=[i for i in range(10,100) if i%10!=0]
    for i in index:
        if dane[i]!=original_dane[i]:
            ckeck_one_more_time()
            return

    xd=tk.Toplevel()
    xd.title('Gratulacje!')
    xd.geometry('450x300+400+300')
    tk.Label(xd, text="Rozwiązanie poprawne!").place(x=150,y=50)
    ok=tk.Button(xd, text="OK", height=HEIGHT, width=WIDTH,bd=BD, command=lambda:xd.destroy(), background="light blue", activebackground="gold2")
    ok.place(x=175,y=150)
    
def exiiit(wnd):
    win=tk.Toplevel()
    win.title("Zakończ")
    win.geometry("450x300+400+300")
    anuluj=tk.Button(win, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:win.destroy(),background="light blue", activebackground="gold2")
    ok=tk.Button(win, text="Zakończ", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:wnd.destroy(), background="light blue", activebackground="gold2")
    tk.Label(win, text="Zakończyć? Bieżąca gra zostanie utracona.").place(x=30,y=50)
    ok.place(x=80, y=150)
    anuluj.place(x=250, y=150)

def odnowa():

    win=tk.Toplevel()
    win.title("Rozpocząć od nowa?")
    win.geometry("450x300+400+300")
    anuluj=tk.Button(win, text="Nie", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:win.destroy(),background="light blue", activebackground="yellow")
    ok=tk.Button(win, text="Tak", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:once_again(win), background="light blue", activebackground="yellow")
    tk.Label(win, text="Rozpocząć od nowa? Bieżąca gra zostanie utracona.").place(x=60,y=50)
    ok.place(x=80, y=150)
    anuluj.place(x=250, y=150)

def once_again(win):
    global removed
    index=[i for i in range(10,100) if i%10!=0]
    for i in index:
        dane[i]=original_dane[i]
        buttons[i].configure(text=str(dane[i]))
    win.destroy()
    for j in removed:
        dane[j]=' '
        buttons[j].configure(text=' ')
    
def nowa_gra():
    win=tk.Toplevel()
    win.title("Rozpocząć od nowa?")
    win.geometry("450x300+400+300")
    anuluj=tk.Button(win, text="Nie", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:win.destroy(),background="light blue", activebackground="yellow")
    ok=tk.Button(win, text="Tak", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:nowa_gra_backend(win), background="light blue", activebackground="yellow")
    tk.Label(win, text="Rozpocząć nową rozgrywkę? Bieżąca gra zostanie utracona.").place(x=30,y=50)
    ok.place(x=80, y=150)
    anuluj.place(x=250, y=150)

def ng(n, win):
    global level
    if n==1:
        level=10
    elif n==2:
        level=20
    elif n==3:
        level=30
    elif n==4:
        level=40
    elif n==5:
        level=50
    win.destroy()
       
    make_sudoku()
    index=[i for i in range(10,100) if i%10!=0]
    global removed
    removed=[]
    remove_some_data(level)
    for i in index:
        buttons[i].configure(text=str(dane[i]))
        buttons[i].configure(background="light blue")
    
def nowa_gra_backend(win):
    win.destroy()
    global level

    okno=tk.Toplevel()
    okno.title("Wybierz poziom trudności")
    okno.geometry("450x300+400+300")
    t1=tk.Button(okno, command=lambda:ng(1,okno), text="Amator", height=HEIGHT, width=WIDTH,bd=BD,background="green2", activebackground="yellow")
    t2=tk.Button(okno, command=lambda:ng(2,okno), text="Łatwy", height=HEIGHT, width=WIDTH,bd=BD, background="OliveDrab1", activebackground="yellow")
    t3=tk.Button(okno, command=lambda:ng(3,okno), text="Średni", height=HEIGHT, width=WIDTH,bd=BD, background="light blue", activebackground="yellow")
    t4=tk.Button(okno, command=lambda:ng(4,okno), text="Trudny", height=HEIGHT, width=WIDTH,bd=BD, background="orange", activebackground="yellow")
    t5=tk.Button(okno, command=lambda:ng(5,okno), text="Ekspert", height=HEIGHT, width=WIDTH,bd=BD, background="red", activebackground="yellow")
    tk.Label(okno, text="Wybierz poziom trudności").place(x=150,y=10)
    t1.place(x=175, y=40)
    t2.place(x=175, y=90)
    t3.place(x=175, y=140)
    t4.place(x=175, y=190)
    t5.place(x=175, y=240)

 
      

def pdp():
    global podpowiedzi
    global last_clicked
    if podpowiedzi==0:
        podpowiedzi=1
        index=[i for i in range(10,100) if i%10!=0]
        global LST
        for j in index:
            buttons[j].configure(background="light blue")
            if dane[j]==str(dane[int(last_clicked)]) and dane[j]!=' ':
                buttons[j].configure(background="steel blue")
                LST=str(dane[int(last_clicked)])
        buttons[int(last_clicked)].configure(background="chartreuse3")
        return

    elif podpowiedzi==1:
        podpowiedzi=0
        index=[i for i in range(10,100) if i%10!=0]
        for j in index:
            buttons[j].configure(background="light blue")
        buttons[int(last_clicked)].configure(background="chartreuse3")
        return

def main():
    global podpowiedzi
    make_sudoku()

    remove_some_data(level)
    
    dane_start_gry=dane
    window=tk.Tk()
    window.title("Sudoku by M")
    window.geometry("1024x768+0+0")
    menu=tk.Label(bg="dark blue")
    window.configure(background="light yellow")

    ix=[i for i in range(9)]
    game=[]
    for i in ix:
        game.append(tk.LabelFrame(height=12, width=27,bg='dark blue',  padx=2, pady=2))

              
    p1=tk.Button(menu,text="Nowa gra", height=HEIGHT, width=WIDTH, bd=BD, background='light blue', activebackground="gold2", command=lambda:nowa_gra() )
    p2=tk.Button(menu,text="Od nowa", height=HEIGHT, width=WIDTH, bd=BD,background='light blue', activebackground="gold2", command=lambda:odnowa())
    p3=tk.Button(menu,text="Rekordy", state='disabled',height=HEIGHT, width=WIDTH,background='light blue', bd=BD, activebackground="gold2")
    p4=tk.Button(menu,text="Wyjście", height=HEIGHT, width=WIDTH,background='light blue', bd=BD, activebackground="gold2", command=lambda:exiiit(window))
    chck=tk.Checkbutton(window, text="Włącz podpowiedzi",bg='light blue', height=2,activebackground="gold2", command=lambda:pdp())

    for k in range(9):
        labe.append(tk.LabelFrame(window,width=74,height=70, bg='dark blue', bd=BD+2))
        labe[k].grid_rowconfigure(0, weight=1)
        labe[k].grid_columnconfigure(0, weight=1)    
        labe[k].grid_propagate(False)
        labe[k].place(x=277+k*69,y=660)
        obj=(tk.Button(labe[k], activeforeground='dark blue', text=k+1,font=('Helvetica',FONT_SIZE), background="light blue",activebackground="gold2"))
        obj.configure(command=lambda btn=obj:fn2(btn))
        btns.append(obj)
        btns[k].grid(row=0,column=0, sticky='nesw')

    usun_frame=tk.LabelFrame(window,width=70,height=70, bg='dark blue')
    usun_frame.grid_rowconfigure(0, weight=1)
    usun_frame.grid_columnconfigure(0, weight=1)
    usun_frame.grid_propagate(False)
    usun_frame.place(x=925, y=571)
    obj=(tk.Button(usun_frame, activeforeground='dark blue', text='Usuń',font=('Helvetica',FONT_SIZE), background="light blue",activebackground="gold2"))
    obj.configure(command=lambda btn=obj:usun())
    obj.grid(row=0, column=0, sticky='nesw')

    ok_frame=tk.LabelFrame(window,width=125,height=70, bg='dark blue')
    ok_frame.grid_rowconfigure(0, weight=1)
    ok_frame.grid_columnconfigure(0, weight=1)
    ok_frame.grid_propagate(False)
    ok_frame.place(x=20, y=571)
    obj=(tk.Button(ok_frame, activeforeground='dark blue', text='Zatwierdź',font=('Helvetica',FONT_SIZE), background="light blue",activebackground="gold2"))
    obj.configure(command=lambda btn=obj:ok())
    obj.grid(row=0, column=0, sticky='nesw')

    pdp_frame=tk.LabelFrame(window,width=125,height=70, bg='dark blue')
    pdp_frame.grid_rowconfigure(0, weight=1)
    pdp_frame.grid_columnconfigure(0, weight=1)
    pdp_frame.grid_propagate(False)
    pdp_frame.place(x=20, y=470)
    obj=tk.Checkbutton(pdp_frame, text="Włącz \n podpowiedzi",bg='light blue', height=2,activebackground="gold2", command=lambda:pdp())
    obj.configure(command=lambda: pdp())
    obj.grid(row=0, column=0, sticky='nesw')
    
    for i in ix:
        if i%3==0:
            game[i].place(x=276, y=51+i*65)
        elif i%3==1:
            game[i].place(x=484, y=35-49+i*65)
        elif i%3==2:
            game[i].place(x=692, y=i*65-31-48)

    index=[i for i in range(10,100) if i%10!=0]

    global buttons
    buttons={}
    
    pixel = tk.PhotoImage(width=1, height=1)
    for i in index:
        quad=i//10-1
        try:
            txt=dane[i][0]
        except:
            txt='xd'

        obj=tk.Button(game[quad], text=txt, compound='c',font=('Helvetica',FONT_SIZE),image=pixel,width=40, height=50, background="light blue",activebackground="gold2")
        obj.configure(command=lambda btn=obj:fn(btn))
        buttons[i]=obj

    for i in index:
        if i%10==1:
            buttons[i].grid(row=1, column=1)
        elif i%10==2:
            buttons[i].grid(row=1, column=2)
        elif i%10==3:
            buttons[i].grid(row=1, column=3)
        elif i%10==4:
            buttons[i].grid(row=2, column=1)
        elif i%10==5:
            buttons[i].grid(row=2, column=2)
        elif i%10==6:
            buttons[i].grid(row=2, column=3)
        elif i%10==7:
            buttons[i].grid(row=3, column=1)
        elif i%10==8:
            buttons[i].grid(row=3, column=2)
        elif i%10==9:
            buttons[i].grid(row=3, column=3)
            
    
    menu.place(x=20, y=51)
    p1.grid(row=1, column=1)
    p2.grid(row=2, column=1)
    p3.grid(row=3, column=1)
    p4.grid(row=4, column=1)

    window.mainloop()
 
main()
