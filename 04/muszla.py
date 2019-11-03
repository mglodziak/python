import turtle
import sys


def rysuj_slimaka(srednica, pi_kat):

    ilosc_krokow=pi_kat*2
    x=turtle.Turtle()
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
    x.rt(90)
    x.fd(srednica)
    x.rt(90)
    x.fd(srednica)


rysuj_slimaka(40,5)
