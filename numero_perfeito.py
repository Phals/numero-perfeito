# -*- coding: ISO-8859-1 -*-

# Numeros perfeitos

import time

n = 0

ini = time.clock()

while 1:
    
    n = n + 2
    controle = 0
    
    for i in range(1,n):
        if n%i == 0:
            controle = controle + i
            
    if controle == n:
        print n, 'eh um numero perfeito => Tempo programa:', (time.clock())-ini
    
    if n%1000 == 0:
        print 'Numero: ', n, 'Tempo programa: ', (time.clock())-ini
