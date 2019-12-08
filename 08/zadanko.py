import math
import turtle as turtuś
from random import randrange

π=math.pi

def okrag (x,y,R,ang):
    new_x=R*math.cos(ang*π/180)
    new_y=R*math.sin(ang*π/180)
    
    return (x+new_x, y+new_y, ang)


def generator(x,y,R,krok):
    for i in range(0,361,krok):
#        print(i)
        yield okrag(x,y,R,i)



def rysuj(lista):
    x=turtuś.tracer(False)
    x=turtuś.Turtle()
    turtuś.colormode(255)

    x=turtuś.Turtle()
    
    for i in lista:

        
        print(i)
        x.penup()
        x.setpos(i[0],i[1])
        
        #x.lt(i[2])
        x.rt(90)
        x.fd(20)
        x.lt(90)
        #x.rt(i[2])
        
        x.pendown()
        x.fillcolor(randrange(255),randrange(255),randrange(255))
        x.begin_fill()
        x.circle(20)
        x.end_fill()
        print(i[2])
        
#    x=turtuś.Turtle()
#    x.rt(90)
#    x.fd(300)
#    x.lt(90)
#    x.circle(300)
#    x=turtuś.tracer(True)

    

x=generator(0,0,300,30)
y= list(x)
#print(y)

rysuj(y)

