# -*- coding: utf-8 -*-
#wygenerować listę współrzędnych macierzy 10x10, pierwsza od -5 do 5, druga od 100 do 110
#korzystaj z list comprehension

import math
import turtle

PI=3.14



def skala(x):
    l=[]
    for i in x:
        element=i/PI
        l.append(element)
    krotka=tuple(l)
    return krotka

def wylicz(x):
    return math.sin(x[0])*math.cos(x[1])      
        

l=[ (x, y)  for y in range(-25,26,1) for x in range(-25,26,1)]
xx=list(map(skala, l))

yy=list(map(wylicz,xx))

#print(yy)

turtus=turtle.Turtle()
turtus.circle()
