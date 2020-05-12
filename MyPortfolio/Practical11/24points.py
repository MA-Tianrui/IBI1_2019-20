arr = []
def choice(originData, m):
    n = len(originData)
    if m == 0:
        return arr
    else:
        for i in range(0, n-m):
            arr.append(originData[i])
            arr.extend(choice(originData[i+1:], m-1))
            return arr
            
choice([1,2,3,4,5], 2)