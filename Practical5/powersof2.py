#start with a positive integer N
N = float(input("Enter a positive integer N:"))
#print the start of sentence
print(str(N), "is", end = " ")
#loop
for i in range(12,-1,-1):
#if the integer larger than a power of 2, minus the power of 2
    if N >= 2**i:
        N = N - 2**i
#print every power of 2
        if N == 0:
            print("2**", str(i))
        else:
            print("2**", str(i), "+", end = " ")