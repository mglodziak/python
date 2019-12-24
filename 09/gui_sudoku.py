import tkinter as tk
import random
import tkinter.font as font

HEIGHT=2
WIDTH=11
BD=3
FONT_SIZE=18
no_to_remove=30
LST=None

global podpowiedzi
podpowiedzi=0






#fnt=tkFont.Font(size=25)

dane={}
original_dane={}
dane_start_gry={}
yes_or_not={}

labe=[]
btns=[]
#myFont = font.Font(size=30)



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
        print(res)
        last_clicked=res
     #   return last_clicked
        
    else:    
        try:
            y=st[21]
        except:
            y=1
        res=str(x)+str(y)
        print(res)

        last_clicked=res
        
    #    return last_clicked
    #print(buttons[int(last_clicked)])
    change_color(dane[int(last_clicked)], last_clicked)   
    return last_clicked
        #btn.configure(text='xd')
       
def fn2(btn):
    global podpowiedzi
    st=str(btn)
    x=st[12]
    y=st[13]
    res=str(x)+str(y)
    res=int(res)-9
    global last_clicked
    #print(last_clicked)
    if yes_or_not[int(last_clicked)]==1:
        dane[int(last_clicked)]=str(res)
        buttons[int(last_clicked)].configure(text=res)
        print(podpowiedzi)
        change_color(dane[int(last_clicked)],last_clicked)
    #print(dane)


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
               # print(LST)
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
        #print(i, j)
        dane[i]=str(board[j[0]][j[1]])
        original_dane[i]=str(board[j[0]][j[1]])
    
    print(original_dane)
    index=[i for i in range(10,100) if i%10!=0]
    for j in index:
        yes_or_not[j]=0
   

def remove_some_data(n):
    for j in range(n):
        index=[i for i in range(10,100) if i%10!=0]
        ix=random.choice(index)
        if dane[ix]==' ':
            remove_some_data(1)
         
        dane[ix]=' '
        yes_or_not[ix]=1
     

def usun():
    try:
        if yes_or_not[int(last_clicked)]==1:
            dane[int(last_clicked)]=' ' 
            buttons[int(last_clicked)].configure(text=' ')
    except:
        pass


def ok():
    index=[i for i in range(10,100) if i%10!=0]
    for i in index:
        if dane[i]!=original_dane[i]:
            print("źle")
            return
       # print(original_dane[i])
    print('dobrze')

def exiiit(wnd):
    win=tk.Toplevel()
    win.title("Zakończ")
    win.geometry("450x300+400+300")
    anuluj=tk.Button(win, text="Anuluj", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:win.destroy(),background="red", activebackground="yellow")
    ok=tk.Button(win, text="Zakończ", height=HEIGHT, width=WIDTH,bd=BD,\
                     command=lambda:wnd.destroy(), background="green", activebackground="yellow")
    tk.Label(win, text="Zakończyć? Wszelkie niezapisany zmiany zostaną utracone.").place(x=30,y=50)
    ok.place(x=80, y=150)
    anuluj.place(x=250, y=150)
    #win.destroy()
    
def chng1():
    global podpowiedzi
    podpowiedzi=1
    index=[i for i in range(10,100) if i%10!=0]
    global LST
    for j in index:
        buttons[j].configure(background="light blue")
        if dane[j]==str(dane[int(last_clicked)]) and dane[j]!=' ':
            buttons[j].configure(background="steel blue")
            LST=str(dane[int(last_clicked)])
            ##brakuje zielonego
    buttons[int(last_clicked)].configure(background="chartreuse3")
            

def chng2():
    global podpowiedzi
    podpowiedzi=0
    index=[i for i in range(10,100) if i%10!=0]
    for j in index:
        buttons[j].configure(background="light blue")
    buttons[int(last_clicked)].configure(background="chartreuse3")
    

def main():
    global podpowiedzi
    make_sudoku()

    remove_some_data(no_to_remove)
    
    dane_start_gry=dane
    print(yes_or_not)
   # print(dane)
    window=tk.Tk()
    window.title("Sudoku by M")
    window.geometry("1024x768+0+0")
    menu=tk.Label(bg="dark blue")
    window.configure(background="light yellow")

    ix=[i for i in range(9)]
    game=[]
    for i in ix:
        game.append(tk.LabelFrame(height=12, width=27,bg='dark blue',  padx=2, pady=2))

              
    p1=tk.Button(menu,text="Nowa gra", height=HEIGHT, width=WIDTH, bd=BD, background='light blue', activebackground="gold2" )
    p2=tk.Button(menu,text="Od nowa", height=HEIGHT, width=WIDTH, bd=BD,background='light blue', activebackground="gold2")
    p3=tk.Button(menu,text="Zapisz grę", height=HEIGHT, width=WIDTH, bd=BD, background='light blue',activebackground="gold2")
    p4=tk.Button(menu,text="Wczytaj grę", height=HEIGHT, width=WIDTH, bd=BD, background='light blue',activebackground="gold2")
    p5=tk.Button(menu,text="Rekordy", height=HEIGHT, width=WIDTH,background='light blue', bd=BD, activebackground="gold2")
    p6=tk.Button(menu,text="Wyjście", height=HEIGHT, width=WIDTH,background='light blue', bd=BD, activebackground="gold2", command=lambda:exiiit(window))
    rad1=tk.Radiobutton(window, anchor='w',bg='light blue',bd=BD+5,width=20, text="Podpowiedzi włączone", activebackground="gold2",value=1,command=lambda:chng1())
    rad2=tk.Radiobutton(window, anchor='w',bg='light blue',bd=BD+5,width=20,text="Podpowiedzi wyłączone", activebackground="gold2",value=0,command=lambda:chng2())
 

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
    #print(btns[3])
    
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
    
    #print(index)
    pixel = tk.PhotoImage(width=1, height=1)
    for i in index:
        quad=i//10-1
        try:
            txt=dane[i][0]
        except:
            txt='xd'
       # print(txt)
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
    p5.grid(row=5, column=1)
    p6.grid(row=6, column=1)
    ##
    rad1.place(x=25, y=400)
    rad2.place(x=25, y=435)

    window.mainloop()
 
main()
