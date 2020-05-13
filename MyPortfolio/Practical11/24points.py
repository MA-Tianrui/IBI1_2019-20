#data = [1, 2, 3, 4, 5, 6]
#def combine(data, l):
#    result = []
#    tmp = [0]*l
#    length = len(data)
#    def next_num(li=0, ni=0):
#        if ni == l:
#            result.append(copy.copy(tmp))
#            return
#        for lj in range(li,length):
#            tmp[ni] = data[lj]
#            next_num(lj+1, ni+1)
#    next_num()
#    print(result)
#    return result
# 
# 
#combine(data,3)

def PointGame(group):
    

#target每组要输出的元素个数，step游标
def combine(data, step, select_data, target_num):
    #如果已经凑齐一组完成的组合，输出当前组
    if len(select_data) == target_num:
        points(select_data)
        return
    #如果游标超过数组长，说明后续元素都被遍历完成，跳转到上一个元素的循环
    if step >= len(data):
        return
    #把选中的元素加入临时输出列表中，n个一组作为输出
    select_data.append(data[step])
    #递归调整最后一位
    combine(data, step + 1, select_data, target_num)
    #构建一个新组合，首先要删掉上次输出组中药排除的元素
    select_data.pop()
    #递归向上调整一位元素                         
    combine(data, step + 1, select_data, target_num)
 

data = [1, 2, 3, 4, 5, 6]
combine(data, 0, [], 3)
