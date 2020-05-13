import sys

# input a group of numbers and check if they fulfill the criteria
ori = input("Please input numbers to compute 24 (use ',' to divide them): ")

num = []
num_str = ori.split(',')
for i in num_str:
    j = float(i)
    num.append(j)
    if j%1 != 0 or j > 23 or j < 1:
        print('The input number must be integers from 1 to 23')
        sys.exit(0)


# get all the sitution and put them into one list
def cal(l):
   rl = []
   for i in list(range(l-1)):
      for j in list(range(i+1,l)):
          for k in range(6):
             rl.append([i, j, k])
   return rl
   

sc = [[], []]
for i in range(2, len(num) + 1):
   sc.append(cal(i))


sci = []
for i in range(len(num)):
   sci.append(sc[len(num) - i])


allSit = []
def select_copy(l):
   l_copy = l.copy()
   if len(l_copy) == len(sci) - 1:
      allSit.append(l_copy)
   for i in sci[len(l)]:
      l.append(i)
      select_copy(l)
      l.pop()
   
select_copy([])


# try all the calculation way between two number
def op(i, j, k, l):
    if k == 0:
        value = l[i] + l[j]
    elif k == 1:
        value = l[i] - l[j]
    elif k == 2:
        value = l[j] - l[i]
    elif k == 3:
        value = l[i] * l[j]
    elif k == 4 and l[j] != 0:
        value = l[i] / l[j]
    elif k == 5 and l[i] != 0:
        value = l[j] / l[i]
    else:
        value = 0
    if value == 24:
        return 1
    else:
        l[i] = value
        l.pop(j)
        return 0
    
# find if 24 can be got in every situation and calculate the repeat times
get24 = False
n = 0
for i in allSit:
   num_copy=num.copy()
   for j in i:
       if op(j[0], j[1], j[2], num_copy) == 1 and get24 == False:
          print("Yes")
          get24 = True
       n += 1

if get24 == False:
    print("No")

# this number of times is the worst situation
print('Times:', n)