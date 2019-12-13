import tkinter as tk
HEIGHT=2
WIDTH=11
BD=3
def starter(ss):
    print(ss)

def main():
    window=tk.Tk()
    window.title("Sudoku by M")
    window.geometry("1024x768")
    menu=tk.Label(bg="black")
    window.configure(background="light yellow")

    ix=[i for i in range(9)]
    game=[]
    for i in ix:
        game.append(tk.LabelFrame(height=12, width=27,bg='black',  padx=2, pady=2))

    
            
    p1=tk.Button(menu, text="Nowa gra", height=HEIGHT, width=WIDTH, bd=BD, activebackground="yellow")
    p2=tk.Button(menu, text="Wczytaj grę", height=HEIGHT, width=WIDTH, bd=BD, activebackground="yellow")
    p3=tk.Button(menu, text="Zapisz grę", height=HEIGHT, width=WIDTH, bd=BD, activebackground="yellow")
    p4=tk.Button(menu, text="Rekordy", height=HEIGHT, width=WIDTH, bd=BD, activebackground="yellow")
    p5=tk.Button(menu, text="Wyjście", height=HEIGHT, width=WIDTH, bd=BD, activebackground="yellow")
    
    
    
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
        buttons[i]=tk.Button(game[quad], text="X",width=5, height=3, background="light blue",activebackground="yellow", command=lambda:starter("dupa"))
    print(buttons)
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
            
        
            




    menu.place(x=10, y=768//3)    
    p1.grid(row=1, column=1)
    p2.grid(row=2, column=1)
    p3.grid(row=3, column=1)
    p4.grid(row=4, column=1)
    p5.grid(row=5, column=1)



    window.mainloop()

    
main()
