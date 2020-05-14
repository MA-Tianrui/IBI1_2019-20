#4.1 Some simple math
print("Part 1:")
a = 996
print("a is", a)
b = 996996
c = 996996/7
d = c/11
e = d/13
print ("e is", e)
print ("e-a is ", e-a)
if e-a<0:
    print("a is greater than e")
elif e-a>0:
    print("e is greater than a")
else:
    print("e is equal to a")

#4.2 Booleans
print()
print("Part 2:")
for X in [True, False]:
    for Y in [True, False]:
        Z = (X and not Y) or (Y and not X)
        W = X != Y
        print("When X is ", X, " and Y is ", Y, ", Z is ", Z, " and W is ", W, ".", sep="")
print("W and Z are also same.")