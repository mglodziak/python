def Newton( n, k ):
 
    Wynik = 1
        for i in range( 1, k+1 ):
            Wynik = Wynik * ( n - i + 1 ) / i
        return Wynik
     
    t = int( raw_input() )
     
    for i in range(t):
        n,k = map( int, raw_input().split() )
        if k == 0 or k == n : print '1'
        else :
            print Newton(n,k)
