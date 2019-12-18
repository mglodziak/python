import tkinter as tk
import random
import tkinter.font as font

HEIGHT=2
WIDTH=11
BD=3
FONT_SIZE=18
#fnt=tkFont.Font(size=25)

dane={}
#myFont = font.Font(size=30)

def starter(ss):
    print(ss)


def fn(btn):

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
def fn2(btn):
    st=str(btn)
    x=st[12]
    y=st[13]
    res=str(x)+str(y)
    res=int(res)-9
    print(res)
    

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


    labe=[]
    btns=[]
    for k in range(9):
        labe.append(tk.LabelFrame(window,width=70,height=70))
        labe[k].grid_rowconfigure(0, weight=1)
        labe[k].grid_columnconfigure(0, weight=1)    
        labe[k].grid_propagate(False)
        labe[k].place(x=275+k*70,y=660)
        obj=(tk.Button(labe[k], text=k+1,font=('Helvetica',FONT_SIZE), background="gold2",activebackground="light blue"))
        obj.configure(command=lambda btn=obj:fn2(btn))
        btns.append(obj)
        btns[k].grid(row=0,column=0, sticky='nesw')
        
    print(btns[3])
    
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
    
    print(index)
    pixel = tk.PhotoImage(width=1, height=1)
    for i in index:
        quad=i//10-1
        obj=tk.Button(game[quad], text=random.randrange(1,10),compound='c',font=('Helvetica',FONT_SIZE),image=pixel,width=40, height=50, background="light blue",activebackground="gold2")
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
            
    
    menu.place(x=20, y=200)
    p1.grid(row=1, column=1)
    p2.grid(row=2, column=1)
    p3.grid(row=3, column=1)
    p4.grid(row=4, column=1)
    p5.grid(row=5, column=1)

    

    window.mainloop()
 

    
main()
