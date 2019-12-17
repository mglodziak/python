import tkinter as tk
import random
import tkinter.font as font

HEIGHT=2
WIDTH=11
BD=3
FONT_SIZE=20
#fnt=tkFont.Font(size=25)

dane={}
#myFont = font.Font(size=30)

def starter(ss):
    print(ss)

def okienko_do_wpisania_cyferki():
    win=tk.Toplevel()
    win.title("Podaj cyfrę")
    win.geometry("210x210+100+470")

    labels=[]
    for k in range(9):
        labels.append(tk.LabelFrame(win,width=70,height=70))
        labels[k].grid_rowconfigure(0, weight=1)
        labels[k].grid_columnconfigure(0, weight=1)    
        labels[k].grid_propagate(False)

    labels[0].grid(row=1,column=1)
    labels[1].grid(row=1,column=2)
    labels[2].grid(row=1,column=3)
    labels[3].grid(row=2,column=1)
    labels[4].grid(row=2,column=2)
    labels[5].grid(row=2,column=3)
    labels[6].grid(row=3,column=1)
    labels[7].grid(row=3,column=2)
    labels[8].grid(row=3,column=3)
    

    
    t1=tk.Button(labels[0], text="1",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue", command=lambda:starter('1'))
    t2=tk.Button(labels[1], text="2",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue")
    t3=tk.Button(labels[2], text="3",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue")
    t4=tk.Button(labels[3], text="4",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue")
    t5=tk.Button(labels[4], text="5",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue")
    t6=tk.Button(labels[5], text="6",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue")
    t7=tk.Button(labels[6], text="7",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue")
    t8=tk.Button(labels[7], text="8",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue")
    t9=tk.Button(labels[8], text="9",font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue")   
  
   # frame.place(x=0,y=0)
  
    t1.grid(row=0,column=0, sticky='nesw')
    t2.grid(row=0,column=0, sticky='nesw')
    t3.grid(row=0,column=0, sticky='nesw')
    t4.grid(row=0,column=0, sticky='nesw')
    t5.grid(row=0,column=0, sticky='nesw')
    t6.grid(row=0,column=0, sticky='nesw')
    t7.grid(row=0,column=0, sticky='nesw')
    t8.grid(row=0,column=0, sticky='nesw')
    t9.grid(row=0,column=0, sticky='nesw')


def fn(btn):
    
    okienko_do_wpisania_cyferki()
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
        return res
        
    else:    
        try:
            y=st[21]
        except:
            y=1
        res=str(x)+str(y)
        print(res)
        return res

def main():
    window=tk.Tk()
    window.title("Sudoku by M")
    window.geometry("1024x768+0+0")
    menu=tk.Label(bg="black")
    window.configure(background="light yellow")

    ix=[i for i in range(9)]
    game=[]
    for i in ix:
        game.append(tk.LabelFrame(height=12, width=27,bg='black',  padx=2, pady=2))

              
    p1=tk.Button(menu, text="Nowa gra", height=HEIGHT, width=WIDTH, bd=BD, background='light blue', activebackground="gold2" )
    p2=tk.Button(menu, text="Wczytaj grę", height=HEIGHT, width=WIDTH, bd=BD,background='light blue', activebackground="gold2")
    p3=tk.Button(menu, text="Zapisz grę", height=HEIGHT, width=WIDTH, bd=BD, background='light blue',activebackground="gold2")
    p4=tk.Button(menu, text="Rekordy", height=HEIGHT, width=WIDTH,background='light blue', bd=BD, activebackground="gold2")
    p5=tk.Button(menu, text="Wyjście", height=HEIGHT, width=WIDTH,background='light blue', bd=BD, activebackground="gold2")
    
    
    for i in ix:
        if i%3==0:
            game[i].place(x=277, y=100+i*66)
        elif i%3==1:
            game[i].place(x=485, y=34+i*66)
        elif i%3==2:
            game[i].place(x=693, y=i*66-32)

    index=[i for i in range(10,100) if i%10!=0]

    global buttons

    buttons={}

    
    print(index)
    for i in index:
        quad=i//10-1
        obj=tk.Button(game[quad], text=random.randrange(1,10),width=5, height=3, background="light blue",activebackground="gold2")
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
            
    
    menu.place(x=10, y=100)    
    p1.grid(row=1, column=1)
    p2.grid(row=2, column=1)
    p3.grid(row=3, column=1)
    p4.grid(row=4, column=1)
    p5.grid(row=5, column=1)

    

    window.mainloop()
 

    
main()
