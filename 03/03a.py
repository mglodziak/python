#algorytm euklidesa

a=eval(input("Set first number: "))
while not isinstance(a,int):
    print("Set number only!")
    a=eval(input(": "))

b=eval(input("Set second number: "))
while not isinstance(b,int):
    print("Set number only!")
    b=eval(input(": "))

c=0
d=a
while a>=0:
    a=a-b
    c=c+1
c=c-1
a=a+b
print (d,"=", b, "*", c, "+", a)
