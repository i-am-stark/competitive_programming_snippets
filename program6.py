""" Given two expressions ex1 and ex2 in the form of strings. The task is to 
compare them and check if they are similar. Expressions consist of lowercase 
alphabets, '+', '-' and  '( )'. """

import string
t=int(input())
while t>0:
    s1 = input()
    s2 = input()
    a, b = "", ""
    h1, h2 = "", ""
    for i in s1 :
        if i in string.ascii_lowercase :
            a += str(ord(i)**3)
            h1 += i
        else:
            a += i
    for i in s2 :
        if i in string.ascii_lowercase :
            b += str(ord(i)**3)
            h2 += i
        else:
            b += i
    a, b = eval(a), eval(b)
    print (["NO", "YES"][a==b])
    t-=1