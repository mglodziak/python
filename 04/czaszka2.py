import turtle
SKALA=0.3
PEN_SIZE=1

def rysuj_czaszke():
    t=turtle.Turtle()
    t.pensize(PEN_SIZE)
    t.up()
    t.goto(0,SKALA*200)
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
    x.goto(0,SKALA*200)
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
    t.goto(0,SKALA*200)
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
    x.goto(0,SKALA*200)
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
    t.goto(SKALA*20,SKALA*80)
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
    x.goto(SKALA*-20,SKALA*80)
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
    x.goto(0,SKALA*60)
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
    x.goto(0,SKALA*60)
    x.down()
    x.lt(240)
    x.fd(SKALA*30)
    x.lt(70)
    x.fd(SKALA*15)
    x.lt(110)
    x.fd(SKALA*10)
    x.hideturtle()

rysuj_czaszke()

