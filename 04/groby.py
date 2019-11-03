import turtle
import sys

ALEJKA=10 #szerokosc alejki
BOK=65 #dlugosc boku kwatery
RAMIE=0.4*BOK

SKALA=0.2 #do czaszki
PEN_SIZE=1 #do czaszki

def kwartal (n,m):
    kw=[]
    for i in range(n):
        x=[]
        for j in range(m):
            x.append(None)
        kw.append(x)
    return kw

def rysuj(kw):
    x=len(kw)
    y=len(kw[0])
    rysuj_obwod(x,y)
    rysuj_kwatery(x,y)
    for i in range(len(kw)):
        for j in range(len(kw[i])):
            if kw[i][j]==None:
                continue
            elif kw[i][j]=={}:
                rysuj_czaszke(i,j)
            elif kw[i][j]["typ"]=='r':
                rysuj_rozgwiazde(i,j,kw[i][j]["ilosc_ramion"])
            elif kw[i][j]["typ"]=='s':
                rysuj_slimaka(i,j,kw[i][j]["srednica"],kw[i][j]["ilosc_zwojow"])
            else:
                print("ERROR klasy id -> Idiot Developer")
                exit()
      
def koparka(kw,x,y,*arg):
    if kw[x][y]==None:
        kw[x][y]={}
    elif kw[x][y]=={}:
        print("Przecież przed chwilą tu kopałeś!...")
    else:
        print("Serio? Trupa chcesz wykopać? Beze mnie takie numery...!")

    for i in range(0,len(arg),2):
        if kw[arg[i]][arg[i+1]]==None:
            kw[arg[i]][arg[i+1]]={}
        elif kw[arg[i]][arg[i+1]]=={}:
           print("Przecież przed chwilą tu kopałeś!...")
        else:
           print("Serio? Trupa chcesz wykopać? Beze mnie takie numery...!")
    return kw

def zakop_rozgwiazde(kw,x,y,r,*arg):
    if kw[x][y]==None:
        print("Wykop najpierw dołek!")
        return None
    elif kw[x][y]!={}:
        print("Tu już jest coś zakopane!!...")
    else:
        kw[x][y]={"ilosc_ramion":r,"typ":'r'}
        kw[x][y].update()

    for i in range(0,len(arg),3):
        if kw[arg[i]][arg[i+1]]==None:
            print("Wykop najpierw dołek!")
            return None
        elif kw[arg[i]][arg[i+1]]!={}:
            print("Tu już jest coś zakopane!!...")
        else:
            kw[arg[i]][arg[i+1]]={"ilosc_ramion":arg[i+2],"typ":'r'}
            kw[arg[i]][arg[i+1]].update()

def zakop_slimaka(kw,x,y,fi,zwoje,*arg):
    if kw[x][y]==None:
        print("Wykop najpierw dołek!")
        return None
    elif kw[x][y]!={}:
        print("Tu już jest coś zakopane!!...")
    else:
        kw[x][y]={"srednica":fi,"ilosc_zwojow":zwoje,"typ":'s'}
        kw[x][y].update()

    for i in range(0,len(arg),4):
        if kw[arg[i]][arg[i+1]]==None:
            print("Wykop najpierw dołek!")
            return None
        elif kw[arg[i]][arg[i+1]]!={}:
            print("Tu już jest coś zakopane!!...")
        else:
            kw[arg[i]][arg[i+1]]={"srednica":arg[i+2],"ilosc_zwojow":arg[i+3],"typ":'s'}
            kw[arg[i]][arg[i+1]].update()
   
def rysuj_obwod(x,y):
    turtus=turtle.Turtle()
    turtus.up()
    turtus.goto(-400,400)
    turtus.down()
    turtus.pensize(2)
    turtus.fd((BOK+ALEJKA)*y+ALEJKA)
    turtus.rt(90)
    turtus.pensize(4)
    turtus.fd((BOK+ALEJKA)*x+ALEJKA)
    turtus.rt(90)
    turtus.fd((BOK+ALEJKA)*y+ALEJKA)
    turtus.rt(90)
    turtus.pensize(2)
    turtus.fd((BOK+ALEJKA)*x+ALEJKA)
    turtus.rt(90)
    turtus.hideturtle()

def rysuj_kwatery(x,y):
    turtus=turtle.Turtle()
    turtus.up()
    turtus.goto(-400,400)
    turtus.down()
    for i in range(y):
        turtus.fd(ALEJKA)
        turtus.rt(90)
        turtus.up()
        turtus.fd(ALEJKA)
        turtus.down()
        for i in range(x):
            turtus.fd(BOK)
            turtus.up()
            turtus.fd(ALEJKA)
            turtus.down()
            
        turtus.lt(90)
        turtus.fd(BOK)
        turtus.lt(90)
        turtus.up()
        turtus.fd(ALEJKA)
        turtus.down()
        turtus.pensize(2)
        for i in range(x):
            turtus.fd(BOK)
            turtus.up()
            turtus.fd(ALEJKA)
            turtus.down()
        turtus.pensize(1)      
        turtus.rt(90)
    turtus.hideturtle()
    
    turtus=turtle.Turtle()
    turtus.up()
    turtus.goto(-400,400)
    turtus.down()

    for i in range(x):
        turtus.rt(90)
        turtus.up()
        turtus.fd(ALEJKA)
        turtus.lt(90)
        turtus.fd(ALEJKA)
        turtus.down()
        for i in range(y):
            turtus.fd(BOK)
            turtus.up()
            turtus.fd(ALEJKA)
            turtus.down()

        turtus.rt(90)
        turtus.fd(BOK)
        turtus.rt(90)
        turtus.up()
        turtus.fd(ALEJKA)
        turtus.down()
        turtus.pensize(2)
        for i in range(y):
            turtus.fd(BOK)
            turtus.up()
            turtus.fd(ALEJKA)
            turtus.down()
        turtus.pensize(1)
        turtus.rt(180)
    turtus.hideturtle()

def rysuj_rozgwiazde(x,y,r):
    new_x=-400+(BOK+ALEJKA)*y+ALEJKA+(BOK//2)
    new_y=400-(BOK+ALEJKA)*x-ALEJKA-(BOK//2)
    turtus=turtle.Turtle()
    turtus.up()
    turtus.goto(new_x,new_y)
    turtus.down()
    angle=360//r
    for i in range(r):
        turtus.fd(RAMIE)
        turtus.backward(RAMIE)
        turtus.rt(angle)
    turtus.hideturtle()

def rysuj_czaszke(xx,yy):
    t=turtle.Turtle()
    t.pensize(PEN_SIZE)
    t.up()
    t.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy,400-(ALEJKA*1.5)-(ALEJKA+BOK)*xx)
    t.down()
    t.circle(-SKALA*200,20)
    t.circle(-SKALA*60,85)
    t.fd(SKALA*30)
    t.circle(-SKALA*10,20)
    t.fd(SKALA*10)
    t.circle(-SKALA*10,20)
    t.fd(SKALA*10)
    t.circle(SKALA*2,90)
    t.fd(SKALA*25)
    t.circle(-SKALA*20,150)
    t.circle(SKALA*15,110)
    t.fd(SKALA*30)
    t.bk(SKALA*10)
    t.rt(80)
    for i in range(3):
        t.fd(SKALA*15)
        t.rt(95)
        t.fd(SKALA*12)
        t.bk(SKALA*20)
        t.fd(SKALA*8)
        t.lt(95)
    t.hideturtle()
    
    x=turtle.Turtle()
    x.pensize(PEN_SIZE)
    x.up()
    x.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy,400-(ALEJKA*1.5)-(ALEJKA+BOK)*xx)
    x.down()
    x.rt(180)
    x.circle(SKALA*200,20)
    x.circle(SKALA*60,85)
    x.fd(SKALA*30)
    x.circle(SKALA*10,20)
    x.fd(SKALA*10)
    x.circle(SKALA*10,20)
    x.fd(SKALA*10)
    x.circle(SKALA*-2,90)
    x.fd(SKALA*25)
    x.circle(SKALA*20,150)
    x.circle(SKALA*-15,110)
    x.fd(SKALA*30)
    x.bk(SKALA*10)
    x.lt(80)
    for i in range(3):
        x.fd(SKALA*15)
        x.lt(95)
        x.fd(SKALA*12)
        x.bk(SKALA*20)
        x.fd(SKALA*8)
        x.rt(95)
    x.hideturtle()

    t=turtle.Turtle()
    t.pensize(PEN_SIZE)
    t.up()
    t.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy,400-(ALEJKA*1.5)-(ALEJKA+BOK)*xx)
    t.down()
    t.circle(SKALA*-200,20)
    t.circle(SKALA*-60,85)
    t.fd(SKALA*30)
    t.circle(SKALA*-10,20)
    t.fd(SKALA*10)
    t.circle(SKALA*-10,20)
    t.fd(SKALA*10)
    t.circle(SKALA*2,90)
    t.fd(SKALA*25)
    t.circle(SKALA*-20,130)
    t.lt(80)
    t.fd(SKALA*70)
    t.circle(SKALA*-10,60)
    t.fd(SKALA*50)
    t.hideturtle()
    
    x=turtle.Turtle()
    x.pensize(PEN_SIZE)
    x.up()
    x.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy,400-(ALEJKA*1.5)-(ALEJKA+BOK)*xx)
    x.down()
    x.rt(180)
    x.circle(SKALA*200,20)
    x.circle(SKALA*60,85)
    x.fd(SKALA*30)
    x.circle(SKALA*10,20)
    x.fd(SKALA*10)
    x.circle(SKALA*10,20)
    x.fd(SKALA*10)
    x.circle(SKALA*-2,90)
    x.fd(SKALA*25)
    x.circle(SKALA*20,130)
    x.rt(80)
    x.fd(SKALA*70)
    x.circle(SKALA*10,60)
    x.fd(SKALA*50)
    x.hideturtle()

    t=turtle.Turtle()
    t.pensize(PEN_SIZE)
    t.up()
    t.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy+SKALA*20,400-(ALEJKA*1.5)-(ALEJKA+BOK)*xx-SKALA*80)
    t.down()
    t.lt(70)
    t.circle(SKALA*-25,150)
    t.circle(SKALA*-25,-150)
    t.rt(140)
    t.circle(SKALA*25,150)
    t.hideturtle()
    
    x=turtle.Turtle()
    x.pensize(PEN_SIZE)
    x.up()
    x.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy+SKALA*-20,400-(ALEJKA*1.5)-(ALEJKA+BOK)*xx-SKALA*80)
    x.down()
    x.lt(110)
    x.circle(SKALA*25,150)
    x.circle(SKALA*25,-150)
    x.lt(140)
    x.circle(SKALA*-25,150)
    x.hideturtle()

    x=turtle.Turtle()
    x.pensize(PEN_SIZE)
    x.up()
    x.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy,400-(ALEJKA+BOK//2)-(ALEJKA+BOK)*xx)
    x.down()
    x.rt(60)
    x.fd(SKALA*30)
    x.rt(70)
    x.fd(SKALA*15)
    x.rt(110)
    x.fd(SKALA*10)
    x.hideturtle()

    x=turtle.Turtle()
    x.pensize(PEN_SIZE)
    x.up()
    x.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy,400-(ALEJKA+BOK//2)-(ALEJKA+BOK)*xx)
    x.down()
    x.lt(240)
    x.fd(SKALA*30)
    x.lt(70)
    x.fd(SKALA*15)
    x.lt(110)
    x.fd(SKALA*10)
    x.hideturtle()

   
def rysuj_slimaka(xx,yy,srednica, pi_kat):

    ilosc_krokow=pi_kat*2
    x=turtle.Turtle()
    x.up()
    x.goto(-400+ALEJKA+BOK//2+(ALEJKA+BOK)*yy,400-(ALEJKA+BOK//2)-(ALEJKA+BOK)*xx)
    x.down()
    x1=1
    x2=1
    fibo=[1,1]

    for i in range(ilosc_krokow):
        x3=(x1+x2)*0.7
        fibo.append(x3)
        x1=x2
        x2=x3

    t=len(fibo)
    t1=fibo[t-1]
    t2=fibo[t-2]
    t=t1+t2
    print(t)

    xxx=float(srednica)/float(t)
    print(xxx)
    
    print(fibo)
    for i in range(len(fibo)):
        fibo[i]=fibo[i]*xxx*2
    print(fibo)
      
    nr_squares=len(fibo)
    for i in range(nr_squares):
        x.circle(-0.5*fibo[i],90)
    x.hideturtle()


#Copyright by mglodziak.

