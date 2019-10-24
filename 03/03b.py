#wyznacz pierwsze x liczb pierwszych (max 20)





def pierwsze(limit):

    if limit > 20:
        print("Max value is 20!")
        limit=20
    
    tab=[2,]       
   # for i in range(2,limit):
    i=3
    while len(tab) < limit:
        for j in tab:            
            if i % j == 0: break 
        else: 
            yield i              
            tab.append(i)
        i=i+2
    print(tab)
 
for i in pierwsze(20):
    #print(i)
    pass
   
#pierwsze(30)


