# -*- coding: ISO-8859-1 -*-

n = 2

while 1:
    
    n = n + 1

    controle = 0

    for i in range(1,n):

        if n%i == 0:

            controle = controle + i

    if controle == n:

        print(n, "\té um numero perfeito")
