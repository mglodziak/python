import itertools
#print(list(itertools.permutations(['1','2','3'])))

#rekurencja w pythonie

#procedura, dla danej funkcji i Q wyznacza minimum funkcji 

def f(a,b,c,d):
    pass
    #return float

def procedura(funkcja, omega, potega):
    pass


x=[2,3,3,5]
y=[1,1,5,3]
z=[0,1,3,2]
t=[3,2,1,4]

lista=list()
for element in itertools.product(x,y,z,t):
    #print(*element)
    pass


def g(*ll):
    print(len(ll))
    if not ll:
        return []
    if len(ll)==1:
        return [(e,) for e in ll[0]]
    L=[]
    for post in g( *ll [1:]):
        for pre in ll[0]:
            L.append( (pre,)+post)
    return L

xx=g(x)
print(xx)

#mamy sekwencję przestrzeni Ω1, Ω2, Ω3, itd.
#f: iloczyn od i/1 do 3 Ωi -> float
#g należy do float

#wyliczyć sumę z modułów

#po ilu wartościach, ta suma przekroczy zadany parametr g

#funkcja liczy il. kartezjański, robię pętle po nim, sumuję, przestrzenie Ω mogą być duże w ciul, trzeba lazy evaluation
#lazy evaluation -> proste generatory, zamiast returna ma yield.

def H(L,t):
    R=[]
    for l in R:
        for x in range(t):
            R.append(x*(l,))
    return R

def Hg(L,t):
    for l in L:
        for x in range(t):
            e=x*(l,)
            yield e


for z in Hg('abc',3):
    print(z)
    

