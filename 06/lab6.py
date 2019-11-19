# -*- coding: utf-8 -*-
#wygenerować listę współrzędnych macierzy 10x10, pierwsza od -5 do 5, druga od 100 do 110
#korzystaj z list comprehension

l=[ (x, y)  for y in range(100,110,1) for x in range(-5,5,1)]
print(l)



