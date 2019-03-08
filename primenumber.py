#This program uses a loop to check if an integer is a prime number
from math import sqrt
while True:
    n = int(input("please enter a number，if you wanna end this program, enter 0 ："))
    if n == 0: break
#The largest factor of a composite number is less than or equal to its square root
    r = int(sqrt(n))
#Decompose the factor of this composite number in a circular way
    for i in range(2,r+1,1):
        if n%i == 0:
            print(n," is a composite number")
            print(n,"=",i,'*',int(n/i))
            break
#This process can be optimized. A composite number can be decomposed into the product of its total prime factor.
    else: print(n," is prime number")
