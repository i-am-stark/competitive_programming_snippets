""" Given an even number N (greater than 2), return two prime numbers whose sum
will be equal to given number. There are several combinations possible. Print 
only the pair whose minimum value is the smallest among all the minimum values of pairs. """

def isprime(n):
    if(n>1):
        for i in range (2,n):
            if (n%i == 0):
                return False
        return True
    return False
for t in range(int(input())):
    num = int(input())
    for i in range(num):
        if(isprime(i) and isprime(num-i)):
            print(i, num-i)
            break