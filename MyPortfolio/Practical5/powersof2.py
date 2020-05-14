#start with a positive integer N
N = float(input("Enter a positive integer N:"))
#print the start of sentence
print(str(N), "is", end = " ")
#a loop from 12 to 0, assume that N < 8192
for i in range(12,-1,-1):
#if the integer larger than a power of 2, minus the power of 2
    if N >= 2**i:
        N = N - 2**i
#change float into str
        power = str(i)
#print every power of 2
#when N=0, we do not need a "+" behind the powers of 2
        if N == 0: 
            print("2**", power, sep="")
        else:
            print("2**", power, " +", end = " ", sep="")