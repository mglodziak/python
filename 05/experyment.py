g="sHa"

def G(x):
    print(g,x)

def H (f,y):
    print(f(y))

def H1(f,y):
    g="oth"
    #print(f(y))
    return G

def H2(y):
    def G(x):
        print(g,x)
    #print (G(y))
    return G

def H3():
    g="oth"
    def G(x):
        print(g,x)
    #print(G(y))
    return G

def H4(f,y):
    global g
    g = "trutututu"
    print(f(y))
    
#G(3)
#H(G,2)
#H1(G,2)
#H2(2)

#g1=H3()
#print(g1(2))
#print(g1)

#H4(G,2)

g="sth"; e="oth"
def G(y):
    g="else"
    def I():
        nonlocal g
        g=2*y
        e=y
        print(g,e)
        #e=y
    print(g)
    return I


def T():
    p=1
    q="a"
    w=None
    def L():
        p=2
        q="b"
        def B():
            nonlocal p,w
            w=44
            p=3
            q="c"
            print(p,q,w)
        B()
        print(p,q,w)
    L()
    print(p,q,w)

    #nielokalne są w sobie zagnieżdżone, nie da się tego zmienić

