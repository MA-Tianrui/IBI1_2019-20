# What does this piece of code do?
# Answer: The code output a random prime number (or 1) from 1 to 100

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:
    p=True
#draw a number between 1 and 100
    n = randint(1,100)
#compute the square root of n, and get the next higher integer of the square root
    u = ceil(n**(0.5))
#check whether n can be divided by integer from 2 to the particular integer larger than its square
    for i in range(2,u+1):
        if n%i == 0:
#if n can be divided, repeat the above step, draw a new n
            p=False


     
#if n cannot be divided, n is a prime number (or 1), print n
print(n)
