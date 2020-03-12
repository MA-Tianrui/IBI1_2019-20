#take a positive integer n
N = float(input("Enter a positive integer:"))
#check if it is a positive integer
if N <= 0 or N%1 != 0:
    print("it is not a positive integer.")
else:
    print(N)
#repeat until 1 occurs
    while N != 1:
#check whether it is an odd or an even, then compute
        if N %2 == 0:
            N = N/2
        else:
            N = N*3+1
        print(N)
#stop when 1 occurs
    print("We stop at 1.")