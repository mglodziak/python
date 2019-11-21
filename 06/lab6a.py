# -*- coding: utf-8 -*-
#wygenerować listę współrzędnych macierzy 10x10, pierwsza od -5 do 5, druga od 100 do 110
#korzystaj z list comprehension

import math
import turtle

PI=3.14
SKALA=10 #10 dla ładnego rysunku
SK_RYS=50 #50 dla ładnego rysunku
ROZNORODNOSC=777   #10000, 666 123 325 69 #777best


def skala(x):
    l=[]
    for i in x:
        element=i/PI
        l.append(element)
    krotka=tuple(l)
    return krotka

def wylicz(x):
    return math.sin(x[0])*math.cos(x[1])*SKALA      
        
l=[ (x, y)  for y in range(-25,26,1) for x in range(-25,26,1)]
#l=[ (x, y)  for y in range(-35,36,1) for x in range(-55,56,1)]
xx=list(map(skala, l))

yy=list(map(wylicz,xx))

zz=list(zip(xx,yy))

t=turtle.tracer(False)
t=turtle.Turtle()
turtle.colormode(255)

#turtus.circle(50)
for i in range(len(zz)):
    t.up() 
    x1=zz[i][0][0]*ROZNORODNOSC
    if x1<0:
        x1=-x1
    while x1>255:
        x1=x1-255

    x2=zz[i][0][1]*ROZNORODNOSC
    if x2<0:
        x2=-x2
    while x2>255:
        x2=x2-255
        
    x3=zz[i][1]*ROZNORODNOSC
    if x3<0:
        x3=-x3
    while x3>255:
        x3=x3-255   
    if x1<0:
        x1=-x1
    if x2<0:
        x2=-x2
    if x3<0:
        x3=-x3
    #print(x1, x2)
    t.fillcolor(int(x1),int(x2),int(x3))
    t.setx(zz[i][0][0]*SK_RYS)
    t.sety(zz[i][0][1]*SK_RYS)
    t.down()
    t.begin_fill()
    t.circle(zz[i][1])
    t.end_fill()
t.hideturtle()
t=turtle.tracer(True)

    
