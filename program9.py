""" Given the co-effecients of X,Y and Z in a system of simultaneous equations.
 Find the values of X,Y and Z.

 a1X + b1Y + c1Z = d1
 a2X + b2Y + c2Z = d2
 a3X + b3Y + c3Z = d3 """
 
import numpy
for _ in range(int(input())):
    m1=list(map(float,input().split()))
    m3=list(map(float,input().split()))
    m2=list(map(float,input().split()))
    a=numpy.array([m1[:3],m2[:3],m3[:3]])
    b=numpy.array([m1[3],m2[3],m3[3]])
    if numpy.linalg.det(a)==0:
        print("0")
    else:
        x=numpy.dot(numpy.linalg.inv(a),b)
        print(*map(int,numpy.floor(x)))