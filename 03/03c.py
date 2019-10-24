#wyznacz najmniejsze x liczb pierwszych (max 20).
#narysuj gwiazdę n ramienną, gdzie n oznacza znalezioną kolejną liczbę pierwszą.


import turtle

def draw_star(n):
    for i in range(1,n+1):
        turtus.fd(450)
        angle=(n-1)*(180/n)
        turtus.rt(angle)


limit=20

limit=eval(input("Set count of primary numbers: "))
n=eval(input("Set which number has been used to drawing star: "))

if limit > 20:
    
    print("Max value is 20!")
    limit=20

    
tab=[2,]       
i=3
while len(tab) < limit:
    for j in tab:            
        if i % j == 0: break 
    else: 
        #yield i              
        tab.append(i)
    i=i+2
print(tab)
 

turtus=turtle.Turtle()

num=tab[n-1]
draw_star(num)

